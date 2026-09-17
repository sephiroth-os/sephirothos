"""Home page registry."""

from dataclasses import dataclass
from typing import TypeAlias

from PySide6.QtWidgets import QWidget

from .activity_monitor.page import ActivityMonitorPage
from .dashboard.page import DashboardPage
from .other.page import OtherPage
from .piss_explorer.page import PissExplorerPage
from .settings.page import SettingsPage
from .start.page import StartPage
from .taxes.page import TaxesPage
from .terminal.page import TerminalPage


PageClass: TypeAlias = type[QWidget]


@dataclass(frozen=True)
class HomePage:
    """Definition of a page available in the Home tab."""

    id: str
    label: str
    page: PageClass


PAGES: tuple[HomePage, ...] = (
    HomePage(
        id="dashboard",
        label="Dashboard",
        page=DashboardPage,
    ),
    HomePage(
        id="taxes",
        label="Taxes",
        page=TaxesPage,
    ),
    HomePage(
        id="start",
        label="Start",
        page=StartPage,
    ),
    HomePage(
        id="activity_monitor",
        label="Activity Monitor",
        page=ActivityMonitorPage,
    ),
    HomePage(
        id="piss_explorer",
        label="Piss Explorer",
        page=PissExplorerPage,
    ),
    HomePage(
        id="terminal",
        label="Terminal",
        page=TerminalPage,
    ),
    HomePage(
        id="settings",
        label="Settings",
        page=SettingsPage,
    ),
    HomePage(
        id="other",
        label="Other",
        page=OtherPage,
    ),
)


DEFAULT_HOME_PAGE = "dashboard"