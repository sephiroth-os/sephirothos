"""CLI page registry."""

from dataclasses import dataclass
from typing import TypeAlias

from PySide6.QtWidgets import QWidget

from .get_started.page import GetStartedPage
from .history.page import HistoryPage
from .manage_sessions.page import ManageSessionsPage
from .sephiroths_shed.page import SephirothsShedPage


PageClass: TypeAlias = type[QWidget]


@dataclass(frozen=True)
class CLIPage:
    """Definition of a page available in the CLI tab."""

    id: str
    label: str
    page: PageClass


PAGES: tuple[CLIPage, ...] = (
    CLIPage(
        id="get_started",
        label="Get Started",
        page=GetStartedPage,
    ),
    CLIPage(
        id="sephiroth's_shed",
        label="Sephiroth's Shed",
        page=SephirothsShedPage,
    ),
    CLIPage(
        id="manage_sessions",
        label="Manage Sessions",
        page=ManageSessionsPage,
    ),
    CLIPage(
        id="history",
        label="History",
        page=HistoryPage,
    ),
)


DEFAULT_CLI_PAGE = "sephiroth's_shed"