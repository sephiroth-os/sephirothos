"""Settings sound page"""

from PySide6.QtWidgets import QWidget

from ui.metrics import UiMetrics


class SoundPage(QWidget):
    """Primary sound page."""

    def __init__(self, metrics: UiMetrics):
        super().__init__()