from __future__ import annotations
from abc import ABC, abstractmethod
from socket import gethostname
from datetime import datetime as dt
from warnings import warn
import logging
from typing import TYPE_CHECKING

from influxdb_client import InfluxDBClient, Point

from .fans import SFCFan
from .settings import (
    SFCDBSettings,
    SFCInfluxDBSettings,
)

if TYPE_CHECKING:
    from simplefancontroller.sfc.data_manager import SFCDataManager


logger = logging.getLogger(__name__)


class SFCDatabaseClient(ABC):
    """Abstract base class for SimpleFanController Database Clients.

    Attributes:
        connected (bool): indicator that shows whether the client is connected to the database or not
        settings (SFCDBSettings): settings for the client
    """

    connected: bool
    data_manager: SFCDataManager
    _settings: SFCDBSettings

    def __init__(self, settings: SFCDBSettings):
        self.connected = False
        self.settings = settings

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        logger.debug("Closing database connection.")
        self._disconnect()

    def write(self, fan: SFCFan):
        """Writes a fan's current intensity to a database.

        Args:
            fan (SFCFan): fan to persist
        """
        logger.debug(
            f"Writing intensity of Fan {fan.settings.name} ({fan.intensity} %) to database."
        )
        self.connect()
        if self.settings.active:
            self._write(fan)
        self.disconnect()

    def connect(self):
        """Connects to database"""
        logger.debug(f"Connecting to database with settings {self.settings}.")
        if self.connected:
            warn("Already connected to database. Disconnecting.")
            self.disconnect()
        self._connect(self.settings)
        self.connected = True

    def disconnect(self):
        """Disconnects from database."""
        logger.debug("Disconnecting from database.")
        if self.connected:
            self._disconnect()
            self.connected = False
        else:
            raise SystemError("Not connected to any database.")

    @classmethod
    def from_settings(cls, settings: SFCDBSettings):
        if isinstance(settings, SFCInfluxDBSettings):
            return SFCInfluxDBClient(settings=settings)

    @abstractmethod
    def _write(self, fan: SFCFan):
        """Writes a Fan's current intensity to a database.

        Must be implemented for every SFCDatabaseClient.

        Args:
            fan (SFCFan): fan to persist
        """

    @abstractmethod
    def _connect(self, settings: SFCDBSettings):
        """Connects to database.

        Must be implemented for every SFCDatabaseClient.
        """

    @abstractmethod
    def _disconnect(self):
        """Disconnects from database.

        Must be implemented for every SFCDatabaseClient.
        """


class SFCInfluxDBClient(SFCDatabaseClient):
    """InfluxDB client for SimpleFanController"""

    settings: SFCInfluxDBSettings
    client: InfluxDBClient

    def _connect(self, settings: SFCInfluxDBSettings):
        self.client = InfluxDBClient(
            url=f"{settings.hostname}:{settings.port}",
            token=settings.token,
            org=settings.organisation,
        )

    def _disconnect(self):
        self.client.close()

    def _write(self, fan: SFCFan):
        self.client.write_api().write(
            bucket=self.settings.bucket,
            record=Point(self.settings.measurement)
            .tag("host", gethostname())
            .tag("device", fan.settings.name)
            .field("intensity", float(fan.intensity))
            .time(dt.utcnow().isoformat()),
        )
