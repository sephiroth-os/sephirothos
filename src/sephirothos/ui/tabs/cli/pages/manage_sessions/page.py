"""CLI manage sessions page"""

from PySide6.QtWidgets import QWidget

from ui.metrics import UiMetrics


class ManageSessionsPage(QWidget):
    """Epic session management page"""

    def __init__(self, metrics: UiMetrics):
        super().__init__()