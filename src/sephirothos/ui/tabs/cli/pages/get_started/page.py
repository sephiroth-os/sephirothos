"""CLI get started page"""

from PySide6.QtWidgets import QWidget

from ui.metrics import UiMetrics


class GetStartedPage(QWidget):
    """Display all apps."""

    def __init__(self, metrics: UiMetrics):
        super().__init__()