"""CLI sidebar contents."""

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QButtonGroup,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from sephirothos.ui.metrics import UiMetrics
from sephirothos.ui.roles import (
    ButtonVariant,
    SurfaceRole,
    TextRole,
)
from sephirothos.ui.tabs.cli.navigation import (
    DEFAULT_CLI_PAGE,
    CLI_PAGE_LABELS,
    CLIPageId,
)


class CLIBar(QWidget):
    """Navigation contents displayed inside the shell sidebar."""

    page_requested = Signal(object)

    def __init__(self, metrics: UiMetrics) -> None:
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
        self.main_layout.setSpacing(
            self.metrics.space_10,
        )

        self.section_label = QLabel("Start")
        self.section_label.setProperty(
            "textRole",
            TextRole.SECTION_TITLE.value,
        )

        self.get_started_button = QPushButton(CLI_PAGE_LABELS[CLIPageId.GET_STARTED])
        self.get_started_button.setCheckable(True)
        self.get_started_button.setProperty(
            "buttonVariant",
            ButtonVariant.NAVIGATION.value,
        )
        self.get_started_button.clicked.connect(
            lambda _checked=False: self.page_requested.emit(CLIPageId.GET_STARTED)
        )

        self.page_buttons = {
            CLIPageId.GET_STARTED: self.get_started_button,
        }

        self.page_button_group = QButtonGroup(self)
        self.page_button_group.setExclusive(True)
        self.page_button_group.addButton(
            self.get_started_button,
        )

        self.main_layout.addWidget(self.section_label)
        self.main_layout.addWidget(self.get_started_button)
        self.main_layout.addStretch()

    def set_active_page(
        self,
        page_id: CLIPageId,
    ) -> None:
        self.page_buttons[page_id].setChecked(True)
