"""Settings page registry."""

from dataclasses import dataclass
from typing import TypeAlias

from PySide6.QtWidgets import QWidget

from .about.page import AboutPage
from .appearance.page import AppearancePage
from .backup.page import BackupPage
from .developer.page import DeveloperPage
from .experimental.page import ExperimentalPage
from .general.page import GeneralPage
from .notifications.page import NotificationsPage
from .power.page import PowerPage
from .recovery.page import RecoveryPage
from .sound.page import SoundPage
from .storage.page import StoragePage
from .updates.page import UpdatesPage


PageClass: TypeAlias = type[QWidget]


@dataclass(frozen=True)
class SettingsPage:
    """Definition of a page available in the Settings tab."""

    id: str
    label: str
    page: PageClass


PAGES: tuple[SettingsPage, ...] = (
    SettingsPage(
        id="general",
        label="General",
        page=GeneralPage,
    ),
    SettingsPage(
        id="appearance",
        label="Appearance",
        page=AppearancePage,
    ),
    SettingsPage(
        id="notifications",
        label="Notifications",
        page=NotificationsPage,
    ),
    SettingsPage(
        id="sound",
        label="Sound",
        page=SoundPage,
    ),
    SettingsPage(
        id="power",
        label="Power",
        page=PowerPage,
    ),
    SettingsPage(
        id="about",
        label="About",
        page=AboutPage,
    ),
    SettingsPage(
        id="updates",
        label="Updates",
        page=UpdatesPage,
    ),
    SettingsPage(
        id="storage",
        label="Storage",
        page=StoragePage,
    ),
    SettingsPage(
        id="backup",
        label="Backup",
        page=BackupPage,
    ),
    SettingsPage(
      id="recovery",
      label="Recovery",
      page=RecoveryPage,
    ),
    SettingsPage(
        id="developer",
        label="Developer",
        page=DeveloperPage,
    ),
    SettingsPage(
        id="experimental",
        label="Experimental",
        page=ExperimentalPage,
    ),
)


DEFAULT_SETTINGS_PAGE = "general"