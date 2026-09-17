"""Home activity monitor page"""

from PySide6.QtWidgets import QWidget

from ui.metrics import UiMetrics


class ActivityMonitorPage(QWidget):
    """Better task manager."""

    def __init__(self, metrics: UiMetrics):
        super().__init__()