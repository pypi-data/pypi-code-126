from datetime import datetime
from typing import Optional
from zoneinfo import ZoneInfo

from souswift_core.models import Model


def now(tz: Optional[ZoneInfo] = None):
    if tz is None:
        tz = ZoneInfo('America/Sao_Paulo')
    return datetime.now(tz=tz)


def to_aware(dt: datetime, tz: Optional[ZoneInfo] = None):
    if tz is None:
        tz = ZoneInfo('America/Sao_Paulo')
    return dt.replace(tzinfo=tz)


def _to_aware(value: datetime, **kwargs):
    del kwargs
    return to_aware(value, value.tzinfo)   # type: ignore


class AwareDatetime(datetime):
    @classmethod
    def __get_validators__(cls):
        yield _to_aware


class Test(Model):
    current_date: AwareDatetime
