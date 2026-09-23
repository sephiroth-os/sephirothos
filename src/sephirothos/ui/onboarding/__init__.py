"""The SephirothOS onboarding UI sequence."""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout, QStackedWidget, QPushButton, QVBoxLayout

from sephirothos.config import AppConfig
from sephirothos.events import EventBus
from sephirothos.ui.metrics import UiMetrics

from .ac import ACPage
from .car import CarPage
from .character import CharacterPage
from .done import DonePage
from .language import LanguagePage
from .laundromat import LaundromatPage
from .onedrive import OneDrivePage
from .personalization import PersonalizationPage
from .profile import ProfilePage
from .welcome import WelcomePage

from sephirothos.ui.roles import SurfaceRole, ButtonVariant

class OnboardingShell(QWidget):

    index = 0

    def __init__(self, application, config: AppConfig, metrics: UiMetrics, event_bus: EventBus):
        super().__init__()

        self.application = application
        self.config = config
        self.event_bus = event_bus
        self.metrics = metrics

        self.setWindowTitle("Welcome to SephirothOS")
        self.setWindowFlag(Qt.WindowType.Window | Qt.WindowType.FramelessWindowHint)

        self.setProperty("surfaceRole", SurfaceRole.BACKGROUND.value)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.top_bar = QWidget(self)
        self.top_bar.setProperty("surfaceRole", SurfaceRole.CHROME.value)
        self.top_bar.setFixedHeight(self.metrics.top_bar_height)
        self.main_layout.addWidget(self.top_bar)

        self.workspace = QHBoxLayout()
        self.workspace.setContentsMargins(
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,
        )
        self.workspace.setSpacing(self.metrics.space_20)
        self.main_layout.addLayout(self.workspace, 1)

        self.sidebar = QWidget(self)
        self.sidebar.setProperty("surfaceRole", SurfaceRole.PANEL.value)
        self.sidebar.setFixedWidth(self.metrics.sidebar_width)
        self.workspace.addWidget(self.sidebar)

        self.content_stack = QStackedWidget(self)
        self.content_stack.setProperty("surfaceRole", SurfaceRole.PANEL.value)
        self.workspace.addWidget(self.content_stack, 1)

        self.footer = QWidget(self)
        self.footer.setProperty("surfaceRole", SurfaceRole.CHROME.value)
        self.footer.setFixedHeight(self.metrics.top_bar_height)
        self.main_layout.addWidget(self.footer)

        self.footer_layout = QHBoxLayout()
        self.footer_layout.setContentsMargins(
            self.metrics.space_20,
            self.metrics.space_10,
            self.metrics.space_20,
            self.metrics.space_10,
        )
        self.footer.setLayout(self.footer_layout)

        self.back_button = QPushButton("Back")
        self.back_button.setProperty("buttonVariant", ButtonVariant.PRIMARY.value)
        self.back_button.clicked.connect(self.retreat)
        self.footer_layout.addWidget(self.back_button)

        self.footer_layout.addStretch()

        self.next_button = QPushButton("Back")
        self.next_button.setProperty("buttonVariant", ButtonVariant.PRIMARY.value)
        self.next_button.clicked.connect(self.turn_page)
        self.footer_layout.addWidget(self.next_button)

        self.welcome_page = WelcomePage(self, metrics=self.metrics, event_bus=self.event_bus)
        self.character_page = CharacterPage(self, metrics=self.metrics, event_bus=self.event_bus)
        self.profile_page = ProfilePage(self, metrics=self.metrics, event_bus=self.event_bus)
        self.laundromat_page = LaundromatPage(self, metrics=self.metrics, event_bus=self.event_bus)
        self.car_page = CarPage(self, metrics=self.metrics, event_bus=self.event_bus)
        self.language_page = LanguagePage(self, metrics=self.metrics, event_bus=self.event_bus)
        self.ac_page = ACPage(self, metrics=self.metrics, event_bus=self.event_bus)
        self.onedrive_page = OneDrivePage(self, metrics=self.metrics, event_bus=self.event_bus)
        self.personalization_page = PersonalizationPage(self, metrics=self.metrics, event_bus=self.event_bus)
        self.done_page = DonePage(self, metrics=self.metrics, event_bus=self.event_bus)

        self.content_stack.addWidget(self.welcome_page)
        self.content_stack.addWidget(self.character_page)
        self.content_stack.addWidget(self.profile_page)
        self.content_stack.addWidget(self.laundromat_page)
        self.content_stack.addWidget(self.car_page)
        self.content_stack.addWidget(self.language_page)
        self.content_stack.addWidget(self.ac_page)
        self.content_stack.addWidget(self.onedrive_page)
        self.content_stack.addWidget(self.personalization_page)
        self.content_stack.addWidget(self.done_page)

        self.content_stack.setCurrentIndex(0)
        self.showFullScreen()

    def turn_page(self):
        self.index += 1
        self.content_stack.setCurrentIndex(self.index)

    def retreat(self):
        self.index -= 1
        self.content_stack.setCurrentIndex(self.index)