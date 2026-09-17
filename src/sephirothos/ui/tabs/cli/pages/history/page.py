"""CLI history page"""

from PySide6.QtWidgets import QWidget

from ui.metrics import UiMetrics


class HistoryPage(QWidget):
    """See history page"""

    def __init__(self, metrics: UiMetrics):
        super().__init__()