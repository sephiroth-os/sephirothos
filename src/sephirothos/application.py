"""SephirothOS application composition and lifecycle"""

from __future__ import annotations

import math
from dataclasses import replace

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFont
from PySide6.QtCore import QCoreApplication

from config import ConfigStore, AppConfig, AppearanceConfig, ConfigurationError
from sephirothos.events import EventBus
from sephirothos.metadata import (
    APPLICATION_NAME,
    ORGANIZATION_NAME,
    VERSION,
)
from sephirothos.services.display_scale import DisplayScaleService
from sephirothos.services.theme import ThemeService
from sephirothos.ui.metrics import UiMetrics
from sephirothos.ui.shell import Shell

class SephirothOS:
    def __init__(self, argv: list[str], config_store: ConfigStore | None = None) -> None:
        self.qt = QApplication(argv)
        self._configure_metadata()

        self.config_store = config_store or ConfigStore()
        self.config = self.config_store.load()

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

        #todo: bgm soon

        self._connect_events()
        self.theme.apply_current()


    def run(self) -> int:
        self.shell = Shell(self, config=self.config, event_bus=self.event_bus, metrics=self.metrics)
        self.shell.show()

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
