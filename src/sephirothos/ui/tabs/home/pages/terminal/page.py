"""Home terminal page"""

from PySide6.QtWidgets import QWidget

from ui.metrics import UiMetrics


class TerminalPage(QWidget):
    """Easy access terminal for home usage at home."""

    def __init__(self, metrics: UiMetrics):
        super().__init__()