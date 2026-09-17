"""CLI sephiroth's shed page"""

from PySide6.QtWidgets import QWidget

from ui.metrics import UiMetrics


class SephirothsShedPage(QWidget):
    """Default non-voidable page"""

    def __init__(self, metrics: UiMetrics):
        super().__init__()