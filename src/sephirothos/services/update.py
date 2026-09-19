from __future__ import annotations

from PySide6.QtCore import QObject, QThread, Signal, Slot
from semantic_version import Version
import requests


class UpdateInfo:
    def __init__(self, version: Version):
        self.version = version


class UpdateWorker(QObject):
    finished = Signal(object)
    failed = Signal(Exception)

    def __init__(self, current_version: str):
        super().__init__()
        self.current_version = Version(current_version)

    @Slot()
    def run(self):
        try:
            response = requests.get(
                "https://api.github.com/repos/"
                "sephiroth-os/sephirothos/releases/latest",
                timeout=10,
            )
            response.raise_for_status()

            release = response.json()

            latest_version = Version(
                release["tag_name"].lstrip("v")
            )

            if latest_version <= self.current_version:
                self.finished.emit(None)
                return

            for asset in release.get("assets", []):
                if asset["name"].lower().endswith(".zip"):
                    self.finished.emit(
                        UpdateInfo(
                            latest_version,
                            asset["browser_download_url"],
                        )
                    )
                    return

            self.finished.emit(None)

        except Exception as exc:
            self.failed.emit(exc)


class UpdateService(QObject):
    update_available = Signal(object)

    def __init__(self, current_version: str, parent=None):
        super().__init__(parent)

        self.current_version = current_version

        self._thread: QThread | None = None
        self._worker: UpdateWorker | None = None

    def check(self):
        if self._thread is not None:
            return

        self._thread = QThread()
        self._worker = UpdateWorker(self.current_version)

        self._worker.moveToThread(self._thread)

        self._thread.started.connect(self._worker.run)

        self._worker.finished.connect(
            self._on_finished
        )

        self._worker.failed.connect(
            self._on_failed
        )

        self._worker.finished.connect(
            self._thread.quit
        )

        self._worker.failed.connect(
            self._thread.quit
        )

        self._thread.finished.connect(
            self._cleanup
        )

        self._thread.start()

    def _on_finished(self, update):
        if update is not None:
            self.update_available.emit(update)

    def _on_failed(self, error):
        print(f"[updater]: Update check failed: {error}")

    def _cleanup(self):
        self._worker = None
        self._thread = None