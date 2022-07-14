from enum import Enum


class LandedState(Enum):
    UNKNOWN = 0
    ON_GROUND = 1
    IN_AIR = 2
    TAKING_OFF = 3
    LANDING = 4
