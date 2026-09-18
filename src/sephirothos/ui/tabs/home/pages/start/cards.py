"""Start Button"""

import sephirothos.assets.icons.icons_rc

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QPushButton, QWidget, QSizePolicy

from sephirothos.ui.roles import ButtonVariant
from sephirothos.ui.widgets.card import Card

from sephirothos.events import EventBus
from sephirothos.ui.metrics import UiMetrics

class StartCard(Card):
    """Better start menu"""

    def __init__(
        self,
        metrics: UiMetrics,
        event_bus: EventBus,
        parent: QWidget | None = None,

    ) -> None:
        super().__init__(metrics, event_bus, parent)

        self.metrics = metrics
        self.event_bus = event_bus


        self._build_ui()

    def _build_ui(self):
        self.start_button = QPushButton()
        self.start_button.setProperty("buttonVariant", ButtonVariant.LINK.value)

        icon_path = ":/icons/start.svg"
        self.start_button.setIcon(QIcon(icon_path))
        self.start_button.setIconSize(QSize(self.metrics.font_hero_title * 3, self.metrics.font_hero_title * 3))

        self.start_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.main_layout.addWidget(self.start_button, 1)