"""Settings about page"""

from PySide6.QtWidgets import QWidget

from sephirothos.events import EventBus
from sephirothos.ui.metrics import UiMetrics


class AboutPage(QWidget):
    """Device and OS info page."""

    def __init__(self, metrics: UiMetrics, event_bus: EventBus):
        super().__init__()