"""Reusable widgets containers."""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QSizePolicy, QVBoxLayout, QWidget, QLabel

from sephirothos.events import EventBus
from sephirothos.ui.metrics import UiMetrics
from sephirothos.ui.roles import SurfaceRole, TextRole


class Card(QWidget):
    """Base container providing standardized widgets presentation."""

    def __init__(
        self,
        metrics: UiMetrics,
        event_bus: EventBus,
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)

        self.metrics = metrics
        self.event_bus = event_bus

        self.setAttribute(
            Qt.WidgetAttribute.WA_StyledBackground,
            True,
        )
        self.setProperty("surfaceRole", SurfaceRole.CARD.value)
        self.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding,
        )

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,
        )
        self.main_layout.setSpacing(metrics.space_20)

        self.title = QLabel("Title Here")
        self.title.setProperty("textRole", TextRole.CARD_TITLE.value)
        self.main_layout.addWidget(self.title, alignment=Qt.AlignmentFlag.AlignTop)