"""Settings experimental page"""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel

from sephirothos.events import EventBus
from sephirothos.ui.metrics import UiMetrics
from sephirothos.ui.roles import TextRole


class ExperimentalPage(QWidget):
    """Experimental page."""

    def __init__(self, metrics: UiMetrics, event_bus: EventBus):
        super().__init__()
        self.metrics = metrics

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

        self.title_label = QLabel("Sephiroth's Narcotics Drawer")
        self.title_label.setProperty(
            "textRole",
            TextRole.PAGE_TITLE.value
        )

        self.subtitle_label = QLabel("I gave 50 dollars to the pole ice")
        self.subtitle_label.setProperty(
            "textRole",
            TextRole.PAGE_SUBTITLE.value
        )

        self.title_layout.addWidget(self.title_label)
        self.title_layout.addWidget(self.subtitle_label)

        self.header_layout.addLayout(self.title_layout)
        self.header_layout.addStretch()

        self.main_layout.addLayout(self.header_layout)