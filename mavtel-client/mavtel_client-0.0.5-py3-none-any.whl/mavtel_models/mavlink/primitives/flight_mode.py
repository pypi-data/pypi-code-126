from enum import Enum


class FlightMode(Enum):
    UNKNOWN = 0
    READY = 1
    TAKEOFF = 2
    HOLD = 3
    MISSION = 4
    RETURN_TO_LAUNCH = 5
    LAND = 6
    OFFBOARD = 7
    FOLLOW_ME = 8
    MANUAL = 9
    ALTCTL = 10
    POSCTL = 11
    ACRO = 12
    STABILIZED = 13
    RATTITUDE = 14
