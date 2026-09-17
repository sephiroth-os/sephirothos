"""Settings updates page"""

from PySide6.QtWidgets import QWidget

from ui.metrics import UiMetrics


class UpdatesPage(QWidget):
    """Manually check for updates and shit."""

    def __init__(self, metrics: UiMetrics):
        super().__init__()