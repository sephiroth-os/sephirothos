from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget, QHBoxLayout
from PySide6.QtCore import Qt

from sephirothos.ui.roles import TextRole, SurfaceRole
from sephirothos.events import EventBus
from sephirothos.ui.metrics import UiMetrics

class OneDrivePage(QWidget):
    def __init__(self, application, metrics: UiMetrics, event_bus: EventBus):
        super().__init__()
        self.application = application
        self.metrics = metrics
        self.event_bus = event_bus

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setProperty("surfaceRole", SurfaceRole.PANEL.value)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,

        )
        self.main_layout.setSpacing(self.metrics.space_20)

        self.header_layout = QVBoxLayout()
        self.header_layout.setContentsMargins(0, 0, 0, 0)
        self.header_layout.setSpacing(0)

        self.title = QLabel("Sephiroth's Money (it's for sale)")
        self.title.setProperty("textRole", TextRole.WELCOME_TITLE.value)
        self.header_layout.addWidget(self.title)

        self.subtitle = QLabel("No bitch, I'm not.")
        self.subtitle.setProperty("textRole", TextRole.WELCOME_SUBTITLE.value)
        self.header_layout.addWidget(self.subtitle)

        self.main_layout.addLayout(self.header_layout)

        self.label_card = QWidget()
        self.label_card.setProperty("surfaceRole", SurfaceRole.CARD.value)
        self.main_layout.addWidget(self.label_card, 1)

        self.alt_layout = QHBoxLayout()
        self.alt_layout.setContentsMargins(0, 0, 0, 0)
        self.alt_layout.setSpacing(self.metrics.space_20)

        self.connect_card = QWidget()
        self.connect_card.setProperty("surfaceRole", SurfaceRole.CARD.value)
        self.alt_layout.addWidget(self.connect_card, 1)

        self.practice_card = QWidget()
        self.practice_card.setProperty("surfaceRole", SurfaceRole.CARD.value)
        self.alt_layout.addWidget(self.practice_card, 1)

        self.main_layout.addLayout(self.alt_layout, 3)