"""Settings backup page"""

from PySide6.QtWidgets import QWidget

from ui.metrics import UiMetrics


class BackupPage(QWidget):
    """The apology page."""

    def __init__(self, metrics: UiMetrics):
        super().__init__()