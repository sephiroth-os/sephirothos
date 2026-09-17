"""Apps tab."""

from PySide6.QtWidgets import (
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from sephirothos.ui.metrics import UiMetrics
from sephirothos.ui.roles import SurfaceRole
from sephirothos.ui.tabs.apps.navigation import (
    DEFAULT_APPS_PAGE,
    AppsPageId,
)
from sephirothos.ui.tabs.apps.pages import (
    all_page
)


class AppsTab(QWidget):
    """Owns the Apps tab's pages and page selection."""

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
        self.set_active_page(DEFAULT_APPS_PAGE)

    def _build_ui(self) -> None:
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.page_stack = QStackedWidget()
        self.page_stack.setProperty(
            "surfaceRole",
            SurfaceRole.TRANSPARENT.value,
        )

        self.pages: dict[AppsPageId, QWidget] = {
            AppsPageId.ALL: all_page(
                metrics=self.metrics,
            ),
        }

        for page in self.pages.values():
            self.page_stack.addWidget(page)

    def set_active_page(self, page_id: AppsPageId) -> None:
        self.page_stack.setCurrentWidget(self.pages[page_id])