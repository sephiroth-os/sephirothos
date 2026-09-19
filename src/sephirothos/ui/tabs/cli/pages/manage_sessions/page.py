"""CLI manage sessions page"""

from PySide6.QtWidgets import QWidget

from sephirothos.ui.metrics import UiMetrics
from sephirothos.events import EventBus


class ManageSessionsPage(QWidget):
    """Epic session management page"""

    def __init__(self, metrics: UiMetrics, event_bus: EventBus):
        super().__init__()