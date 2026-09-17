"""Settings sidebar contents."""

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
from sephirothos.ui.tabs.settings.navigation import (
    DEFAULT_SETTINGS_PAGE,
    SETTINGS_PAGE_LABELS,
    SettingsPageId,
)


class SettingsBar(QWidget):
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
        self.set_active_page(DEFAULT_SETTINGS_PAGE)

    def _build_ui(self) -> None:
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(
            self.metrics.space_10,
        )

        self.section_label = QLabel("Settings")
        self.section_label.setProperty(
            "textRole",
            TextRole.SECTION_TITLE.value,
        )

        self.general_button = QPushButton(SETTINGS_PAGE_LABELS[SettingsPageId.GENERAL])
        self.general_button.setCheckable(True)
        self.general_button.setProperty(
            "buttonVariant",
            ButtonVariant.NAVIGATION.value,
        )
        self.general_button.clicked.connect(
            lambda _checked=False: self.page_requested.emit(SettingsPageId.GENERAL)
        )

        self.page_buttons = {
            SettingsPageId.GENERAL: self.general_button,
        }

        self.page_button_group = QButtonGroup(self)
        self.page_button_group.setExclusive(True)
        self.page_button_group.addButton(
            self.general_button,
        )

        self.main_layout.addWidget(self.section_label)
        self.main_layout.addWidget(self.general_button)
        self.main_layout.addStretch()

    def set_active_page(
        self,
        page_id: SettingsPageId,
    ) -> None:
        self.page_buttons[page_id].setChecked(True)
