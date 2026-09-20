"""Home taxes page"""
import datetime
from random import choice

import sephirothos.assets.videos.taxes_rc

from PySide6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy
from PySide6.QtCore import Qt, QUrl

from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget

from sephirothos.events import EventBus
from sephirothos.ui.metrics import UiMetrics
from sephirothos.ui.roles import SurfaceRole

class TaxesPage(QWidget):
    """Primary home dashboard."""

    def __init__(self, metrics: UiMetrics, event_bus: EventBus):
        super().__init__()

        self.metrics = metrics
        self.event_bus = event_bus

        self.setProperty(
            "surfaceRole",
            SurfaceRole.TRANSPARENT.value
        )

        self._build_ui()

    def _build_ui(self):
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,
        )
        self.main_layout.setSpacing(self.metrics.space_20)

        self.taxes_card = TaxesCard(self.metrics, self.event_bus)

        self.main_layout.addWidget(self.taxes_card, 1)

    def start_taxes(self):
        self.taxes_card.play()

    def stop_taxes(self):
        self.taxes_card.stop()


class TaxesCard(QWidget):
    def __init__(
        self,
        metrics: UiMetrics,
        event_bus: EventBus,
    ) -> None:
        super().__init__()

        self.metrics = metrics
        self.event_bus = event_bus

        self.setAttribute(
            Qt.WidgetAttribute.WA_StyledBackground,
            True,
        )
        self.setProperty("surfaceRole", SurfaceRole.CARD.value)
        self.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding,
        )

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,
        )
        self.main_layout.setSpacing(metrics.space_20)

        self._build_ui(self.metrics)

    def _build_ui(self, metrics: UiMetrics) -> None:

        self.player = QMediaPlayer(self)

        self.audio = QAudioOutput(self)
        self.audio.setVolume(0.3)
        self.player.setAudioOutput(self.audio)

        self.video = QVideoWidget(self)
        self.player.setVideoOutput(self.video)

        self.player.setSource(QUrl("qrc:/gangnam/GangnamStyleRoth.mp4"))

        self.player.setLoops(QMediaPlayer.Loops.Infinite)
        self.player.setPlaybackRate(1)

        self.video.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.video.setAspectRatioMode(Qt.AspectRatioMode.IgnoreAspectRatio)

        self.main_layout.addWidget(self.video)
        self.main_layout.setStretch(0, 1)

    def play(self):
        self.player.play()

    def stop(self):
        self.player.stop()