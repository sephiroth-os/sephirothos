"""Home file explorer page"""

from PySide6.QtWidgets import QWidget

from ui.metrics import UiMetrics


class PissExplorerPage(QWidget):
    """Better file explorer page"""

    def __init__(self, metrics: UiMetrics):
        super().__init__()