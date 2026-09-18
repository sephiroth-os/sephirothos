"""Settings general page"""

from PySide6.QtWidgets import QWidget

from events import EventBus
from ui.metrics import UiMetrics


class GeneralPage(QWidget):
    """Primary settings page."""

    def __init__(self, metrics: UiMetrics, event_bus: EventBus):
        super().__init__()