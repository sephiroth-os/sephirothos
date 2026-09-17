"""Settings sidebar contents."""

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QButtonGroup,
    QFrame,
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
    DividerRole,
)

from .pages import PAGES, DEFAULT_SETTINGS_PAGE


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

        self.page_button_group = QButtonGroup(self)
        self.page_button_group.setExclusive(True)

        self.page_buttons: dict[str, QPushButton] = {}

        self.main_layout.addWidget(self.section_label)

        for definition in PAGES:
            button = QPushButton(definition.label)

            button.setCheckable(True)
            button.setProperty(
                "buttonVariant",
                ButtonVariant.NAVIGATION.value,
            )

            button.clicked.connect(
                lambda _checked=False, page_id=definition.id:
                    self.page_requested.emit(page_id)
            )

            self.page_buttons[definition.id] = button
            self.page_button_group.addButton(button)

            self.main_layout.addWidget(button)

            if definition.id == "power":
                self.divider = QFrame()
                self.divider.setObjectName("sidebarHeaderDivider")
                self.divider.setFrameShape(
                    QFrame.Shape.NoFrame,
                )
                self.divider.setProperty(
                    "dividerRole",
                    DividerRole.DEFAULT.value,
                )
                self.divider.setFixedHeight(
                    self.metrics.border_thin,
                )

                self.section_label2 = QLabel("System")
                self.section_label2.setProperty(
                    "textRole",
                    TextRole.SECTION_TITLE.value,
                )
                self.main_layout.addWidget(self.divider)
                self.main_layout.addSpacing(self.metrics.space_10)
                self.main_layout.addWidget(self.section_label2)

            if definition.id == "recovery":
                self.divider = QFrame()
                self.divider.setObjectName("sidebarHeaderDivider")
                self.divider.setFrameShape(
                    QFrame.Shape.NoFrame,
                )
                self.divider.setProperty(
                    "dividerRole",
                    DividerRole.DEFAULT.value,
                )
                self.divider.setFixedHeight(
                    self.metrics.border_thin,
                )

                self.section_label2 = QLabel("Advanced")
                self.section_label2.setProperty(
                    "textRole",
                    TextRole.SECTION_TITLE.value,
                )
                self.main_layout.addWidget(self.divider)
                self.main_layout.addSpacing(self.metrics.space_10)
                self.main_layout.addWidget(self.section_label2)

            if definition.id == "experimental":
                self.divider = QFrame()
                self.divider.setObjectName("sidebarHeaderDivider")
                self.divider.setFrameShape(
                    QFrame.Shape.NoFrame,
                )
                self.divider.setProperty(
                    "dividerRole",
                    DividerRole.DEFAULT.value,
                )
                self.divider.setFixedHeight(
                    self.metrics.border_thin,
                )
                self.main_layout.addWidget(self.divider)
                self.main_layout.addSpacing(self.metrics.space_10)

        self.main_layout.addStretch()

    def set_active_page(self, page_id: str) -> None:
        self.page_buttons[page_id].setChecked(True)
