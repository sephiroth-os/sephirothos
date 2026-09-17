"""Settings experimental page"""

from PySide6.QtWidgets import QWidget

from ui.metrics import UiMetrics


class ExperimentalPage(QWidget):
    """Experimental page."""

    def __init__(self, metrics: UiMetrics):
        super().__init__()