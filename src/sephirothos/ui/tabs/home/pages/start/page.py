"""Home start page"""

from PySide6.QtWidgets import QWidget

from ui.metrics import UiMetrics


class StartPage(QWidget):
    """Better start menu"""

    def __init__(self, metrics: UiMetrics):
        super().__init__()