"""Settings storage page"""

from PySide6.QtWidgets import QWidget

from ui.metrics import UiMetrics


class StoragePage(QWidget):
    """The storage page."""

    def __init__(self, metrics: UiMetrics):
        super().__init__()