#!/usr/bin/python3
# -----------------------------------------------
"""
    DESCRIPTION:
        Functions for using dates stored as int

    ASSUMPTIONS:
        The tools module assumes dates are valid and are of the expected type.
        See the core module for the more resilient class

    LIMITATIONS:
        Uses the Gregorian calendar and makes no adjustment for the Julian calendar changeover.
        Therefore only use dates from 1583.
"""
# -----------------------------------------------

import datetime
from typing import Union

from . import _core as udc
from . import _tools as udt

# -----------------------------------------------


def add_days(iymd: int, days: int) -> int:
    """
    Adds a number of days to a date in in Ymd format
    :param iymd: int, the date in Ymd format
    :param days: int, the number of days to add
    :return: int, the new date in Ymd format
    """

    return udc.glue_parts(
        *udc.epoch_to_parts(udc.epoch_from_parts(*udc.explode_iymd(iymd)) + days)
    )


# -----------------------------------------------


def add_months(iymd: int, months: int) -> int:
    """
    Adds given months to a date. Use negative months to subtract months
    :param iymd: int, the date in Ymd format
    :param months: int, the number of months
    :return: int, the new date
    """

    return udc.glue_parts(*udc.add_months(*udc.explode_iymd(iymd), months))


# -----------------------------------------------


def add_weekdays(iymd: int, weekdays: int) -> int:
    """
    Adds a number of weekdays, monday to friday, to a date in in Ymd format
    :param iymd: int, the date in Ymd format
    :param weekdays: int, the number of days to add
    :return: int, the new date in Ymd format
    """

    return udc.glue_parts(
        *udc.add_weekdays(udc.epoch_from_parts(*udc.explode_iymd(iymd)), weekdays)
    )


# -----------------------------------------------


def as_datetime(
        iymd: Union[int, str],
        fmt: str = 'Ymd',
        yy_pivot: str = None,
        rtype: str = 'datetime') -> Union[datetime.datetime, datetime.date, None]:
    """
    Returns as_ymd function as a datetime or date
    :param iymd: int or str, the date value, missing month or day defaults to 1.
    :param fmt: str, the date format. Valid values: Yymd, in any order.
    :param yy_pivot: the pivot year for two digit years
    :param rtype: str, the return type, datetime or date
    :return: datetime, date or None
    """

    ymd = as_ymd(iymd, fmt, yy_pivot)
    if ymd:
        d_ymd = datetime.datetime.strptime(str(ymd), '%Y%m%d')
        if rtype == 'date':
            return d_ymd.date()
        return d_ymd
    return None


# -----------------------------------------------


def as_iymd(idate: Union[int, str], fmt: str, yy_pivot: int = None) -> Union[int, None]:
    """
    Converts the ymd input to the Ymd format from the given format
    :param idate: int or str, the date value, missing month or day defaults to 1.
    :param fmt: str, the date format. Valid values: Yymd, in any order.
    :param yy_pivot: the pivot year for two digit years
    :return: int, the date in Ymd format
    """

    parts = udc.as_parts(idate, fmt, yy_pivot)
    return udt.YMD(*parts).iymd if parts else None


# -----------------------------------------------


def as_ymd(iymd: Union[int, str], fmt: str, yy_pivot: int = None) -> Union[udt.YMD, None]:
    """
    Converts the ymd input to the Ymd format from the given format
    :param iymd: int or str, the date value, missing month or day defaults to 1.
    :param fmt: str, the date format. Valid values: Yymd, in any order.
    :param yy_pivot: the pivot year for two digit years
    :return: int, the date in Ymd format
    """

    parts = udc.as_parts(iymd, fmt, yy_pivot)
    return udt.YMD(*parts) if parts else None


# -----------------------------------------------


def day_of_week(iymd: int) -> int:
    """
    Calculates the number for day of the week. Sunday = 0, Monday = 1...
    :param iymd: int, date in Ymd format
    :return: int, the day number 0 to 6
    """

    return (udc.epoch_from_parts(*udc.explode_iymd(iymd)) - 1) % 7


# -----------------------------------------------


def days_between(from_iymd: int, to_iymd: int) -> int:
    """
    Calculates the days between two dates
    :param from_iymd: int, the from date in Ymd format
    :param to_iymd: int, the to date in Ymd format
    :return: int, the days between the dates
    """

    return (
        udc.epoch_from_parts(*udc.explode_iymd(to_iymd))
        - udc.epoch_from_parts(*udc.explode_iymd(from_iymd))
    )


# -----------------------------------------------


def is_leap_year(year: int) -> int:
    """
    Is the year a leap year
    :param year: int, the year
    :return: int, 1 for leap year, 0 not a leap year
    """

    return udc.is_leap_year(year)


# -----------------------------------------------


def is_valid(iymd: int) -> bool:
    """
    Checks the date is valid. Year expected to be between 1583 and 9999
    :param iymd: int, the date in Ymd format
    :return: bool, is the date is a valid date or not
    """

    return udc.is_valid(*udc.explode_iymd(iymd))


# -----------------------------------------------


def months_between(from_iymd: Union[int, udt.YMD], to_iymd: Union[int, udt.YMD]) -> int:
    """
    Calculates the complete months between two dates
    :param from_iymd: int or YMD, the from date in Ymd or Ym format
    :param to_iymd: int or YMD, the from date in Ymd or Ym format
    :return: int, the complete months between the dates
    """

    from_ymd = udt.YMD(from_iymd) if isinstance(from_iymd, int) else from_iymd
    to_ymd = udt.YMD(to_iymd) if isinstance(to_iymd, int) else to_iymd
    return udt.months_between(from_ymd, to_ymd)


# -----------------------------------------------


def quarter(iymd: int, to_str: bool = True) -> Union[int, str]:
    """
    Calculates the quarter from a year, returning the quarter end month, or quarter number
    :param iymd: int, the date in Ymd or Ym format
    :param to_str: boolean, true returns 2021Q3, otherwise 202103 format
    :return: str 2021Q1, 2021Q2, 2021Q3, 2021Q4; or int 202103, 202106, 202109, 202112
    """

    parts = udc.explode_iymd(iymd)
    return udc.quarter(parts[0], parts[1], to_str)


# -----------------------------------------------


def weekdays_between(from_iymd: int, to_iymd: int, inclusive: bool = False) -> int:
    """
    Calculates the complete months between two dates
    :param from_iymd: int, the from date in Ymd format
    :param to_iymd: int, the from date in Ymd format
    :param inclusive: bool, whether to include the to date as a completed day
    :return: int, the complete months between the dates
    """

    return udc.weekdays_between_epochs(
        udc.epoch_from_parts(*udc.explode_iymd(from_iymd)),
        udc.epoch_from_parts(*udc.explode_iymd(to_iymd)),
        inclusive
    )


# -----------------------------------------------
# End.
