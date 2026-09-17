"""CLI tab."""

from PySide6.QtWidgets import (
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from sephirothos.ui.metrics import UiMetrics
from sephirothos.ui.roles import SurfaceRole
from sephirothos.ui.tabs.cli.navigation import (
    DEFAULT_CLI_PAGE,
    CLIPageId,
)
from sephirothos.ui.tabs.cli.pages import (
    get_started_page
)


class CLITab(QWidget):
    """Owns the CLI tab's pages and page selection."""

    def __init__(
        self,
         metrics: UiMetrics,
    ) -> None:
        super().__init__()

        self.metrics = metrics

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

        self.pages: dict[CLIPageId, QWidget] = {
            CLIPageId.GET_STARTED: get_started_page(
                metrics=self.metrics,
            ),
        }

        for page in self.pages.values():
            self.page_stack.addWidget(page)

    def set_active_page(self, page_id: CLIPageId) -> None:
        self.page_stack.setCurrentWidget(self.pages[page_id])