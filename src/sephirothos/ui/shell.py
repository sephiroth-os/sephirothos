"""Root SephirothOS widget."""

from __future__ import annotations

from dataclasses import dataclass
from random import choice

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout, QWidget, QButtonGroup, QStackedWidget, QLabel

from sephirothos.config import AppConfig
from sephirothos.content.window_titles import WINDOW_TITLES
from sephirothos.events import EventBus
from sephirothos.ui.metrics import UiMetrics
from sephirothos.ui.roles import ButtonVariant, DividerRole, SurfaceRole, TextRole
from sephirothos.ui.tabs.navigation import (
    DEFAULT_TAB,
    TAB_LABELS,
    TAB_ORDER,
    TabId,
)

@dataclass(frozen=True, slots=True)
class TabPair:
    """Widgets associated with one primary tab."""

    bar: QWidget
    tab: QWidget

class Shell(QWidget):
    def __init__(self, application, config: AppConfig, event_bus: EventBus, metrics: UiMetrics) -> None:
        super().__init__()

        self.application = application
        self.config = config
        self.event_bus = event_bus
        self.metrics = metrics

        self.tab_pairs: dict[TabId, TabPair] = {}
        self.tab_buttons: dict[TabId, TabPair] = {}
        self.current_tab: TabId | None = None

        self.setWindowTitle(choice(WINDOW_TITLES))
        self.setWindowFlag(Qt.WindowType.Window | Qt.WindowType.FramelessWindowHint)
        self.showFullScreen()

        self.setProperty("surfaceRole", SurfaceRole.BACKGROUND.value)

        self._build_shell()

    def _build_shell(self) -> None:
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self._build_top_bar()
        self._build_workspace()

        self.main_layout.addWidget(self.top_bar)
        self.main_layout.addWidget(self.workspace, 1)

    def _build_top_bar(self) -> None:
        self.top_bar = QWidget()
        self.top_bar.setProperty("surfaceRole", SurfaceRole.CHROME.value)

        self.top_bar.setMinimumHeight(self.metrics.top_bar_height)

        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(
            self.metrics.space_10,
            self.metrics.space_10,
            self.metrics.space_10,
            self.metrics.space_10,
        )
        self.top_bar_layout.setSpacing(0)

        self.tab_button_group = QButtonGroup(self)
        self.tab_button_group.setExclusive(True)

    def _build_workspace(self) -> None:
        self.workspace = QWidget()
        self.workspace.setProperty("surfaceRole", SurfaceRole.BACKGROUND.value)

        self.workspace_layout = QHBoxLayout(self.workspace)
        self.workspace_layout.setContentsMargins(
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,
        )
        self.workspace_layout.setSpacing(self.metrics.space_20)

        self._build_sidebar()
        self._build_content_area()

        self.workspace_layout.addWidget(self.sidebar)
        self.workspace_layout.addWidget(self.content_area, 1)

    def _build_sidebar(self) -> None:
        self.sidebar = QWidget()
        self.sidebar.setProperty("surfaceRole", SurfaceRole.PANEL.value)

        self.sidebar.setFixedWidth(self.metrics.sidebar_width)

        self.sidebar_layout = QVBoxLayout(self.sidebar)
        self.sidebar_layout.setContentsMargins(
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,
        )
        self.sidebar_layout.setSpacing(0)

        self._build_sidebar_header()

        self.bar_stack = QStackedWidget()
        self.bar_stack.setProperty("surfaceRole", SurfaceRole.TRANSPARENT.value)

        self.sidebar_layout.addSpacing(self.metrics.space_20)

        self.sidebar_layout.addWidget(self.bar_stack)

    def _build_sidebar_header(self) -> None:
        """Construct the static sidebar header."""

        self.username_label = QLabel(self.config.username)
        self.username_label.setProperty("textRole", TextRole.USERNAME.value)

        self.subtitle_label = QLabel("Veni, veni, venias, ne me mori facias.")
        self.subtitle_label.setProperty(
            "textRole",
            TextRole.CAPTION.value
        )
        self.subtitle_label.setWordWrap(True)

        self.header_divider = QFrame()
        self.header_divider.setObjectName("sidebarHeaderDivider")
        self.header_divider.setFrameShape(
            QFrame.Shape.NoFrame,
        )
        self.header_divider.setProperty(
            "dividerRole",
            DividerRole.DEFAULT.value,
        )
        self.header_divider.setFixedHeight(
            self.metrics.border_thin,
        )

        self.sidebar_layout.addWidget(
            self.username_label,
        )
        self.sidebar_layout.addSpacing(
            self.metrics.space_10,
        )
        self.sidebar_layout.addWidget(
            self.subtitle_label,
        )
        self.sidebar_layout.addSpacing(
            self.metrics.space_20,
        )
        self.sidebar_layout.addWidget(
            self.header_divider,
        )

    def _build_content_area(self) -> None:
        self.content_area = QWidget()
        self.content_area.setProperty("surfaceRole", SurfaceRole.PANEL.value)