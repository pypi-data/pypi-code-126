"""Sinai is a library to help you monitor everything."""
from abc import ABC

from sinai.types import MonitorInstance

VERSION = "0.0.5"


class BaseView(ABC):
    def __init__(self, monitor: MonitorInstance):
        self.monitor = monitor
