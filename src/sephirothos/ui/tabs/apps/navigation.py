"""Apps tab page identities."""

from enum import StrEnum


class AppsPageId(StrEnum):
    ALL = "all"


APPS_PAGE_LABELS: dict[AppsPageId, str] = {
    AppsPageId.ALL: "All",
}

APPS_PAGE_ORDER: tuple[AppsPageId, ...] = (AppsPageId.ALL,)

DEFAULT_APPS_PAGE = AppsPageId.ALL