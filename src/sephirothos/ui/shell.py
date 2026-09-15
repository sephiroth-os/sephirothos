from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget


class Shell(QWidget):
    def __init__(self, application):
        super().__init__()

        self.application = application

        self.setWindowFlag(Qt.WindowType.Window | Qt.WindowType.FramelessWindowHint)
        self.showFullScreen()

        self.setStyleSheet("background-color: #1c1c1c")

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
        self.top_bar.setObjectName("topBar")
        self.top_bar.setStyleSheet("background-color: #121212; border-radius: 0px")

        self.top_bar.setMinimumHeight(60)

        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(0, 0, 0, 0)
        self.top_bar_layout.setSpacing(0)

    def _build_workspace(self) -> None:
        self.workspace = QWidget()
        self.workspace.setObjectName("workspace")
        self.workspace.setStyleSheet("background-color: #1c1c1c")

        self.workspace_layout = QHBoxLayout(self.workspace)
        self.workspace_layout.setContentsMargins(20, 20, 20, 20)
        self.workspace_layout.setSpacing(20)

        self._build_sidebar()
        self._build_content_area()

        self.workspace_layout.addWidget(self.sidebar)
        self.workspace_layout.addWidget(self.content_area, 1)

    def _build_sidebar(self) -> None:
        self.sidebar = QWidget()
        self.sidebar.setObjectName("sidebar")
        self.sidebar.setStyleSheet("background-color: #121212")

        self.sidebar.setFixedWidth(264)

    def _build_content_area(self) -> None:
        self.content_area = QWidget()
        self.content_area.setObjectName("content_area")
        self.content_area.setStyleSheet("background-color: #121212")
