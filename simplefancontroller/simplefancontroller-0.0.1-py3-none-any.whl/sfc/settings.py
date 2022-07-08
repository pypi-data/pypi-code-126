"""Settings for various parts of SFC

Settings objects have two purposes:
- they are used for controlling different parts of SFC
- they can be used as DTOs.

"""

from abc import ABC

from pydantic import BaseModel, validator


# FAN SETTINGS
class SFCFanSettings(BaseModel, ABC):
    name: str
    gpio_pin: int
    active: bool = True
    invert_signal: bool = False

    class Config:
        arbitrary_types_allowed = True


class SFC2PinFanSettings(SFCFanSettings):
    off_threshold: int = 40
    shutdown_lag: int = 5


class SFCPWMFanSettings(SFCFanSettings):
    pwm_frequency: int = 25_000
    off_threshold: int = 40
    max_threshold: int = 80

    @validator("max_threshold")
    def max_gt_off_threshold(cls, v):
        # todo: find bug
        if hasattr(cls, "max_threshold"):
            assert v > cls.off_threshold
        return v

    @validator("off_threshold")
    def off_lt_max_threshold(cls, v):
        if hasattr(cls, "max_threshold"):
            assert v < cls.max_threshold
        return v


# DATABASE SETTINGS
class SFCDBSettings(BaseModel, ABC):
    name: str
    active: bool = False


class SFCInfluxDBSettings(SFCDBSettings):
    hostname: str
    token: str
    bucket: str
    organisation: str
    port: int = 8086
    measurement: str = "fans"


# CONTROLLER SETTINGS
class SFCThreadManagerSettings(BaseModel):
    active: bool = False
    refresh_delay: int = 10


class SFControllerSettings(BaseModel):
    debug: bool = True
    active: bool = False
    refresh_delay: int = 10
    sensor_file: str = "/sys/class/thermal/thermal_zone0/temp"
