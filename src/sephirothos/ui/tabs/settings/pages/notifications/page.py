"""Settings notifications page"""

from PySide6.QtWidgets import QWidget

from sephirothos.events import EventBus
from sephirothos.ui.metrics import UiMetrics


class NotificationsPage(QWidget):
    """Notifications and options lmaaaaaaaa page."""

    def __init__(self, metrics: UiMetrics, event_bus: EventBus):
        super().__init__()