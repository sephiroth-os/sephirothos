"""Home other page"""

from PySide6.QtWidgets import QWidget

from ui.metrics import UiMetrics


class OtherPage(QWidget):
    """Other features and shit."""

    def __init__(self, metrics: UiMetrics):
        super().__init__()