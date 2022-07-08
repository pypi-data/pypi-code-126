import logging
import threading
import time
from typing import Callable, Optional, Union
from warnings import warn

from .settings import (
    SFCThreadManagerSettings,
    SFControllerSettings,
)

logger = logging.getLogger(__name__)


class SFCThreadManager:
    """Manager for the fan controlling thread.

    The SFCThreadManager starts and controls a thread dedicated to regularly polling the CPU temperature and updating
    the fan intensities.

    Attributes:
        cpu_temp_fun: callable that reads the current CPU temperature
        fan_ctl_fun: callable that controls the fan intensities
        settings: settings object

    """

    cpu_temp_fun: Callable
    fan_ctl_fun: Callable
    _thread: Optional[threading.Thread]
    _settings: SFCThreadManagerSettings
    _is_running: bool
    _internal_sleep_time: float = 0.1

    def __init__(
        self,
        cpu_temp_fun: Callable,
        fan_ctl_fun: Callable,
        settings: Union[None, SFControllerSettings, SFCThreadManagerSettings] = None,
    ):
        self.cpu_temp_fun = cpu_temp_fun
        self.fan_ctl_fun = fan_ctl_fun
        self._is_running = False
        self._thread = None
        self.settings = settings or SFCThreadManagerSettings()
        if settings.active:
            self.start()

    @property
    def settings(self) -> SFCThreadManagerSettings:
        return self._settings

    @settings.setter
    def settings(self, val: Union[SFControllerSettings, SFCThreadManagerSettings]):
        if isinstance(val, SFControllerSettings):
            new_settings = SFCThreadManagerSettings(**val.dict())
            if hasattr(self, "_settings"):
                old_settings = self.settings
                if self._is_running and new_settings != old_settings:
                    self.restart()
            self.settings = new_settings
        else:
            self._settings = val

    def start(self):
        """Starts the controller thread."""
        logger.debug("\nStarting thread")
        if not self.settings.active:
            warn("Not starting thread. Fan control is turned off.")
            return
        elif self._is_running:
            warn("Thread already started. Restarting instead.")
            self.restart()
            return
        self._thread = threading.Thread(target=self._execute, daemon=True)
        self._is_running = True
        self._thread.start()

    def _execute(self):
        """Periodically controls the fans.

        This method is run in the _thread. While _is_running is True, the method first calls cpu_temp_fun to update
        the current temperature. Then, fan_ctl_fun is called to update the intensities of all fans.
        Then the thread waits for the refresh_delay to pass and repeats the procedure. Under
        the hood, the controller only waits for a short amount of time to be able to stop and control the fans without
        waiting for the entire sleep_interval to pass.
        """
        logger.debug("Starting execution.")
        delay = self._internal_sleep_time
        # set counter so that the if condition in the while loop is satisfied during the first iteration
        counter = self.settings.refresh_delay / delay
        while self._is_running:
            if counter * delay == self.settings.refresh_delay:
                counter = 0
                self.cpu_temp_fun()
                if self.settings.active:
                    self.fan_ctl_fun()
            counter += 1
            time.sleep(delay)
        logger.debug("Thread stopped.")

    def stop(self):
        """Stops the controller thread."""
        logger.debug("Stopping thread.")
        self._is_running = False
        time.sleep(self._internal_sleep_time)
        self._thread = None

    def restart(self):
        """Restarts the controller thread."""
        logger.debug("Restarting thread.")
        self.stop()
        self.start()
