from datetime import datetime

import pytz
from dateutil.rrule import SU, WEEKLY, rrule


def last_sunday_of_month(year: int, month: int) -> datetime:
    """
    Derive date for last Sunday of a month; useful for deriving date for DST start/end
    """
    date_ = datetime(year=year, month=month, day=1)
    # we can find max 5 sundays in a months
    days = rrule(freq=WEEKLY, dtstart=date_, byweekday=SU, count=5)
    # Check if last date is same month,
    # If not this couple year/month only have 4 Sundays
    if days[-1].month == month:
        return days[-1]
    else:
        return days[-2]


def dst_start_utc(year: int) -> datetime:
    """Last Sunday of March"""
    # Get 5 next Sundays from first March
    dst_start = last_sunday_of_month(year, 3)
    return dst_start.replace(hour=1, tzinfo=pytz.UTC)


def dst_end_utc(year: int) -> datetime:
    """Last Sunday of October"""
    dst_end = last_sunday_of_month(year, 10)
    return dst_end.replace(hour=2, tzinfo=pytz.UTC)
