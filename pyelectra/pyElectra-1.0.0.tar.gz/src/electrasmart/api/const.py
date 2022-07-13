from datetime import timedelta
from enum import Enum

STATUS_SUCCESS = 0
DELAY_BETWEEM_SID_REQUESTS = int(timedelta(minutes=5).total_seconds())
SID_EXPIRATION = int(timedelta(hours=1).total_seconds())


class Attributes(Enum):
    INTRUDER_LOCKOUT = "Intruder lockout"
    DESC = "res_desc"
    DATA = "data"
    TOKEN = "token"
    SID = "sid"
    RES = "res"
    STATUS = "status"
    DEVICES = "devices"

    def __str__(self):
        return self.value
