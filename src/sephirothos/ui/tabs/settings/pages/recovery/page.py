"""Settings recovery page"""

from PySide6.QtWidgets import QWidget

from ui.metrics import UiMetrics


class RecoveryPage(QWidget):
    """The page that doesn't work."""

    def __init__(self, metrics: UiMetrics):
        super().__init__()