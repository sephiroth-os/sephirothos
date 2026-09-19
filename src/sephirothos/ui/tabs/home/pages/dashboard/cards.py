from PySide6.QtWidgets import QWidget

from sephirothos.events import EventBus
from sephirothos.ui.metrics import UiMetrics
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


class PerformanceCard(Card):
    def __init__(
        self,
        metrics: UiMetrics,
        event_bus: EventBus,
        parent: QWidget | None = None
    ) -> None:
        super().__init__(metrics, event_bus, parent)

        self._metrics = metrics

        self.title.setText("Performance")


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

        self.title.setText("Piss O' Meter")