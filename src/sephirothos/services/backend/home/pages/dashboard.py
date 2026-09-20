"""The backend for the dashboard page of SephirothOS"""

from __future__ import annotations

from sephirothos.services.performance import PerformanceService, PerformanceSnapshot

class DashboardBackend:
    def __init__(self, event_bus):
        self.event_bus = event_bus
        self.performance = PerformanceService()

        self.snapshot = None

    def get_performance(self) -> PerformanceSnapshot:
        self.snapshot: PerformanceSnapshot = self.performance.snapshot()
        return self.snapshot