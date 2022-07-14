from enum import Enum


class FixType(Enum):
    NO_GPS = 0
    NO_FIX = 1
    FIX_2D = 2
    FIX_3D = 3
    FIX_DGPS = 4
    RTK_FLOAT = 5
    RTK_FIXED = 6
