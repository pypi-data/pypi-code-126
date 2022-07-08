from __future__ import annotations
import logging
from typing import Generator, TYPE_CHECKING

from .fans import SFCFan, SFCFanState
from .settings import SFCFanSettings

if TYPE_CHECKING:
    from simplefancontroller.sfc.data_manager import SFCDataManager

logger = logging.getLogger(__name__)


class SFCFanStorage:
    """Storage for SFCFan instances.

    Stores SFCFan instances in a list and provides an API for interacting with them.

    Attributes:
        data_manager (SFCDataManager): persists data
        _container (list): list that contains the SFCFan instances
    """

    data_manager: SFCDataManager
    _container: list[SFCFan]

    def __init__(self, data_manager: SFCDataManager):
        self.data_manager = data_manager
        self._container = []

    def add_fan(self, fan: SFCFan):
        """Adds a fan to the Storage.

        Args:
            fan (SFCFan): fan to add
        """
        logger.debug(f"Adding fan {fan}.")
        fan_name = fan.settings.name
        if fan_name in self.get_fan_names():
            raise ValueError(f"A fan with the ID {fan_name} already exists.")
        self._container.append(fan)

    def remove_fan(self, fan_name: str):
        """Removes a fan from the storage by name.

        Args:
            fan_name (str): name of fan to remove
        """
        logger.debug(f"Removing fan {fan_name}.")
        fan = self.get_fan(fan_name)
        fan.shutdown()
        idx = self._container.index(fan)
        del self._container[idx]
        del fan

    def get_fan(self, fan_name: str) -> SFCFan:
        """Queries a fan instance by its name.

        Args:
            fan_name (str): name of fan to query

        Return:
            SFCFan with specified name
        """
        try:
            return next(fan for fan in self.get_fans() if fan.settings.name == fan_name)
        except StopIteration as e:
            raise ValueError(f"No fan with name {fan_name} found.") from e

    def get_fan_names(self) -> Generator[str, None, None]:
        """Returns the names of all SFCFan instances in the storage.

        Yields:
            names of all SFCFan instances
        """
        yield from map(lambda x: x.settings.name, self.get_fans())

    def update_fan(self, fan_name: str, settings: SFCFanSettings):
        """Update a fan with new settings.

        Args:
            fan_name: name of SFCFan to update
            settings: settings to apply to SFCFan
        """
        logger.debug(f"Updating fan {fan_name} with {settings}")
        fan = self.get_fan(fan_name)
        fan.settings = settings
        self.data_manager.save_fan(fan.settings)

    def get_fans(self):
        """Returns all SFCFan instances in the storage.

        Yields:
            SFCFan instances stored in the storage
        """
        yield from self._container

    def get_occupied_pins(self) -> list[int]:
        """Returns a list of occupied GPIO pins

        Yields:
            GPIO pins currently occupied by SimpleFanController
        """
        yield from map(lambda fan: fan.settings.gpio_pin, self.get_fans())

    def get_state(self) -> dict[str, SFCFanState]:
        """Returns the current fan intensities.

        Yields:
            tuples consisting of SFCFan names and stringified fan intensities
        """
        yield from map(lambda fan: (fan.settings.name, fan.state), self.get_fans())

    def start(self):
        """Stops all fans."""
        logger.debug("Starts all fans.")
        for fan in self.get_fans():
            fan.start()

    def stop(self):
        """Starts all fans."""
        logger.debug("Stops all fans.")
        for fan in self.get_fans():
            fan.stop()

    def shutdown(self):
        """Shuts down all fans managed by this SFCFanManager instance."""
        logger.debug("Shutting down SFCFanStorage.")
        for fan in self.get_fans():
            fan.shutdown()
