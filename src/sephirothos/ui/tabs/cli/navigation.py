"""CLI tab page identities."""

from enum import StrEnum


class CLIPageId(StrEnum):
    GET_STARTED = "get_started"


CLI_PAGE_LABELS: dict[CLIPageId, str] = {
    CLIPageId.GET_STARTED: "Get Started",
}

CLI_PAGE_ORDER: tuple[CLIPageId, ...] = (CLIPageId.GET_STARTED,)

DEFAULT_CLI_PAGE = CLIPageId.GET_STARTED