"""SephirothOS application composition and lifecycle"""

from __future__ import annotations

import ctypes
import math
import os
import sys
import time

from dataclasses import replace
from pathlib import Path

from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtGui import QFont
from PySide6.QtCore import QCoreApplication

from sephirothos.config import ConfigStore, AppConfig, AppearanceConfig, ConfigurationError
from sephirothos.events import EventBus
from sephirothos.metadata import (
    APPLICATION_NAME,
    ORGANIZATION_NAME,
    VERSION,
)
from sephirothos.services.background_music import BackgroundMusicService
from sephirothos.services.display_scale import DisplayScaleService
from sephirothos.services.theme import ThemeService
from sephirothos.ui.metrics import UiMetrics
from sephirothos.ui.onboarding.welcome import OnboardingShell
from sephirothos.ui.shell import Shell
from sephirothos.services.update import UpdateService
from sephirothos.ui.mirage import Mirage


class SephirothOS:
    def __init__(self, argv: list[str], config_store: ConfigStore | None = None) -> None:
        self.qt = QApplication(argv)
        self._configure_metadata()

        self.config_store = config_store or ConfigStore()
        self.config = self.config_store.load()

        if self.config.update_in_progress:
            self._update_cleanup()

        self._configure_font()

        self.event_bus = EventBus()
        self.display_scale = self._create_display_scale(self.config)
        self.metrics = UiMetrics.from_scale(self.display_scale)

        self.theme = ThemeService(
            target=self.qt,
            metrics=self.metrics,
            initial_theme=self.config.appearance.theme_id,
            initial_accent=self.config.appearance.accent_id,
        )

        self.shell = None
        self.alt_shell = None
        self.mirage = None

        parent = self.mirage

        self.background_music = BackgroundMusicService(
            parent=self.qt
        )
        self.qt.aboutToQuit.connect(
            self.background_music.stop
        )

        self.update_service = UpdateService(VERSION)

        self._connect_events()
        self.theme.apply_current()


    def run(self) -> int:

        if self.config.onboarding_complete:
            self.shell = Shell(self, config=self.config, event_bus=self.event_bus, metrics=self.metrics)
            self.shell.show()
        else:
            self.mirage = Mirage(self, self.metrics, self.event_bus)
            # self.alt_shell = OnboardingShell(self, config=self.config, event_bus=self.event_bus, metrics=self.metrics)
            # self.alt_shell.show()

        # self.background_music.play()
        self.update_service.check()

        return self.qt.exec()

    def _configure_metadata(self) -> None:
        QCoreApplication.setApplicationName(APPLICATION_NAME)
        QCoreApplication.setApplicationVersion(VERSION)
        QCoreApplication.setOrganizationName(ORGANIZATION_NAME)

    def _connect_events(self) -> None:
        self.event_bus.quit_requested.connect(
            self.qt.quit,
        )
        self.event_bus.appearance_apply_requested.connect(
            self._apply_appearance,
        )
        self.event_bus.pause_music.connect(
            self.background_music.pause,
        )
        self.event_bus.resume_music.connect(
            self.background_music.play,
        )
        self.update_service.update_available.connect(
            self._on_update_available,
        )

    @staticmethod
    def _create_display_scale(config: AppConfig) -> DisplayScaleService:
        return DisplayScaleService(config.appearance.display_scale)

    def _configure_font(self) -> None:
        """Configure the default application font."""

        font_family = self.config.appearance.font_family

        self.qt.setFont(QFont(font_family))

    def _apply_appearance(self, appearance: AppearanceConfig) -> None:
        """Persist and apply an appearance configuration."""

        previous_appearance = self.config.appearance
        applied = replace(appearance)

        try:
            self.config.appearance = applied
            self.config_store.save(self.config)

        except ConfigurationError:
            self.config.appearance = previous_appearance

            self.event_bus.appearance_apply_requested.emit("Could not save appearance settings.")
            return

        restart_required = not math.isclose(
            self.display_scale.factor,
            applied.display_scale,
        )

        self.qt.setFont(
            QFont(applied.font_family),
        )

        theme_changed = self.theme.set_theme(applied.theme_id)

        accent_changed = self.theme.set_accent(applied.accent_id)

        if not theme_changed and not accent_changed:
            # Reapply the stylesheet after changing font
            self.theme.apply_current()

        self.event_bus.appearance_applied.emit(replace(applied), restart_required)

    def _on_update_available(self, update):
        update_consent = QMessageBox.question(
            self.mirage,
            "Update Available",
            "I AM FUCKING RENDERING SOMETHING!",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.Yes,
        )

        if update_consent != QMessageBox.StandardButton.Yes:
            return

        try:
            self.launch_updater()
        except Exception as e:
            QMessageBox.critical(
                self.mirage,
                "Update Failed",
                f"Could not start the updater:\n\n{e}",
            )
            return

        self.qt.quit()

    def launch_updater(self):
        updater = Path(sys.executable).parent / "Updater.exe"

        result = ctypes.windll.shell32.ShellExecuteW(
            None,
            "runas",
            str(updater),
            f"--pid {os.getpid()}",
            str(updater.parent),
            1,
        )

        if result <= 32:
            raise RuntimeError(
                f"Failed to launch updater (ShellExecute error {result})"
            )

    def _update_cleanup(self):
        updater = Path(sys.executable).parent / "Updater.exe"
        new_updater = Path(sys.executable).parent / "Updater.new.exe"

        if not new_updater.exists():
            return

        for _ in range(10):
            try:
                if updater.exists():
                    updater.unlink()

                new_updater.rename(updater)

                print("[updater]: Updater updated successfully.")
                return

            except OSError as e:
                print(f"[updater]: Updater cleanup waiting: {e}")
                time.sleep(0.5)

        print("[updater]: Could not finalize updater update.")