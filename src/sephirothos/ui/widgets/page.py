"""Default Page object"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QSizePolicy, QVBoxLayout, QWidget, QHBoxLayout

from sephirothos.events import EventBus
from sephirothos.ui.roles import SurfaceRole, TextRole
from sephirothos.ui.metrics import UiMetrics


class Page(QWidget):
    def __init__(
        self,
        metrics: UiMetrics,
        event_bus: EventBus,
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)

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

        self.header_layout = QHBoxLayout()
        self.header_layout.setContentsMargins(0, 0, 0, 0)
        self.header_layout.setSpacing(self.metrics.space_20)

        self.title_layout = QVBoxLayout()
        self.title_layout.setContentsMargins(0, 0, 0, 0)
        self.title_layout.setSpacing(self.metrics.space_10)

        self.title_label = QLabel("Title Here")
        self.title_label.setProperty(
            "textRole",
            TextRole.PAGE_TITLE.value
        )

        self.subtitle_label = QLabel("Subtitle Here")
        self.subtitle_label.setProperty(
            "textRole",
            TextRole.PAGE_SUBTITLE.value
        )

        self.title_layout.addWidget(self.title_label)
        self.title_layout.addWidget(self.subtitle_label)

        self.header_layout.addLayout(self.title_layout)
        self.header_layout.addStretch()

        self.main_layout.addLayout(self.header_layout)