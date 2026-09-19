from sephirothos.events import EventBus

from sephirothos.ui.roles import SurfaceRole
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Qt

from sephirothos.ui.metrics import UiMetrics
from sephirothos.ui.tabs.home.pages.taxes.cards import TaxesCard


class Mirage(QWidget):
    def __init__(self, application, metrics: UiMetrics, event_bus: EventBus) -> None:
        super().__init__()

        self.application = application
        self.metrics = metrics
        self.event_bus = event_bus

        self.setWindowTitle("Something is Coming in 9 Months...")
        self.setWindowFlag(Qt.WindowType.Window | Qt.WindowType.FramelessWindowHint)
        self.showFullScreen()

        self.setProperty("surfaceRole", SurfaceRole.BACKGROUND.value)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,
        )

        self.video_widget = TaxesCard(self.metrics, self.event_bus)
        self.main_layout.addWidget(self.video_widget, 1)

        self.video_widget.play()