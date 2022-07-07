from enum import Enum
from .alvie import store_reservation_to_alvie, store_reservation_to_alvie_v2


class PMS(str, Enum):
    ORACLE = 'ORACLE'
    RMS = 'RMS'
