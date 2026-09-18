"""Home start page"""

from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout

from events import EventBus
from ui.metrics import UiMetrics

from sephirothos.ui.roles import (
    SurfaceRole,
    TextRole
)

from .cards import StartCard


class StartPage(QWidget):
    """Better start menu"""

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

        self.header_layout = QHBoxLayout()
        self.header_layout.setContentsMargins(0, 0, 0, 0)
        self.header_layout.setSpacing(self.metrics.space_20)

        self.title_layout = QVBoxLayout()
        self.title_layout.setContentsMargins(0, 0, 0, 0)
        self.title_layout.setSpacing(self.metrics.space_10)

        self.title_label = QLabel("Sephiroth's Nuclear Waste Dump")
        self.title_label.setProperty(
            "textRole",
            TextRole.PAGE_TITLE.value
        )

        self.subtitle_label = QLabel("Hmmm... uhhhh... yup.")
        self.subtitle_label.setProperty(
            "textRole",
            TextRole.PAGE_SUBTITLE.value
        )

        self.title_layout.addWidget(self.title_label)
        self.title_layout.addWidget(self.subtitle_label)

        self.header_layout.addLayout(self.title_layout)
        self.header_layout.addStretch()

        self.main_layout.addLayout(self.header_layout)

        self.start_layout = QVBoxLayout()
        self.start_layout.setContentsMargins(0, 0, 0, 0)
        self.start_layout.setSpacing(self.metrics.space_20)

        self.start_card = StartCard(self.metrics, self.event_bus)
        self.start_layout.addWidget(self.start_card, 1)

        self.main_layout.addLayout(self.start_layout, 1)