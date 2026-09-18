from PySide6.QtWidgets import QWidget

from events import EventBus
from ui.metrics import UiMetrics
from ui.widgets.card import Card


class WeatherCard(Card):
    def __init__(
        self,
        metrics: UiMetrics,
        event_bus: EventBus,
        parent: QWidget | None = None
    ) -> None:
        super().__init__(metrics, event_bus, parent)

        self._metrics = metrics


class TipCard(Card):
    def __init__(
        self,
        metrics: UiMetrics,
        event_bus: EventBus,
        parent: QWidget | None = None
    ) -> None:
        super().__init__(metrics, event_bus, parent)

        self._metrics = metrics


class QuoteCard(Card):
    def __init__(
        self,
        metrics: UiMetrics,
        event_bus: EventBus,
        parent: QWidget | None = None
    ) -> None:
        super().__init__(metrics, event_bus, parent)

        self._metrics = metrics


class PerformanceCard(Card):
    def __init__(
        self,
        metrics: UiMetrics,
        event_bus: EventBus,
        parent: QWidget | None = None
    ) -> None:
        super().__init__(metrics, event_bus, parent)

        self._metrics = metrics


class NASDAQCard(Card):
    def __init__(
        self,
        metrics: UiMetrics,
        event_bus: EventBus,
        parent: QWidget | None = None
    ) -> None:
        super().__init__(metrics, event_bus, parent)

        self._metrics = metrics


class QuickCard(Card):
    def __init__(
        self,
        metrics: UiMetrics,
        event_bus: EventBus,
        parent: QWidget | None = None
    ) -> None:
        super().__init__(metrics, event_bus, parent)

        self._metrics = metrics


class MeterCard(Card):
    def __init__(
        self,
        metrics: UiMetrics,
        event_bus: EventBus,
        parent: QWidget | None = None
    ) -> None:
        super().__init__(metrics, event_bus, parent)

        self._metrics = metrics