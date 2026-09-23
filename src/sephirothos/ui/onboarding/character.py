from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget, QHBoxLayout
from PySide6.QtCore import Qt

from sephirothos.ui.roles import TextRole, SurfaceRole
from sephirothos.events import EventBus
from sephirothos.ui.metrics import UiMetrics

class CharacterPage(QWidget):
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

        self.title = QLabel("Sephiroth's Stylish, Fashionable, Sophisticated, Fresh, Sharp Wardrobe")
        self.title.setWordWrap(True)
        self.title.setProperty("textRole", TextRole.WELCOME_TITLE.value)
        self.header_layout.addWidget(self.title)

        self.subtitle = QLabel("The comments got to me, so I bought Wii Fit.")
        self.subtitle.setProperty("textRole", TextRole.WELCOME_SUBTITLE.value)
        self.header_layout.addWidget(self.subtitle)

        self.main_layout.addLayout(self.header_layout)

        self.second_layout = QHBoxLayout()
        self.second_layout.setContentsMargins(0, 0, 0, 0)
        self.second_layout.setSpacing(self.metrics.space_20)
        self.main_layout.addLayout(self.second_layout, 1)

        self.editor_layout = QVBoxLayout()
        self.editor_layout.setContentsMargins(0, 0, 0, 0)
        self.editor_layout.setSpacing(self.metrics.space_20)
        self.second_layout.addLayout(self.editor_layout, 3)

        self.preview_widget = QWidget()
        self.preview_widget.setProperty("surfaceRole", SurfaceRole.CARD.value)
        self.second_layout.addWidget(self.preview_widget, 1)