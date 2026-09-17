"""Settings appearance page"""

from PySide6.QtWidgets import QWidget

from ui.metrics import UiMetrics


class AppearancePage(QWidget):
    """UI customization page."""

    def __init__(self, metrics: UiMetrics):
        super().__init__()