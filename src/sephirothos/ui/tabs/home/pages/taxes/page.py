"""Home taxes page"""

from PySide6.QtWidgets import QWidget

from ui.metrics import UiMetrics


class TaxesPage(QWidget):
    """This is where you file taxes."""

    def __init__(self, metrics: UiMetrics):
        super().__init__()