import sephirothos.assets.animations.animations_rc

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget, QHBoxLayout, QPushButton, \
    QTextEdit, QLineEdit, QFrame, QSizePolicy
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QMovie, QPainter, QPainterPath

from sephirothos.ui.roles import TextRole, SurfaceRole, ButtonVariant, InputRole, DividerRole
from sephirothos.events import EventBus
from sephirothos.ui.metrics import UiMetrics

from sephirothos.ui.widgets.card import Card


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