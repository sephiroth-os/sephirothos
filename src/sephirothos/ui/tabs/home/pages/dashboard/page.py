"""Home dashboard page"""
import datetime
from random import choice

from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel

from content.subtitles import HOME_SUBTITLES
from events import EventBus
from ui.metrics import UiMetrics
from ui.roles import SurfaceRole, TextRole

from .cards import (
    WeatherCard,
    TipCard,
    QuoteCard,
    PerformanceCard,
    NASDAQCard,
    MeterCard,
    QuickCard,
)


class DashboardPage(QWidget):
    """Primary home dashboard."""

    def __init__(self, metrics: UiMetrics, event_bus: EventBus):
        super().__init__()

        self.metrics = metrics
        self.event_bus = event_bus

        self.setProperty(
            "surfaceRole",
            SurfaceRole.TRANSPARENT.value
        )

        self._build_ui()
        self._configure_clock()

    def _build_ui(self):
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,
            self.metrics.space_20,
        )
        self.main_layout.setSpacing(self.metrics.space_20)

        self.header_layout = QHBoxLayout()
        self.header_layout.setContentsMargins(0, 0, 0, 0)
        self.header_layout.setSpacing(self.metrics.space_20)

        self.title_layout = QVBoxLayout()
        self.title_layout.setContentsMargins(0, 0, 0, 0)
        self.title_layout.setSpacing(self.metrics.space_10)

        self.title_label = QLabel("Welcome to Sephiroth's House")
        self.title_label.setProperty(
            "textRole",
            TextRole.PAGE_TITLE.value
        )

        self.subtitle_label = QLabel(choice(HOME_SUBTITLES))
        self.subtitle_label.setProperty(
            "textRole",
            TextRole.PAGE_SUBTITLE.value
        )

        self.clock_layout = QVBoxLayout()
        self.clock_layout.setContentsMargins(0, 0, 0, 0)
        self.clock_layout.setSpacing(self.metrics.space_10)

        self.time_label = QLabel()
        self.time_label.setProperty(
            "textRole",
            TextRole.PAGE_TITLE.value
        )
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.date_label = QLabel()
        self.date_label.setProperty(
            "textRole",
            TextRole.PAGE_SUBTITLE.value
        )

        self.title_layout.addWidget(self.title_label)
        self.title_layout.addWidget(self.subtitle_label)

        self.clock_layout.addWidget(self.time_label)
        self.clock_layout.addWidget(self.date_label)

        self.header_layout.addLayout(self.title_layout)
        self.header_layout.addStretch()
        self.header_layout.addLayout(self.clock_layout)

        self.main_layout.addLayout(self.header_layout)

        self.weather_card = WeatherCard(
            self.metrics,
            self.event_bus
        )
        self.tip_card = TipCard(
            self.metrics,
            self.event_bus
        )
        self.quote_card = QuoteCard(
            self.metrics,
            self.event_bus
        )
        self.nasdaq_card = NASDAQCard(
            self.metrics,
            self.event_bus
        )
        self.performance_card = PerformanceCard(
            self.metrics,
            self.event_bus
        )
        self.meter_card = MeterCard(
            self.metrics,
            self.event_bus
        )
        self.quick_card = QuickCard(
            self.metrics,
            self.event_bus
        )

        # Entire area beneath the dashboard header
        self.dashboard_layout = QHBoxLayout()
        self.dashboard_layout.setContentsMargins(0, 0, 0, 0)
        self.dashboard_layout.setSpacing(self.metrics.space_20)

        # Left Side
        self.left_column_layout = QVBoxLayout()
        self.left_column_layout.setContentsMargins(0, 0, 0, 0)
        self.left_column_layout.setSpacing(self.metrics.space_20)

        self.top_left_layout = QHBoxLayout()
        self.top_left_layout.setContentsMargins(0, 0, 0, 0)
        self.top_left_layout.setSpacing(self.metrics.space_20)

        self.bottom_left_layout = QHBoxLayout()
        self.bottom_left_layout.setContentsMargins(0, 0, 0, 0)
        self.bottom_left_layout.setSpacing(self.metrics.space_20)

        # Right Side
        self.right_column_layout = QVBoxLayout()
        self.right_column_layout.setContentsMargins(0, 0, 0, 0)
        self.right_column_layout.setSpacing(self.metrics.space_20)

        # Assemble UI
        self.right_column_layout.addWidget(
            self.performance_card,
            3
        )
        self.right_column_layout.addWidget(
            self.nasdaq_card,
            1
        )

        self.top_left_layout.addWidget(
            self.weather_card, 1
        )
        self.top_left_layout.addWidget(
            self.tip_card, 1
        )
        self.top_left_layout.addWidget(
            self.quote_card, 1
        )

        self.bottom_left_layout.addWidget(
            self.meter_card, 1
        )
        self.bottom_left_layout.addWidget(
            self.quick_card, 1
        )

        self.left_column_layout.addLayout(
            self.top_left_layout, 1
        )
        self.left_column_layout.addLayout(
            self.bottom_left_layout, 1
        )

        self.dashboard_layout.addLayout(
            self.left_column_layout,
            3
        )
        self.dashboard_layout.addLayout(
            self.right_column_layout,
            1,
        )

        self.main_layout.addLayout(
            self.dashboard_layout,
            1
        )


    def _configure_clock(self) -> None:
        self.clock_timer = QTimer(self)
        self.clock_timer.setInterval(1000)
        self.clock_timer.timeout.connect(
            self._update_clock,
        )

        self._update_clock()
        self.clock_timer.start()

    def _update_clock(self) -> None:
        now = datetime.datetime.now()

        formatted_time = now.strftime("%I:%M %p").lstrip("0")
        formatted_date = now.strftime("%A, %B %d, %Y").replace(" 0", " ")

        self.time_label.setText(formatted_time)
        self.date_label.setText(formatted_date)