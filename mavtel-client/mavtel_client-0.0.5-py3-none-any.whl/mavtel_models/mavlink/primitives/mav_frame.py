from enum import Enum


class MavFrame(Enum):
    UNDEF = 0
    BODY_NED = 1
    VISION_NED = 2
    ESTIM_NED = 3
