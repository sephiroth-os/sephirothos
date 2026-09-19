"""Apps page registry."""

from dataclasses import dataclass
from typing import TypeAlias

from PySide6.QtWidgets import QWidget

from .all.page import AllPage


PageClass: TypeAlias = type[QWidget]


@dataclass(frozen=True)
class AppsPage:
    """Definition of a page available in the Apps tab."""

    id: str
    label: str
    page: PageClass


PAGES: tuple[AppsPage, ...] = (
    AppsPage(
        id="all",
        label="All",
        page=AllPage,
    ),
)


DEFAULT_APPS_PAGE = "all"