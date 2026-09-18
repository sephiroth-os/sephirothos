"""CLI tab."""

from PySide6.QtWidgets import (
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from events import EventBus
from sephirothos.ui.metrics import UiMetrics
from sephirothos.ui.roles import SurfaceRole

from .pages import PAGES, DEFAULT_CLI_PAGE


class CLITab(QWidget):
    """Owns the CLI tab's pages and page selection."""

    def __init__(
        self,
        metrics: UiMetrics,
        event_bus: EventBus,
    ) -> None:
        super().__init__()

        self.metrics = metrics
        self.event_bus = event_bus

        self.setProperty(
            "surfaceRole",
            SurfaceRole.TRANSPARENT.value,
        )

        self._build_ui()
        self.set_active_page(DEFAULT_CLI_PAGE)

    def _build_ui(self) -> None:
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.page_stack = QStackedWidget()
        self.page_stack.setProperty(
            "surfaceRole",
            SurfaceRole.TRANSPARENT.value,
        )

        self.pages: dict[str, QWidget] = {}

        for definition in PAGES:
            page = definition.page(
                metrics=self.metrics,
                event_bus=self.event_bus,
            )

            self.pages[definition.id] = page
            self.page_stack.addWidget(page)

        self.main_layout.addWidget(self.page_stack)

    def set_active_page(self, page_id: str) -> None:
        self.page_stack.setCurrentWidget(
            self.pages[page_id],
        )