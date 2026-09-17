"""Home settings page"""

from PySide6.QtWidgets import QWidget

from ui.metrics import UiMetrics


class SettingsPage(QWidget):
    """Quick common settings page"""

    def __init__(self, metrics: UiMetrics):
        super().__init__()