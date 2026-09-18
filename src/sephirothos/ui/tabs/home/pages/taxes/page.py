"""Home taxes page"""
import datetime
from random import choice

from PySide6.QtWidgets import QWidget, QVBoxLayout

from events import EventBus
from ui.metrics import UiMetrics
from ui.roles import SurfaceRole

from .cards import TaxesCard

class TaxesPage(QWidget):
    """Primary home dashboard."""

    def __init__(self, metrics: UiMetrics, event_bus: EventBus):
        super().__init__()

        self.metrics = metrics
        self.event_bus = event_bus

        self.setProperty(
            "surfaceRole",
            SurfaceRole.TRANSPARENT.value
        )

        self._build_ui()

    def _build_ui(self):
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,
        )
        self.main_layout.setSpacing(self.metrics.space_20)

        self.taxes_card = TaxesCard(self.metrics, self.event_bus)

        self.main_layout.addWidget(self.taxes_card, 1)

    def start_taxes(self):
        self.taxes_card.play()

    def stop_taxes(self):
        self.taxes_card.stop()