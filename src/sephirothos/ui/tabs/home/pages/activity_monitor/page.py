"""Home activity monitor page"""

from PySide6.QtWidgets import QWidget

from events import EventBus
from ui.metrics import UiMetrics


class ActivityMonitorPage(QWidget):
    """Better task manager."""

    def __init__(self, metrics: UiMetrics, event_bus: EventBus):
        super().__init__()