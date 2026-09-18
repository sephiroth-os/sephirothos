"""Apps sidebar contents."""

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QButtonGroup,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from events import EventBus
from sephirothos.ui.metrics import UiMetrics
from sephirothos.ui.roles import (
    ButtonVariant,
    SurfaceRole,
    TextRole,
)
from sephirothos.ui.tabs.apps.navigation import (
    DEFAULT_APPS_PAGE,
    APPS_PAGE_LABELS,
    AppsPageId,
)


class AppsBar(QWidget):
    """Navigation contents displayed inside the shell sidebar."""

    page_requested = Signal(object)

    def __init__(self, metrics: UiMetrics, event_bus: EventBus) -> None:
        super().__init__()

        self.metrics = metrics
        self.event_bus = event_bus

        self.setProperty(
            "surfaceRole",
            SurfaceRole.TRANSPARENT.value,
        )

        self._build_ui()
        self.set_active_page(DEFAULT_APPS_PAGE)

    def _build_ui(self) -> None:
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(
            self.metrics.space_10,
        )

        self.section_label = QLabel("Apps")
        self.section_label.setProperty(
            "textRole",
            TextRole.SECTION_TITLE.value,
        )

        self.all_button = QPushButton(APPS_PAGE_LABELS[AppsPageId.ALL])
        self.all_button.setCheckable(True)
        self.all_button.setProperty(
            "buttonVariant",
            ButtonVariant.NAVIGATION.value,
        )
        self.all_button.clicked.connect(
            lambda _checked=False: self.page_requested.emit(AppsPageId.ALL)
        )

        self.page_buttons = {
            AppsPageId.ALL: self.all_button,
        }

        self.page_button_group = QButtonGroup(self)
        self.page_button_group.setExclusive(True)
        self.page_button_group.addButton(
            self.all_button,
        )

        self.main_layout.addWidget(self.section_label)
        self.main_layout.addWidget(self.all_button)
        self.main_layout.addStretch()

    def set_active_page(
        self,
        page_id: AppsPageId,
    ) -> None:
        self.page_buttons[page_id].setChecked(True)
