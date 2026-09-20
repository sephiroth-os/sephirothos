"""Geometry Dash Performance Service."""

from __future__ import annotations

from dataclasses import dataclass
from random import Random
import win32pdh
import psutil
import pywintypes

DISK_ACTIVITY_COUNTER = r"\PhysicalDisk(_Total)\% Disk Time"

class PerformanceError(RuntimeError):
    """Raised when system performance information cannot be read."""


class WinCounter:
    """Read one Windows Performance Data Helper counter."""

    def __init__(self, path: str) -> None:
        self._query = win32pdh.OpenQuery()

        try:
            add_counter = getattr(
                win32pdh,
                "AddEnglishCounter",
                win32pdh.AddCounter,
            )
            self._counter = add_counter(
                self._query,
                path,
            )

            win32pdh.CollectQueryData(self._query)
        except Exception:
            win32pdh.CloseQuery(self._query)
            self._query = None
            raise

    def value(self) -> float:
        """Collect and return the formatted counter value."""

        if self._query is None:
            raise PerformanceError("The performance counter is closed.")

        win32pdh.CollectQueryData(self._query)

        _, value = win32pdh.GetFormattedCounterValue(
            self._counter,
            win32pdh.PDH_FMT_DOUBLE,
        )

        return float(value)

    def close(self):
        """Close the underlying PDH query."""

        if self._query is None:
            return

        win32pdh.CloseQuery(self._query)
        self._query = None


@dataclass(frozen=True, slots=True)
class PerformanceSnapshot:
    """Current dashboard performance values."""

    cpu_percentage: float
    memory_percentage: float
    disk_activity_percentage: float
    piss_percentage: float


class PerformanceService:
    """Produce nonblocking system performance snapshots."""

    def __init__(
        self,
        randomizer: Random | None = None
    ) -> None:
        self._randomizer = randomizer or Random()
        self._piss_percentage = self._randomizer.uniform(
            0.0,
            100.0,
        )

        psutil.cpu_percent(interval=None)

        try:
            self._disk_counter = WinCounter(
                DISK_ACTIVITY_COUNTER,
            )
        except (OSError, pywintypes.error) as error:
            raise PerformanceError(
                "Could not initialize the Windows disk activity counter."
            ) from error

    def snapshot(self) -> PerformanceSnapshot:
        """Return current CPU, memory, disk, and piss values."""

        try:
            cpu_percentage = psutil.cpu_percent(interval=None)
            memory_percentage = psutil.virtual_memory().percent
            disk_activity_percentage = self._disk_counter.value()
        except (
            OSError,
            pywintypes.error,
            RuntimeError,
            psutil.Error,
        ) as error:
            raise PerformanceError("Could not read system performance information.") from error

        self._piss_percentage = self._randomizer.uniform(
            0.0,
            100.0,
        )

        return PerformanceSnapshot(
            cpu_percentage=self._clamp_percentage(cpu_percentage),
            memory_percentage=self._clamp_percentage(memory_percentage),
            disk_activity_percentage=self._clamp_percentage(disk_activity_percentage),
            piss_percentage=self._clamp_percentage(disk_activity_percentage),
        )

    def close(self) -> None:
        """Release performance-counter resources."""

        try:
            self._disk_counter.close()
        except (OSError, pywintypes.error) as error:
            raise Warning("Could not close the disk activity counter.")

    @staticmethod
    def _clamp_percentage(value: float) -> float:
        return min(max(float(value), 0.0), 100.0)