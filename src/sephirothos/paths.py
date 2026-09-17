"""Filesystem locations used by SephirothOS."""

import os
from collections.abc import Mapping
from pathlib import Path

from sephirothos.metadata import APPLICATION_NAME, ORGANIZATION_NAME


class PathConfigurationError(RuntimeError):
    """Raised when required Windows path cannot be determined."""


def app_data_directory(
        environment: Mapping[str, str] | None = None,
) -> Path:
    """Return the user-specific SephirothOS application data directory."""

    env = os.environ if environment is None else environment
    appdata = env.get("APPDATA")

    if not appdata:
        raise PathConfigurationError("The APPDATA environment variable is unavailable.")

    return Path(appdata) / ORGANIZATION_NAME / APPLICATION_NAME


def config_path(environment: Mapping[str, str] | None = None) -> Path:
    """Return the path to the user configuration file."""

    return app_data_directory(environment) / "config.json"


def log_directory(environment: Mapping[str, str] | None = None) -> Path:
    """Return the path to the log directory."""

    return app_data_directory(environment) / "logs"


def cache_directory(environment: Mapping[str, str] | None = None) -> Path:
    """Return the path to the cache directory."""

    return app_data_directory(environment) / "cache"