"""Settings recovery page"""

from PySide6.QtWidgets import QWidget

from events import EventBus
from ui.metrics import UiMetrics


class RecoveryPage(QWidget):
    """The page that doesn't work."""

    def __init__(self, metrics: UiMetrics, event_bus: EventBus):
        super().__init__()