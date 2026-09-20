"""Local filesystem storage info"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from shutil import disk_usage

BYTES_PER_GIGABYTE = 1024**3


class StorageError(RuntimeError):
    """Raised when a storage error is encountered."""


@dataclass(frozen=True, slots=True)
class StorageSnapshot:
    """Current capacity information for one filesystem."""

    root: Path
    total_bytes: int
    used_bytes: int
    free_bytes: int

    @property
    def used_percentage(self) -> float:
        if self.total_bytes == 0:
            return 0.0

        return self.used_bytes / self.total_bytes * 100

    @property
    def total_gigabytes(self) -> float:
        return self.total_bytes / BYTES_PER_GIGABYTE

    @property
    def free_gigabytes(self) -> float:
        return self.free_bytes / BYTES_PER_GIGABYTE


class StorageService:
    """Read capacity information for drives."""

    def __init__(
        self,
        root: Path | None = None,
    ) -> None:
        self.root = root or self._system_drive_root()

    def snapshot(self) -> StorageSnapshot:
        """Return the current storage state."""

        try:
            usage = disk_usage(self.root)
        except OSError as error:
            raise StorageError(f"Could not read storage information for {self.root}") from error

        return StorageSnapshot(
            root=self.root,
            total_bytes=usage.total,
            used_bytes=usage.used,
            free_bytes=usage.free,
        )

    @staticmethod
    def _system_drive_root() -> Path:
        system_drive = os.environ.get("SystemDrive")

        if system_drive:
            drive = system_drive.rstrip("\\/")
            return Path(f"{drive}\\")

        home_anchor = Path.home().anchor

        if home_anchor:
            return Path(home_anchor)

        raise StorageError("Could not determine the Windows system drive.")