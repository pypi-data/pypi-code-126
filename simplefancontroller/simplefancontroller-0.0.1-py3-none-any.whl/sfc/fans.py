from abc import ABC, abstractmethod
from typing import Optional, Union
import logging

from pydantic import BaseModel
import numpy as np
from gpiozero import PWMOutputDevice, OutputDevice

from .settings import SFCFanSettings, SFCPWMFanSettings, SFC2PinFanSettings
from simplefancontroller.ui.html_utils import stringify_intensity

logger = logging.getLogger(__name__)


class SFCFanState(BaseModel):
    name: str
    active: bool
    intensity: float
    is_stopped: bool

    @classmethod
    def from_fan(cls, fan):
        return cls(
            name=fan.settings.name,
            active=fan.settings.active,
            intensity=fan.intensity,
            is_stopped=fan._is_stopped,
        )


class SFCFan(ABC):
    """Base class for SFCFans.

    Attributes:
        settings (SFCFanSettings): the fan's settings
        intensity (float): the intensity that the fan is operating on
        device (OutputDevice): gpiozero Device to be controlled
    """

    _settings: SFCFanSettings
    _intensity: float = -1.0
    device: Union[None, OutputDevice, PWMOutputDevice]
    _active: bool
    _is_stopped: bool = False

    @property
    def intensity(self) -> Optional[float]:
        return self._intensity

    @intensity.setter
    def intensity(self, value: float):
        if self.settings.invert_signal is True:
            value = 100 - value
        self._intensity = value

    @property
    def settings(self) -> SFCFanSettings:
        return self._settings

    @settings.setter
    def settings(self, value: SFCFanSettings):
        self._settings = value
        self.update_device()

    @property
    def state(self):
        return SFCFanState.from_fan(self)

    def __init__(self, settings: SFCFanSettings):
        """Init method for fans.

        Args:
            settings (SFCFanSettings): the settings that shall be applied to the fan
        """
        self._settings = settings
        self.intensity = 0.0
        self.device = None
        self.connect()

    @abstractmethod
    def _calculate_intensity(self, temperature: float):
        """Calculates the fan's intensity using a CPU temperature value."""

    @abstractmethod
    def _apply_intensity(self):
        """Sets the pin according to the calculated intensity."""

    @abstractmethod
    def _connect(self):
        """Private method that implements the Fan specific connection."""

    def update_status(self, temperature: float):
        """Calculates a new intensity and sets the pins."""
        logger.debug(f'Updating fan intensity of fan "{self.settings.name}"')
        if self.settings.active and not self._is_stopped:
            self._calculate_intensity(temperature)
            self._apply_intensity()

    def update_device(self):
        """Updates the Fan's device with the Fan's current settings."""
        self.shutdown()
        dev_cls = self.device.__class__
        self.device = dev_cls(pin=self.settings.gpio_pin)

    def connect(self):
        """Sets the device attribute of the correct Device class."""
        if self.device:
            raise SystemError(
                f"Fan {self.settings.name} already connected to Device {self.device}."
            )
        self._connect()

    def shutdown(self):
        """Stops the fan, releases the GPIO pin and removes the attached device.

        Does nothing, if the device is already closed.
        """
        if self.settings.active:
            self.stop()
        if not self.device.closed:
            self.device.close()

    def stop(self):
        """Stops the fan."""
        if self.settings.active and not self.device.closed:
            self.intensity = 0
            self._apply_intensity()
        self._is_stopped = True

    def start(self):
        """Starts the fan."""
        self._is_stopped = False

    @classmethod
    def from_settings(cls, settings: SFCFanSettings):
        if isinstance(settings, SFC2PinFanSettings):
            return SFC2PinFan(settings=settings)
        elif isinstance(settings, SFCPWMFanSettings):
            return SFCPWMFan(settings=settings)


class SFC2PinFan(SFCFan):
    """Class for 2-pin fans."""

    settings: SFC2PinFanSettings
    device: Optional[OutputDevice]

    def __init__(self, settings):
        super().__init__(settings)

    def _calculate_intensity(self, temperature):
        """Calculates the fan intensity for 2-pin fans.

        The fan is turned on, if the current temperature if higher than off_threshold. If the fan is currently turned on
        and the current temperature is at least shutdown_lag lower than off_threshold, the fan is turned off again.

        Args:
            temperature (float): current CPU temperature
        """
        if (
            self.intensity == 100
            and temperature >= self.settings.off_threshold - self.settings.shutdown_lag
        ):
            intensity = 100
        elif temperature > self.settings.off_threshold:
            intensity = 100
        else:
            intensity = 0
        self.intensity = intensity

    def _apply_intensity(self):
        logger.debug(f"Setting Classic pin (pin: {self.settings.gpio_pin})")
        if self.intensity == 0 or self.settings.active is False:
            self.device.off()
        else:
            self.device.on()

    def _connect(self):
        self.device = OutputDevice(pin=self.settings.gpio_pin)


class SFCPWMFan(SFCFan):
    """Class for PWM controlled fans.

    This class is used for 4-pin fans that can be controlled using Pule Width Modulation (PWM).
    """

    settings: SFCPWMFanSettings
    device: PWMOutputDevice

    def __init__(self, settings):
        """Init method for PWM fans.

        Args:
            settings (SFCPWMFanSettings): the settings that shall be applied to the fan

        Raises:
            ValueError: if max_threshold <= off_threshold an exception is raised
        """
        super().__init__(settings)

    def _calculate_intensity(self, temperature):
        """Calculates the intensity for PWM fans.

        Interpolates the intensity between off_threshold and max_threshold if the temperature is between those values.
        Otherwise, the fan is either turned off (temperature < off_threshold) or turned to full speed (temperature >=
        max_threshold). Then sets the current intensity to the calculated value.

        Args:
            temperature (float): current CPU temperature
        """
        intensity = np.round(
            (temperature - self.settings.off_threshold)
            / (self.settings.max_threshold - self.settings.off_threshold)
            * 100,
            0,
        )
        if intensity > 100:
            intensity = 100
        elif intensity < 0:
            intensity = 0
        self.intensity = intensity

    def _apply_intensity(self):
        val = self.intensity / 100 if self.settings.active else 0
        logger.debug(
            f"Setting PWM pin (pin: {self.settings.gpio_pin}) with value {val}."
        )
        self.device.value = val

    def _connect(self):
        self.device = PWMOutputDevice(
            pin=self.settings.gpio_pin, frequency=self.settings.pwm_frequency
        )
        self.device.on()
