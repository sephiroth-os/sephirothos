"""Settings power page"""

from PySide6.QtWidgets import QWidget

from ui.metrics import UiMetrics


class PowerPage(QWidget):
    """Pope Francisco power page."""

    def __init__(self, metrics: UiMetrics):
        super().__init__()