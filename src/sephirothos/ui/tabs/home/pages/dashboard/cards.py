"""Cards for the Dashboard"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QProgressBar, QFrame, QPushButton

from sephirothos.events import EventBus
from sephirothos.ui.metrics import UiMetrics
from sephirothos.ui.roles import TextRole, ProgressRole, SurfaceRole, ProgressVariant, DividerRole, ButtonVariant
from sephirothos.services.performance import PerformanceSnapshot
from sephirothos.ui.widgets.card import Card


class WeatherCard(Card):
    def __init__(
        self,
        metrics: UiMetrics,
        event_bus: EventBus,
        parent: QWidget | None = None
    ) -> None:
        super().__init__(metrics, event_bus, parent)

        self._metrics = metrics

        self.title.setText("Weather")


class TipCard(Card):
    def __init__(
        self,
        metrics: UiMetrics,
        event_bus: EventBus,
        parent: QWidget | None = None
    ) -> None:
        super().__init__(metrics, event_bus, parent)

        self._metrics = metrics

        self.title.setText("Daily Tip")


class QuoteCard(Card):
    def __init__(
        self,
        metrics: UiMetrics,
        event_bus: EventBus,
        parent: QWidget | None = None
    ) -> None:
        super().__init__(metrics, event_bus, parent)

        self._metrics = metrics

        self.title.setText("Quote of the Day")


class _PerformanceMetric(QWidget):
    """One labeled performance percentage and progress bar."""

    def __init__(
        self,
        title: str,
        caption: str,
        metrics: UiMetrics,
        variant: ProgressVariant,
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)

        self.setProperty(
            "surfaceRole",
            SurfaceRole.TRANSPARENT.value,
        )

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.header_layout = QHBoxLayout()
        self.header_layout.setContentsMargins(0, 0, 0, 0)
        self.header_layout.setSpacing(0)

        self.label_layout = QVBoxLayout()
        self.label_layout.setContentsMargins(0, 0, 0, 0)
        self.label_layout.setSpacing(0)

        self.title_label = QLabel(title)
        self.title_label.setProperty(
            "textRole",
            TextRole.BODY.value,
        )

        self.caption_label = QLabel(caption)
        self.caption_label.setProperty(
            "textRole",
            TextRole.CAPTION.value,
        )

        self.value_label = QLabel("—")
        self.value_label.setProperty(
            "textRole",
            TextRole.BODY.value,
        )

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setProperty(
            "progressRole",
            ProgressRole.DEFAULT.value,
        )
        self.progress_bar.setProperty(
            "progressVariant",
            variant.value,
        )

        self.label_layout.addWidget(self.title_label)
        self.label_layout.addWidget(self.caption_label)

        self.header_layout.addLayout(self.label_layout)
        self.header_layout.addStretch()
        self.header_layout.addWidget(
            self.value_label,
            alignment=Qt.AlignmentFlag.AlignRight,
        )

        self.main_layout.addLayout(self.header_layout)
        self.main_layout.addSpacing(metrics.space_10)
        self.main_layout.addWidget(self.progress_bar)
        self.main_layout.addStretch()

    def set_percentage(self, percentage: float) -> None:
        self.value_label.setText(f"{percentage:.1f}%")
        self.progress_bar.setValue(round(percentage))


class PerformanceCard(Card):
    """Display live system performance information."""

    def __init__(
        self,
        metrics: UiMetrics,
        event_bus: EventBus,
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(metrics, event_bus, parent)

        self.metrics = metrics
        self.event_bus = event_bus

        self.title.setText("Performance")

        self._build_ui(metrics)

    def _build_ui(self, metrics: UiMetrics) -> None:
        self.divider = QFrame()
        self.divider.setFrameShape(QFrame.Shape.NoFrame)
        self.divider.setProperty(
            "dividerRole",
            DividerRole.DEFAULT.value,
        )
        self.divider.setFixedHeight(metrics.border_thin)

        self.content_layout = QVBoxLayout()
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)

        self.cpu_metric = _PerformanceMetric(
            "CPU Usage",
            "Thinking very hard. Hahaha. Hard...",
            metrics,
            ProgressVariant.CPU,
        )

        self.memory_metric = _PerformanceMetric(
            "RAM",
            "Apparently enough to run this.",
            metrics,
            ProgressVariant.MEMORY,
        )

        self.disk_metric = _PerformanceMetric(
            "Disk",
            "I am selling your data as we speak.",
            metrics,
            ProgressVariant.DISK,
        )

        self.piss_metric = _PerformanceMetric(
            "Piss",
            "Bottom text",
            metrics,
            ProgressVariant.PISS,
        )

        self.content_layout.addWidget(self.cpu_metric, 1)
        self.content_layout.addWidget(self.memory_metric, 1)
        self.content_layout.addWidget(self.disk_metric, 1)
        self.content_layout.addWidget(self.piss_metric, 1)

        self.footer_layout = QHBoxLayout()
        self.footer_layout.setContentsMargins(0, 0, 0, 0)
        self.footer_layout.setSpacing(0)

        self.performance_monitor_button = QPushButton("Open Performance Monitor")
        self.performance_monitor_button.setProperty(
            "buttonVariant",
            ButtonVariant.LINK.value,
        )
        self.performance_monitor_button.setCursor(
            Qt.CursorShape.PointingHandCursor,
        )

        self.footer_layout.addWidget(
            self.performance_monitor_button,
        )
        self.footer_layout.addStretch()

        self.footer_divider = QFrame()
        self.footer_divider.setFrameShape(QFrame.Shape.NoFrame)
        self.footer_divider.setProperty(
            "dividerRole",
            DividerRole.DEFAULT.value,
        )
        self.footer_divider.setFixedHeight(metrics.border_thin)

        self.main_layout.addWidget(self.divider)
        self.main_layout.addLayout(self.content_layout, 1)
        self.main_layout.addWidget(self.footer_divider)
        self.main_layout.addLayout(self.footer_layout)

    def set_performance(
        self,
        snapshot: PerformanceSnapshot,
    ) -> None:
        """Display a new performance snapshot."""

        self.cpu_metric.set_percentage(
            snapshot.cpu_percentage,
        )
        self.memory_metric.set_percentage(
            snapshot.memory_percentage,
        )
        self.disk_metric.set_percentage(
            snapshot.disk_activity_percentage,
        )
        self.piss_metric.set_percentage(
            snapshot.piss_percentage,
        )




class NASDAQCard(Card):
    def __init__(
        self,
        metrics: UiMetrics,
        event_bus: EventBus,
        parent: QWidget | None = None
    ) -> None:
        super().__init__(metrics, event_bus, parent)

        self._metrics = metrics

        self.title.setText("NVIDIA Stock")


class QuickCard(Card):
    def __init__(
        self,
        metrics: UiMetrics,
        event_bus: EventBus,
        parent: QWidget | None = None
    ) -> None:
        super().__init__(metrics, event_bus, parent)

        self._metrics = metrics

        self.title.setText("Quick Apps")


class MeterCard(Card):
    def __init__(
        self,
        metrics: UiMetrics,
        event_bus: EventBus,
        parent: QWidget | None = None
    ) -> None:
        super().__init__(metrics, event_bus, parent)

        self._metrics = metrics

        self.title.setText("Important Info")