"""CLI sephiroth's shed page"""

from PySide6.QtWidgets import QWidget

from events import EventBus
from ui.metrics import UiMetrics


class SephirothsShedPage(QWidget):
    """Default non-voidable page"""

    def __init__(self, metrics: UiMetrics, event_bus: EventBus):
        super().__init__()