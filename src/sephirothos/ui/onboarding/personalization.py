from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget, QHBoxLayout
from PySide6.QtCore import Qt

from sephirothos.ui.roles import TextRole, SurfaceRole
from sephirothos.events import EventBus
from sephirothos.ui.metrics import UiMetrics


class PersonalizationPage(QWidget):
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

        self.title = QLabel("Igloo")
        self.title.setProperty("textRole", TextRole.WELCOME_TITLE.value)
        self.header_layout.addWidget(self.title)

        self.subtitle = QLabel("I have to bludgeon my ex-girlfriend to death with the balance board first.")
        self.subtitle.setProperty("textRole", TextRole.WELCOME_SUBTITLE.value)
        self.header_layout.addWidget(self.subtitle)

        self.main_layout.addLayout(self.header_layout)

        self.row_1 = QHBoxLayout()
        self.row_1.setContentsMargins(0, 0, 0, 0)
        self.row_1.setSpacing(self.metrics.space_20)

        self.row_2 = QHBoxLayout()
        self.row_2.setContentsMargins(0, 0, 0, 0)
        self.row_2.setSpacing(self.metrics.space_20)

        self.row_3 = QHBoxLayout()
        self.row_3.setContentsMargins(0, 0, 0, 0)
        self.row_3.setSpacing(self.metrics.space_20)

        self.theme_card = QWidget()
        self.theme_card.setProperty("surfaceRole", SurfaceRole.CARD.value)
        self.row_1.addWidget(self.theme_card, 2)

        self.preview_card = QWidget()
        self.preview_card.setProperty("surfaceRole", SurfaceRole.CARD.value)
        self.row_1.addWidget(self.preview_card, 3)

        self.accent_card = QWidget()
        self.accent_card.setProperty("surfaceRole", SurfaceRole.CARD.value)
        self.row_2.addWidget(self.accent_card, 3)

        self.display_card = QWidget()
        self.display_card.setProperty("surfaceRole", SurfaceRole.CARD.value)
        self.row_2.addWidget(self.display_card, 2)

        self.font_card = QWidget()
        self.font_card.setProperty("surfaceRole", SurfaceRole.CARD.value)
        self.row_3.addWidget(self.font_card, 2)

        self.extra_card = QWidget()
        self.extra_card.setProperty("surfaceRole", SurfaceRole.CARD.value)
        self.row_3.addWidget(self.extra_card, 3)

        self.main_layout.addLayout(self.row_1, 1)
        self.main_layout.addLayout(self.row_2, 1)
        self.main_layout.addLayout(self.row_3, 1)
