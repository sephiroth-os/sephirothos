"""Settings tab page identities."""

from enum import StrEnum


class SettingsPageId(StrEnum):
    GENERAL = "general"


SETTINGS_PAGE_LABELS: dict[SettingsPageId, str] = {
    SettingsPageId.GENERAL: "General",
}

SETTING_PAGE_ORDER: tuple[SettingsPageId, ...] = (SettingsPageId.GENERAL,)

DEFAULT_SETTINGS_PAGE = SettingsPageId.GENERAL