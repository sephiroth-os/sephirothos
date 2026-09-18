"""Settings appearance page"""

from PySide6.QtWidgets import QWidget

from events import EventBus
from ui.metrics import UiMetrics


class AppearancePage(QWidget):
    """UI customization page."""

    def __init__(self, metrics: UiMetrics, event_bus: EventBus):
        super().__init__()