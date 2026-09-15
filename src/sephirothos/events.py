"""Your mom's Wi-Fi router."""

from PySide6.QtCore import QObject, Signal


class EventBus(QObject):
    quit_requested = Signal()
    restart_requested = Signal()
