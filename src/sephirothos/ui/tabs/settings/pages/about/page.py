"""Settings about page"""

from PySide6.QtWidgets import QWidget

from ui.metrics import UiMetrics


class AboutPage(QWidget):
    """Device and OS info page."""

    def __init__(self, metrics: UiMetrics):
        super().__init__()