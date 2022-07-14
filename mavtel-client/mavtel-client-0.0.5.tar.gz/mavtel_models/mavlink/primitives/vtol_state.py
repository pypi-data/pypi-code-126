from enum import Enum


class VtolState(Enum):
    UNDEFINED = 0
    TRANSITION_TO_FW = 1
    TRANSITION_TO_MC = 2
    MC = 3
    FW = 4
