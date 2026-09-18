"""Real taxes"""

import sephirothos.assets.videos.taxes_rc

from PySide6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy

from events import EventBus
from ui.metrics import UiMetrics
from ui.widgets.card import Card

from PySide6.QtCore import QUrl, Qt
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget

class TaxesCard(Card):
    def __init__(
        self,
        metrics: UiMetrics,
        event_bus: EventBus,
        parent: QWidget | None = None
    ) -> None:
        super().__init__(metrics, event_bus, parent)

        self._metrics = metrics
        self.event_bus = event_bus

        self._build_ui(self._metrics)

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