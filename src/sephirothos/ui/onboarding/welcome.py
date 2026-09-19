"""The SephirothOS onboarding UI sequence."""
from PySide6.QtWebEngineWidgets import QWebEngineView

import sephirothos.assets.animations.animations_rc

from sephirothos.content.languages import LANGUAGES

from PySide6.QtCore import Qt
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QButtonGroup, QStackedWidget, QLabel, QPushButton, \
    QLineEdit, QToolButton, QFrame, QSizePolicy, QTextEdit, QListWidget, QListWidgetItem

from sephirothos.config import AppConfig
from sephirothos.events import EventBus
from sephirothos.ui.metrics import UiMetrics
from sephirothos.ui.roles import SurfaceRole, TextRole, ButtonVariant, InputRole, DividerRole
from sephirothos.ui.widgets.card import Card

langs = LANGUAGES

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

        self.content_stack.addWidget(self.welcome_page)
        self.content_stack.addWidget(self.character_page)
        self.content_stack.addWidget(self.profile_page)
        self.content_stack.addWidget(self.laundromat_page)
        self.content_stack.addWidget(self.car_page)
        self.content_stack.addWidget(self.language_page)
        self.content_stack.addWidget(self.ac_page)
        self.content_stack.addWidget(self.onedrive_page)
        self.content_stack.addWidget(self.personalization_page)

        self.content_stack.setCurrentIndex(0)
        self.showFullScreen()

    def turn_page(self):
        self.index += 1
        self.content_stack.setCurrentIndex(self.index)

    def retreat(self):
        self.index -= 1
        self.content_stack.setCurrentIndex(self.index)


class WelcomePage(QWidget):
    def __init__(self, application, metrics: UiMetrics, event_bus: EventBus):
        super().__init__()
        self.application = application
        self.metrics = metrics
        self.event_bus = event_bus

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setProperty("surfaceRole", SurfaceRole.PANEL.value)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,

        )
        self.main_layout.setSpacing(self.metrics.space_20)

        self.header_layout = QVBoxLayout()
        self.header_layout.setContentsMargins(0, 0, 0, 0)
        self.header_layout.setSpacing(0)

        self.main_layout.addStretch()

        self.title = QLabel("Welcome to SephirothOS")
        self.title.setProperty("textRole", TextRole.WELCOME_TITLE.value)
        self.header_layout.addWidget(self.title)

        self.subtitle = QLabel("I got called a fatass on Instragram Live.")
        self.subtitle.setProperty("textRole", TextRole.WELCOME_SUBTITLE.value)
        self.header_layout.addWidget(self.subtitle)

        self.main_layout.addLayout(self.header_layout)

        self.main_layout.addStretch()


class CharacterPage(QWidget):
    def __init__(self, application, metrics: UiMetrics, event_bus: EventBus):
        super().__init__()
        self.application = application
        self.metrics = metrics
        self.event_bus = event_bus

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setProperty("surfaceRole", SurfaceRole.PANEL.value)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,

        )
        self.main_layout.setSpacing(self.metrics.space_20)

        self.header_layout = QVBoxLayout()
        self.header_layout.setContentsMargins(0, 0, 0, 0)
        self.header_layout.setSpacing(0)

        self.title = QLabel("Sephiroth's Stylish, Fashionable, Sophisticated, Fresh, Sharp Wardrobe")
        self.title.setWordWrap(True)
        self.title.setProperty("textRole", TextRole.WELCOME_TITLE.value)
        self.header_layout.addWidget(self.title)

        self.subtitle = QLabel("The comments got to me, so I bought Wii Fit.")
        self.subtitle.setProperty("textRole", TextRole.WELCOME_SUBTITLE.value)
        self.header_layout.addWidget(self.subtitle)

        self.main_layout.addLayout(self.header_layout)

        self.second_layout = QHBoxLayout()
        self.second_layout.setContentsMargins(0, 0, 0, 0)
        self.second_layout.setSpacing(self.metrics.space_20)
        self.main_layout.addLayout(self.second_layout, 1)

        self.editor_layout = QVBoxLayout()
        self.editor_layout.setContentsMargins(0, 0, 0, 0)
        self.editor_layout.setSpacing(self.metrics.space_20)
        self.second_layout.addLayout(self.editor_layout, 3)

        self.preview_widget = QWidget()
        self.preview_widget.setProperty("surfaceRole", SurfaceRole.CARD.value)
        self.second_layout.addWidget(self.preview_widget, 1)


class ProfilePage(QWidget):
    def __init__(self, application, metrics: UiMetrics, event_bus: EventBus):
        super().__init__()
        self.application = application
        self.metrics = metrics
        self.event_bus = event_bus

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setProperty("surfaceRole", SurfaceRole.PANEL.value)

        self.true_main_layout = QHBoxLayout(self)
        self.true_main_layout.setContentsMargins(
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,
        )
        self.true_main_layout.setSpacing(self.metrics.space_20)

        self.header_layout = QVBoxLayout()
        self.header_layout.setContentsMargins(0, 0, 0, 0)
        self.header_layout.setSpacing(0)

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(self.metrics.space_20)

        self.title = QLabel("Sephiroth's Grindr Profile")
        self.title.setProperty("textRole", TextRole.WELCOME_TITLE.value)
        self.header_layout.addWidget(self.title)

        self.subtitle = QLabel("I like men.")
        self.subtitle.setProperty("textRole", TextRole.WELCOME_SUBTITLE.value)
        self.header_layout.addWidget(self.subtitle)

        self.main_layout.addLayout(self.header_layout)

        self.true_main_layout.addLayout(self.main_layout, 1)

        self.profile_card = QWidget()
        self.profile_card.setProperty("surfaceRole", SurfaceRole.CARD.value)
        self.profile_card.setFixedWidth(self.metrics.sidebar_width)

        self.second_layout = QHBoxLayout()
        self.second_layout.setContentsMargins(0, 0, 0, 0)
        self.second_layout.setSpacing(self.metrics.space_20)
        self.main_layout.addLayout(self.second_layout, 1)

        self.info_layout = QVBoxLayout()
        self.info_layout.setContentsMargins(0, 0, 0, 0)
        self.info_layout.setSpacing(self.metrics.space_20)

        self.user_info_card = UserInfoCard(self.metrics, self.event_bus)
        self.info_layout.addWidget(self.user_info_card, 1)

        self.description_card = DescriptionCard(self.metrics, self.event_bus)
        self.info_layout.addWidget(self.description_card, 1)

        self.last_layout = QHBoxLayout()
        self.last_layout.setContentsMargins(0, 0, 0, 0)
        self.last_layout.setSpacing(self.metrics.space_20)
        self.info_layout.addLayout(self.last_layout, 2)

        self.extra_card = ExtraCard(self.metrics, self.event_bus)
        self.last_layout.addWidget(self.extra_card, 1)

        self.collage_card = CollageCard(self.metrics, self.event_bus)
        self.last_layout.addWidget(self.collage_card, 1)

        self.second_layout.addLayout(self.info_layout, 1)
        self.second_layout.addWidget(self.profile_card)


class LaundromatPage(QWidget):
    def __init__(self, application, metrics: UiMetrics, event_bus: EventBus):
        super().__init__()
        self.application = application
        self.metrics = metrics
        self.event_bus = event_bus

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setProperty("surfaceRole", SurfaceRole.PANEL.value)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,

        )
        self.main_layout.setSpacing(self.metrics.space_20)

        self.header_layout = QVBoxLayout()
        self.header_layout.setContentsMargins(0, 0, 0, 0)
        self.header_layout.setSpacing(0)

        self.title = QLabel("Sephiroth's Dishwasher")
        self.title.setProperty("textRole", TextRole.WELCOME_TITLE.value)
        self.header_layout.addWidget(self.title)

        self.subtitle = QLabel("Last time I weighed myself I was 85.")
        self.subtitle.setProperty("textRole", TextRole.WELCOME_SUBTITLE.value)
        self.header_layout.addWidget(self.subtitle)

        self.main_layout.addLayout(self.header_layout)


class CarPage(QWidget):
    def __init__(self, application, metrics: UiMetrics, event_bus: EventBus):
        super().__init__()
        self.application = application
        self.metrics = metrics
        self.event_bus = event_bus

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setProperty("surfaceRole", SurfaceRole.PANEL.value)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,

        )
        self.main_layout.setSpacing(self.metrics.space_20)

        self.header_layout = QVBoxLayout()
        self.header_layout.setContentsMargins(0, 0, 0, 0)
        self.header_layout.setSpacing(0)

        self.title = QLabel("Insert Title Here")
        self.title.setProperty("textRole", TextRole.WELCOME_TITLE.value)
        self.header_layout.addWidget(self.title)

        self.subtitle = QLabel("I fell off the balance board and cracked my skull open.")
        self.subtitle.setProperty("textRole", TextRole.WELCOME_SUBTITLE.value)
        self.header_layout.addWidget(self.subtitle)

        self.main_layout.addLayout(self.header_layout)


class LanguagePage(QWidget):
    def __init__(self, application, metrics: UiMetrics, event_bus: EventBus):
        super().__init__()
        self.application = application
        self.metrics = metrics
        self.event_bus = event_bus

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setProperty("surfaceRole", SurfaceRole.PANEL.value)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,

        )
        self.main_layout.setSpacing(self.metrics.space_20)

        self.header_layout = QVBoxLayout()
        self.header_layout.setContentsMargins(0, 0, 0, 0)
        self.header_layout.setSpacing(0)

        self.title = QLabel("בורר השפה של Sephiroth")
        self.title.setProperty("textRole", TextRole.WELCOME_TITLE.value)
        self.header_layout.addWidget(self.title)

        self.subtitle = QLabel("我現在在玩 Wii Fit。")
        self.subtitle.setProperty("textRole", TextRole.WELCOME_SUBTITLE.value)
        self.header_layout.addWidget(self.subtitle)

        self.main_layout.addLayout(self.header_layout)

        self.alt_layout = QHBoxLayout()
        self.alt_layout.setContentsMargins(0, 0, 0, 0)
        self.alt_layout.setSpacing(self.metrics.space_20)
        self.main_layout.addLayout(self.alt_layout, 1)

        self.language_dir_card = LanguageDirectoryCard(self.metrics, self.event_bus)
        self.alt_layout.addWidget(self.language_dir_card, 1)

        self.location_card = QWidget()
        self.location_card.setProperty("surfaceRole", SurfaceRole.CARD.value)

        self.this_layout = QVBoxLayout()
        self.this_layout.setContentsMargins(
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,
        )
        self.this_layout.setSpacing(0)
        self.location_card.setLayout(self.this_layout)

        self.map = QWebEngineView()
        self.map.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding,
        )

        self.map.setHtml("""
        <!DOCTYPE html>
        <html>
        <head>
            <link
                rel="stylesheet"
                href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
            />
            <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    
            <style>
                html, body, #map {
                    width: 100%;
                    height: 100%;
                    margin: 0;
                }
            </style>
        </head>
    
        <body>
            <div id="map"></div>
    
            <script>
                const map = L.map("map").setView([51.505, -0.09], 13);
    
                L.tileLayer(
                    "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
                    {
                        maxZoom: 19,
                        attribution: "&copy; OpenStreetMap contributors"
                    }
                ).addTo(map);
            </script>
        </body>
        </html>
        """)

        self.this_layout.addWidget(self.map)

        self.alt_layout.addWidget(self.location_card, 1)


class ACPage(QWidget):
    def __init__(self, application, metrics: UiMetrics, event_bus: EventBus):
        super().__init__()
        self.application = application
        self.metrics = metrics
        self.event_bus = event_bus

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setProperty("surfaceRole", SurfaceRole.PANEL.value)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,

        )
        self.main_layout.setSpacing(self.metrics.space_20)

        self.header_layout = QVBoxLayout()
        self.header_layout.setContentsMargins(0, 0, 0, 0)
        self.header_layout.setSpacing(0)

        self.title = QLabel("Sephiroth's Left Shoe")
        self.title.setProperty("textRole", TextRole.WELCOME_TITLE.value)
        self.header_layout.addWidget(self.title)

        self.subtitle = QLabel('This bitch said, "Are you ok?"')
        self.subtitle.setProperty("textRole", TextRole.WELCOME_SUBTITLE.value)
        self.header_layout.addWidget(self.subtitle)

        self.main_layout.addLayout(self.header_layout)


class OneDrivePage(QWidget):
    def __init__(self, application, metrics: UiMetrics, event_bus: EventBus):
        super().__init__()
        self.application = application
        self.metrics = metrics
        self.event_bus = event_bus

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setProperty("surfaceRole", SurfaceRole.PANEL.value)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,

        )
        self.main_layout.setSpacing(self.metrics.space_20)

        self.header_layout = QVBoxLayout()
        self.header_layout.setContentsMargins(0, 0, 0, 0)
        self.header_layout.setSpacing(0)

        self.title = QLabel("Sephiroth's Money (it's for sale)")
        self.title.setProperty("textRole", TextRole.WELCOME_TITLE.value)
        self.header_layout.addWidget(self.title)

        self.subtitle = QLabel("No bitch, I'm not.")
        self.subtitle.setProperty("textRole", TextRole.WELCOME_SUBTITLE.value)
        self.header_layout.addWidget(self.subtitle)

        self.main_layout.addLayout(self.header_layout)

        self.label_card = QWidget()
        self.label_card.setProperty("surfaceRole", SurfaceRole.CARD.value)
        self.main_layout.addWidget(self.label_card, 1)

        self.alt_layout = QHBoxLayout()
        self.alt_layout.setContentsMargins(0, 0, 0, 0)
        self.alt_layout.setSpacing(self.metrics.space_20)

        self.connect_card = QWidget()
        self.connect_card.setProperty("surfaceRole", SurfaceRole.CARD.value)
        self.alt_layout.addWidget(self.connect_card, 1)

        self.practice_card = QWidget()
        self.practice_card.setProperty("surfaceRole", SurfaceRole.CARD.value)
        self.alt_layout.addWidget(self.practice_card, 1)

        self.main_layout.addLayout(self.alt_layout, 3)


class PersonalizationPage(QWidget):
    def __init__(self, application, metrics: UiMetrics, event_bus: EventBus):
        super().__init__()
        self.application = application
        self.metrics = metrics
        self.event_bus = event_bus

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setProperty("surfaceRole", SurfaceRole.PANEL.value)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,

        )
        self.main_layout.setSpacing(self.metrics.space_20)

        self.header_layout = QVBoxLayout()
        self.header_layout.setContentsMargins(0, 0, 0, 0)
        self.header_layout.setSpacing(0)

        self.title = QLabel("Igloo")
        self.title.setProperty("textRole", TextRole.WELCOME_TITLE.value)
        self.header_layout.addWidget(self.title)

        self.subtitle = QLabel("I have to bludgeon my ex-girlfriend to death with the balance board first.")
        self.subtitle.setProperty("textRole", TextRole.WELCOME_SUBTITLE.value)
        self.header_layout.addWidget(self.subtitle)

        self.main_layout.addLayout(self.header_layout)


class DonePage(QWidget):
    def __init__(self, application, metrics: UiMetrics, event_bus: EventBus):
        super().__init__()
        self.application = application
        self.metrics = metrics
        self.event_bus = event_bus

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setProperty("surfaceRole", SurfaceRole.PANEL.value)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,

        )
        self.main_layout.setSpacing(self.metrics.space_20)

        self.header_layout = QVBoxLayout()
        self.header_layout.setContentsMargins(0, 0, 0, 0)
        self.header_layout.setSpacing(0)

        self.title = QLabel("Ibe Wudge")
        self.title.setProperty("textRole", TextRole.WELCOME_TITLE.value)
        self.header_layout.addWidget(self.title)

        self.subtitle = QLabel("I swear to God I just saw the instructor winking at me.")
        self.subtitle.setProperty("textRole", TextRole.WELCOME_SUBTITLE.value)
        self.header_layout.addWidget(self.subtitle)

        self.main_layout.addLayout(self.header_layout)


from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QPainter, QPainterPath
from PySide6.QtWidgets import QLabel


class CircularImage(QLabel):
    def __init__(self, size=64, parent=None):
        super().__init__(parent)

        self.setFixedSize(size, size)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def set_image(self, path):
        pixmap = QPixmap(path)

        if pixmap.isNull():
            return

        pixmap = pixmap.scaled(
            self.size(),
            Qt.AspectRatioMode.KeepAspectRatioByExpanding,
            Qt.TransformationMode.SmoothTransformation
        )

        result = QPixmap(self.size())
        result.fill(Qt.GlobalColor.transparent)

        painter = QPainter(result)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        path = QPainterPath()
        path.addEllipse(0, 0, self.width(), self.height())

        painter.setClipPath(path)
        painter.drawPixmap(0, 0, pixmap)

        painter.end()

        self.setPixmap(result)


class UserInfoCard(Card):
    def __init__(
        self,
        metrics: UiMetrics,
        event_bus: EventBus,
        parent: QWidget | None = None
    ) -> None:
        super().__init__(metrics, event_bus, parent)

        self._metrics = metrics

        self.alt_layout = QHBoxLayout()
        self.alt_layout.setContentsMargins(0, 0, 0, 0)
        self.alt_layout.setSpacing(metrics.space_20)

        self.main_layout.addLayout(self.alt_layout, 1)

        self.input_column = QVBoxLayout()
        self.input_column.setContentsMargins(0, 0, 0, 0)
        self.input_column.setSpacing(0)

        self.username_label = QLabel("Username:")
        self.username_label.setProperty("textRole", TextRole.CARD_TITLE.value)
        self.input_column.addWidget(self.username_label)

        self.username_row = QHBoxLayout()
        self.username_row.setContentsMargins(0, 0, 0, 0)
        self.username_row.setSpacing(self.metrics.space_10)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your username...")
        self.username_input.setProperty("inputRole", InputRole.EDITOR.value)
        self.username_row.addWidget(self.username_input)

        self.username_confirm = QPushButton("Submit")
        self.username_confirm.setProperty("buttonVariant", ButtonVariant.SECONDARY.value)
        self.username_row.addWidget(self.username_confirm)

        self.input_column.addLayout(self.username_row)

        self.input_column.addSpacing(self.metrics.space_10)

        self.password_label = QLabel("Password:")
        self.password_label.setProperty("textRole", TextRole.CARD_TITLE.value)
        self.input_column.addWidget(self.password_label)

        self.password_row = QHBoxLayout()
        self.password_row.setContentsMargins(0, 0, 0, 0)
        self.password_row.setSpacing(self.metrics.space_10)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password...")
        self.password_input.setProperty("inputRole", InputRole.EDITOR.value)
        self.password_row.addWidget(self.password_input)

        self.password_confirm = QPushButton("Submit")
        self.password_confirm.setProperty("buttonVariant", ButtonVariant.SECONDARY.value)
        self.password_row.addWidget(self.password_confirm)

        self.input_column.addLayout(self.password_row)

        self.input_column.addSpacing(self.metrics.space_10)

        self.password2_label = QLabel("Confirm Password:")
        self.password2_label.setProperty("textRole", TextRole.CARD_TITLE.value)
        self.input_column.addWidget(self.password2_label)

        self.password2_row = QHBoxLayout()
        self.password2_row.setContentsMargins(0, 0, 0, 0)
        self.password2_row.setSpacing(self.metrics.space_10)

        self.password2_input = QLineEdit()
        self.password2_input.setPlaceholderText("Confirm your password...")
        self.password2_input.setProperty("inputRole", InputRole.EDITOR.value)
        self.password2_row.addWidget(self.password2_input)

        self.password2_confirm = QPushButton("Submit")
        self.password2_confirm.setProperty("buttonVariant", ButtonVariant.SECONDARY.value)
        self.password2_row.addWidget(self.password2_confirm)

        self.input_column.addLayout(self.password2_row)

        self.input_column.addStretch()

        self.tiptext = QLabel("")
        self.tiptext.setProperty("textRole", TextRole.DANGER.value)
        self.input_column.addWidget(self.tiptext)

        self.alt_layout.addLayout(self.input_column, 1)

        self.divider = QFrame()
        self.divider.setObjectName("sidebarHeaderDivider")
        self.divider.setFrameShape(
            QFrame.Shape.NoFrame,
        )
        self.divider.setProperty(
            "dividerRole",
            DividerRole.DEFAULT.value,
        )
        self.divider.setFixedWidth(
            self.metrics.border_thin,
        )
        self.alt_layout.addWidget(self.divider)

        self.movie_label = QLabel()
        self.movie_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.movie_label.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)

        movie = QMovie(":/anim/welcome.gif")
        self.movie_label.setMovie(movie)
        self.movie_label.setScaledContents(True)
        movie.start()

        self.alt_layout.addWidget(self.movie_label, 1)


class DescriptionCard(Card):
    def __init__(
        self,
        metrics: UiMetrics,
        event_bus: EventBus,
        parent: QWidget | None = None
    ) -> None:
        super().__init__(metrics, event_bus, parent)

        self._metrics = metrics

        self.description_label = QLabel("Description:")
        self.description_label.setProperty("textRole", TextRole.CARD_TITLE.value)
        self.main_layout.addWidget(self.description_label)

        self.description_input = QTextEdit()
        self.description_input.setPlaceholderText("Enter profile description...")
        self.description_input.setProperty("inputRole", InputRole.EDITOR.value)
        self.main_layout.addWidget(self.description_input, 1)

        self.description_confirm = QPushButton("Submit")
        self.description_confirm.setProperty("buttonVariant", ButtonVariant.SECONDARY.value)
        self.main_layout.addWidget(self.description_confirm)


class ExtraCard(Card):
    def __init__(
        self,
        metrics: UiMetrics,
        event_bus: EventBus,
        parent: QWidget | None = None
    ) -> None:
        super().__init__(metrics, event_bus, parent)

        self._metrics = metrics


class CollageCard(Card):
    def __init__(
        self,
        metrics: UiMetrics,
        event_bus: EventBus,
        parent: QWidget | None = None
    ) -> None:
        super().__init__(metrics, event_bus, parent)

        self._metrics = metrics


class LanguageDirectoryCard(Card):
    def __init__(
        self,
        metrics: UiMetrics,
        event_bus: EventBus,
        parent: QWidget | None = None
    ) -> None:
        super().__init__(metrics, event_bus, parent)

        self._metrics = metrics

        # Alphabetically sorted source data
        self.items = tuple(sorted(langs, key=str.casefold))
        self._selected_item: str | None = None

        self.search = QLineEdit()
        self.search.setPlaceholderText("Search...")
        self.search.setProperty("inputRole", InputRole.SEARCH.value)
        self.search.textChanged.connect(self.filter_items)

        # Scrollable list
        self.list_widget = QListWidget()
        self.list_widget.itemClicked.connect(self.select_item)

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.layout.addWidget(self.search)
        self.layout.addWidget(self.list_widget)

        self.main_layout.addLayout(self.layout)

        self.filter_items("")

    def filter_items(self, text: str) -> None:
        text = text.casefold()

        filtered = [
            item
            for item in self.items
            if text in item.casefold()
        ]

        if self._selected_item in filtered:
            filtered.remove(self._selected_item)
            filtered.insert(0, self._selected_item)

        self.list_widget.clear()
        self.list_widget.addItems(filtered)

        if filtered and filtered[0] == self._selected_item:
            self.list_widget.setCurrentRow(0)

    def select_item(self, item: QListWidgetItem) -> None:
        self._selected_item = item.text()
        self.filter_items(self.search.text())