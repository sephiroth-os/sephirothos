"""Home terminal page"""

from PySide6.QtWidgets import QWidget

from events import EventBus
from ui.metrics import UiMetrics


class TerminalPage(QWidget):
    """Easy access terminal for home usage at home."""

    def __init__(self, metrics: UiMetrics, event_bus: EventBus):
        super().__init__()