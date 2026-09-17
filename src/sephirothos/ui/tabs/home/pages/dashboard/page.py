"""Home dashboard page"""

from PySide6.QtWidgets import QWidget

from ui.metrics import UiMetrics


class DashboardPage(QWidget):
    """Primary home dashboard."""

    def __init__(self, metrics: UiMetrics):
        super().__init__()