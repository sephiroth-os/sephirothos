"""Settings general page"""

from PySide6.QtWidgets import QWidget

from ui.metrics import UiMetrics


class GeneralPage(QWidget):
    """Primary settings page."""

    def __init__(self, metrics: UiMetrics):
        super().__init__()