"""Home other page"""

from PySide6.QtWidgets import QWidget

from events import EventBus
from ui.metrics import UiMetrics


class OtherPage(QWidget):
    """Other features and shit."""

    def __init__(self, metrics: UiMetrics, event_bus: EventBus):
        super().__init__()