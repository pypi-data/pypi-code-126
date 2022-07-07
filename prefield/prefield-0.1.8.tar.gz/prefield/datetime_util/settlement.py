import calendar
from datetime import date, datetime, time
from typing import Literal, Optional, Tuple

import pytz

from .dst import dst_end_utc, dst_start_utc

Timezones = Literal["UTC", "Europe/London", "CET"]


def settlement_to_datetime(
    date_: date,
    sp_: int,
    trade_timezone: Timezones = "Europe/London",
    period_mins: int = 30,
    closed: Literal["right", "left", "middle"] = "left",
) -> datetime:
    """
    Convert a date and settlement period into a timezone-aware Python datetime object
    for the start or end of the settlement period.

    Parameters
    ----------
    date_ : date
        delivery or settlement date that the settlement periods belongs in

    sp_: int
        settlement period we want to convert to datetime

    trade_timezone: str, "Europe/London"
        timezone of the market

    period_mins: int,30
        length of each trading period in minutes

    closed: str, "left"
        one of left/middle/right. left returns the start of the period, middle the
        middle point and right the end of the period

    Returns
    -------
    UTC datetime for the settlement period

    """
    return from_unixtime(
        settlement_to_epoch(date_, sp_, trade_timezone, period_mins, closed)
    )


def n_settlements_in_date(date_: date, period_mins: int = 30) -> int:
    _, n_settlements = period_start_and_total(0, "UTC", period_mins, date_)

    return n_settlements


def to_unixtime(datetime_: datetime, timezone_: Optional[Timezones] = None) -> int:
    """Convert a python datetime object, `datetime_`, into unixtime int"""
    _validate_datetime("datetime_", datetime_)
    if not timezone_ and not datetime_.tzinfo:
        raise ValueError(
            "EITHER datetime_ must contain tzinfo OR timezone_ must be passed."
        )
    if timezone_ and not datetime_.tzinfo:
        utc_datetime = pytz.timezone(timezone_).localize(datetime_).astimezone(pytz.utc)
    else:
        utc_datetime = datetime_.astimezone(pytz.utc)
    unixtime = int(
        (utc_datetime - datetime(1970, 1, 1, 0, 0, 0, 0, pytz.utc)).total_seconds()
    )
    return unixtime


def from_unixtime(epoch: int, timezone_: Timezones = "UTC") -> datetime:
    """Convert a unix epoch int into datetime"""
    _validate_timestamp(epoch)
    return datetime.fromtimestamp(epoch, tz=pytz.timezone(timezone_))


def settlement_to_epoch(
    date_: date,
    sp_: int,
    trade_timezone: Timezones = "Europe/London",  # timezone that the trade takes place
    period_mins: int = 30,
    closed: Literal["right", "left", "middle"] = "left",
) -> int:
    """
    Convert a date and settlement period into a unix epoch for the start or end of the
    settlement period. The period_mis argument defines the length of each settlement
    period
    """
    _validate_date(date_)
    _validate_sp(sp_, date_)

    # calculate local midnight start time for period 1
    date_start_adjusted = to_unixtime(datetime.combine(date_, time()), trade_timezone)
    ts_raw = date_start_adjusted + (period_mins * 60 * (sp_ - 1))
    timestamp_ = ts_raw

    if closed.lower() == "right":
        timestamp_ += period_mins * 60
    elif closed.lower() == "middle":
        timestamp_ += int(period_mins / 2 * 60)
    return timestamp_


def _validate_datetime(name, datetime_, require_tzinfo=False):
    if not isinstance(datetime_, datetime):
        raise TypeError(f"`{name}` must be of type datetime.datetime")
    if require_tzinfo and not datetime_.tzinfo:
        raise ValueError(f"`{name}` is missing tzinfo")


def _validate_date(date_):
    if not isinstance(date_, date):
        raise TypeError("`date_` must be of type datetime.date")


def _validate_timestamp(epoch: int) -> None:
    if epoch < 0:
        raise ValueError("Invalid value for `epoch`, Unix timestamps cannot be negative")


def _validate_sp(sp_: int, date_: date) -> None:
    max_sp = n_settlements_in_date(date_)
    if not 1 <= sp_ <= max_sp:
        raise ValueError(
            f"`sp_` must be in the interval 1 <= sp_ <= {max_sp} "
            f"on date {date_.isoformat()}, got {sp_}"
        )


def month_end(year: int, month: int) -> date:
    last_day_of_month = calendar.monthrange(year, month)[1]
    return date(year, month, last_day_of_month)


def period_start_and_total(
    local_hour_start: int, local_timezone: Timezones, period_mins: int, date_: date
) -> Tuple[int, int]:
    """
    Method that accounts for the trading timezone and DST to return:
        - The period number for that the trading day starts on
        - The total number of periods in a given day
    """
    periods_per_hour = int(60 / period_mins)
    # min period is 1
    start = 1
    # neglecting DST
    start += periods_per_hour * local_hour_start
    total = (24 - local_hour_start) * periods_per_hour

    dst_start = dst_start_utc(date_.year)
    dst_end = dst_end_utc(date_.year)
    local_tz = pytz.timezone(local_timezone)

    if date_ == dst_start.date():
        local_dst_start = dst_start.astimezone(local_tz)
        # due to time conversion the hour skips
        local_hour_dst_start = local_dst_start.hour - 1
        if local_hour_start >= local_hour_dst_start:
            start -= periods_per_hour
        if local_hour_start <= local_hour_dst_start:
            total -= periods_per_hour

    if date_ == dst_end.date():
        local_dst_end = dst_end.astimezone(local_tz)
        # no need to add/subtract hour when clocks go back
        local_hour_dst_end = local_dst_end.hour
        if local_hour_start >= local_hour_dst_end:
            start += periods_per_hour
        if local_hour_start <= local_hour_dst_end:
            total += periods_per_hour

    return int(start), int(total)
