from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget, QHBoxLayout, QSizePolicy, \
    QLineEdit, QListWidgetItem, QListWidget
from PySide6.QtCore import Qt
from PySide6.QtWebEngineWidgets import QWebEngineView

from sephirothos.content.languages import LANGUAGES

from sephirothos.ui.roles import TextRole, SurfaceRole, InputRole
from sephirothos.events import EventBus
from sephirothos.ui.metrics import UiMetrics
from sephirothos.ui.widgets.card import Card

langs = LANGUAGES

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