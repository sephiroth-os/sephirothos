"""CLI get started page"""

from PySide6.QtWidgets import QWidget

from events import EventBus
from ui.metrics import UiMetrics


class GetStartedPage(QWidget):
    """start page"""

    def __init__(self, metrics: UiMetrics, event_bus: EventBus):
        super().__init__()