import logging
from typing import Optional

from gpiozero import CPUTemperature
import numpy as np

from .storage import SFCFanStorage
from .settings import SFControllerSettings, SFCDBSettings
from .data_manager import SFCDataManager
from .database import SFCDatabaseClient
from .thread_manager import SFCThreadManager
from .fans import SFCFan

logger = logging.getLogger(__name__)


class SimpleFanController:
    """SimpleFanController

    Controller for 2-, and 4-pin fans using the GPIO pins on a Raspberry Pi.
    Fans can be added and removed to the included fan_storage

    Attributes:
        settings (SimpleFanControllerSettings): settings of the controller
        fans (SFCFanStorage): specialized list that contains SFCFan objects
        current_temperature (float): current CPU temperature
        db_client (SFCDatabaseClient): database client for persisting fan intensities
        thread_manager (SFCThreadManager): manager of the fan control thread
        data_manager (SFCDataManager): persists data
    """

    _settings: SFControllerSettings
    fans: SFCFanStorage
    current_temperature: Optional[float]
    db_clients: dict[str, SFCDatabaseClient]
    thread_manager: SFCThreadManager
    data_manager: SFCDataManager

    @property
    def settings(self) -> SFControllerSettings:
        return self._settings

    @settings.setter
    def settings(self, v: SFControllerSettings):
        self._settings = v
        self.data_manager.save_settings(v)
        if self.thread_manager:
            self.thread_manager.settings = v

    def __init__(self, settings: Optional[SFControllerSettings] = None):
        """Init method for SimpleFanController.

        Initializes a new controller, deactivates GPIO warnings, sets GPIO mode to BCM and starts a thread manager
        .
        Args:
            settings (SFControllerSettings): settings that shall be applied to the controller
        """
        logger.debug(f"Starting controller with settings {settings}")
        settings = settings or SFControllerSettings()
        self.data_manager = SFCDataManager()
        self.fans = SFCFanStorage(self.data_manager)
        self.current_temperature = None
        self.db_clients = {}
        self.thread_manager = SFCThreadManager(
            cpu_temp_fun=self.get_temperature,
            fan_ctl_fun=self.set_fan_intensities,
            settings=settings,
        )
        self.settings = settings

    def get_db_client(self, name):
        if name not in self.db_clients:
            raise ValueError(f"No database connection with name {name} found.")
        return self.db_clients[name].settings

    def attach_db_client(self, settings: SFCDBSettings):
        if settings.name in self.db_clients:
            raise ValueError(f"Database connection with name {settings.name} already exsists.")
        self.db_clients[settings.name] = SFCDatabaseClient.from_settings(settings)

    def remove_db_client(self, name):
        self.get_db_client(name)
        del self.db_clients[name]

    def update_db_client(self, name: str, settings: SFCDBSettings):
        self.get_db_client(name)
        if name != settings.name:
            self.remove_db_client(name)
        self.db_clients[settings.name] = SFCDatabaseClient.from_settings(settings)

    def get_temperature(self):
        """Reads the current CPU temperature."""
        logger.debug("\nGetting CPU temperature")
        if self.settings.debug:
            self.current_temperature = np.random.randint(40, 80)
        else:
            self.current_temperature = np.round(
                CPUTemperature(sensor_file=self.settings.sensor_file).temperature, 2
            )
        logger.debug(f"Current temperature: {self.current_temperature} °C")
        return self.current_temperature

    def set_fan_intensities(self):
        """Updates fan intensities and publishes data to the attached SFCDatabaseClient.

        Updates the intensities of all attached fans and writes the new intensities to the attached SFCDatabaseClient if activated.
        """
        if not list(self.fans.get_fans()):
            logger.debug("No fans found. Skipping.")
            return
        elif not self.current_temperature:
            logger.info("No temperature reading available. Cannot set fan intensity.")
            return
        for fan in self.fans.get_fans():
            fan.update_status(self.current_temperature)
            logger.debug(
                f'Controlling fan "{fan.settings.name}" with intensity: {fan.intensity}%'
            )
            for client in self.db_clients.values():
                client.write(fan)

    def export_data(self):
        """Exports the current settings to a local SQLite database."""
        logger.debug("Persisting data")
        self.data_manager.save_settings(self.settings)
        for fan in self.fans.get_fans():
            self.data_manager.save_fan(fan.settings)
        for client in self.db_clients.values():
            self.data_manager.save_persistence(client.settings)
        logger.debug("Successfully exported data")

    def import_data(self):
        """Imports settings from the local SQLite database."""
        logger.debug("Importing data")
        for db_name in self.data_manager.get_persistence_names():
            db_client = self.data_manager.get_persistence(db_name)
            self.db_clients[db_client.name] = SFCDatabaseClient.from_settings(db_client)
        for fan_name in self.data_manager.get_fan_names():
            fan_settings = self.data_manager.get_fan(fan_name)
            fan = SFCFan.from_settings(fan_settings)
            self.fans.add_fan(fan)
        logger.debug("Successfully imported data")

    def start(self):
        """Starts controlling the fans."""
        self.fans.start()
        self.thread_manager.start()

    def stop(self):
        """Stops controlling the fans."""
        self.fans.stop()
        self.thread_manager.stop()

    def shutdown(self):
        """Shuts down the controller."""
        self.stop()
        self.data_manager.shutdown()
        self.fans.shutdown()
