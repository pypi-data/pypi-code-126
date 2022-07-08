#!/usr/bin/python3
# -----------------------------------------------
"""
    DESCRIPTION:
        Functions for using dates stored as int

    ASSUMPTIONS:
        The intdate module assumes dates are valid and are of the expected type.
        See the _utils module for more resilient functions

    LIMITATIONS:
        No limitations to note
"""
# -----------------------------------------------

from __future__ import annotations
from datetime import datetime, date
from typing import Any, Optional, Tuple, Union

from . import _core as udc

# -----------------------------------------------


def _get_parts(year_or_iymd: int, month: int, day: int) -> Tuple[int, int, int, int]:
    """ Creates the date parts tuple from the provided data. """

    if month is None:  # Assume year_or_ymd is Ymd or Ym format
        if year_or_iymd < 9999_99:
            year_or_iymd = (year_or_iymd * 100) + 1

        return (
            year_or_iymd,
            year_or_iymd // 1_00_00,
            (year_or_iymd % 1_00_00) // 1_00,
            year_or_iymd % 1_00
        )

    # Assume seperate parts provided

    return (
        (year_or_iymd * 1_00_00) + (month * 1_00) + (day or 1),
        year_or_iymd, month, (day or 1)
    )


# -----------------------------------------------


class YMD:
    """ Class of date parts, year, month, day """

    iymd: Optional[int]
    year: Optional[int]
    month: Optional[int]
    day: Optional[int]
    status: str = None

    # ---

    def __init__(
            self,
            year_or_iymd: int,
            month: int = None,
            day: int = None,
            trusted: bool = False
    ):
        """
        Sets the synchronised date values
        :param year_or_iymd: int, the year or date in Ymd format
        :param month: int, optional, the month number, 1 = Jan
        :param day: int, optional, the day. If month supplied and not day, the 1st is assumed
        :param trusted: bool, when trusted validation checks are skipped
        """

        self.iymd, self.year, self.month, self.day = _get_parts(year_or_iymd, month, day)
        self._properties = {}

        if trusted:
            self.status = udc.TRUSTED
        elif udc.is_valid(self.year, self.month, self.day):
            self.status = udc.VALID
        else:
            self.iymd = self.year = self.month = self.day = None
            self.status = udc.INVALID

    # ---
    # Comparison magic methods

    def __lt__(self, other: int) -> bool:
        """ Called on comparison using < operator """
        return self.iymd < other

    def __le__(self, other: int) -> bool:
        """ Called on comparison using <= operator """
        return self.iymd <= other

    def __eq__(self, other: int) -> bool:
        """ Called on comparison using == operator """
        return self.iymd == other

    def __ne__(self, other: int) -> bool:
        """ Called on comparison using != operator """
        return self.iymd != other

    def __ge__(self, other: int) -> bool:
        """ Called on comparison using >= operator """
        return self.iymd >= other

    def __gt__(self, other: int) -> bool:
        """ To get called on comparison using > operator """
        return self.iymd > other

    # ---
    # Operator magic methods

    def __add__(self, other: int) -> YMD:
        """ Called on add operation using + operator. In calendar days """
        return add_days(self, other)

    def __sub__(self, other: Union[int, YMD]) -> Union[int, YMD]:
        """ Called on subtraction operation using - operator. In calendar days """
        if isinstance(other, int):
            return add_days(self, other * -1)
        return days_between(self, other)

    # ---
    # Type conversion magic methods

    def __bool__(self):
        """ Called by built-int bool() method to convert a type to a bool """
        return bool(self.status != udc.INVALID)

    def __int__(self):
        """ Called by built-int int() method to convert a type to an int """
        return self.iymd

    def __repr__(self):
        """ Called by built-int repr() method to return a readable representation of the type """
        return self.iymd

    def __str__(self):
        """ Called by built-int str() method to convert a type to a str """
        return str(self.iymd)

    # ---
    # Restrict attribute updates

    def __setattr__(self, key: str, value: Any):
        """ Assurance that the date has not been manually modifed """

        if self.status:
            raise Exception('Unable to modified YMD')
        self.__dict__[key] = value

    # ---
    # Private modules

    def _get_property(self, name: str) -> Any:
        """
        Gets the ymd date property. Added when first needed,
         rather than at initialisation, for performance.
         Only EPOCH at the moment, but more may be added.
        :param name: str, the property name; [EPOCH]
        :return: the property value
        """

        if name not in self._properties:
            if name == udc.EPOCH:
                self._properties[name] = udc.epoch_from_parts(self.year, self.month, self.day)

        return self._properties[name]

    # ---
    # Public modules

    def day_of_week(self) -> int:
        """
        Calculates the number for day of the week. Sunday = 0, Monday = 1...
        :return: int, the day number 0 to 6
        """

        return udc.day_of_week(self._get_property(udc.EPOCH))

    # ---

    def epoch(self) -> int:
        """
        The epoch value for the date
        :return: int, the epoch value
        """

        return self._get_property(udc.EPOCH)


# -----------------------------------------------


class Undated(YMD):
    """
    Use when encountering dates that are stored as integers, and conversion to datetime and back
    for calculations is not desired.
    """

    def __init__(self, idate: Union[YMD, datetime, date, float, int, str], **kwargs):
        """
        See the properties function for valid parameters
        :param idate: the date, converted by the properties function to YMD class.
        :param kwargs: str, supply format if it not Ymd, Ym
        """

        self.idate = idate
        self.options = kwargs
        self.options['fmt'] = kwargs.get('fmt', None)
        self.options['trusted'] = kwargs.get('trusted', False)
        self.options['yy_pivot'] = kwargs.get('yy_pivot', None)

        if isinstance(idate, YMD):
            super(Undated, idate)
        elif self.options['trusted']:  # Expected to be int in Ymd format.
            super().__init__(idate, trusted=True)
        else:
            super().__init__(*self._idate_to_parts(idate), trusted=True)

    # ---
    # Operator magic methods

    def __add__(self, other: int) -> Undated:
        """ Called on add operation using + operator. In calendar days """
        return Undated(add_days(super(), other))

    def __sub__(self, other: int) -> Undated:
        """ Called on subtraction operation using - operator. In calendar days """
        return Undated(add_days(super(), other * -1))

    # ---
    # Private methods

    def _idate_to_parts(
            self,
            idate: Union[datetime, date, float, int, str]
    ) -> Union[Tuple[int, int, int], None]:
        """
        Converts idate to it's year, month, day parts
        :param idate: int, or other type, to allow flexibility with incoming data
        :return: tuple (year, month, day)
        """

        ymd_type = type(idate)
        if ymd_type == int:
            return udc.as_parts(idate, fmt=self.options['fmt'], yy_pivot=self.options['yy_pivot'])
        if ymd_type in [datetime, date]:
            return self._idate_to_parts(int(idate.strftime('%Y%m%d')))
        if ymd_type == float or (ymd_type == str and idate.isdigit()):
            return self._idate_to_parts(int(idate))
        return None

    # ---
    # Public methods

    def add_days(self, days: int) -> Undated:
        """
        Adds months to the date
        :param days: int, the days to add, use negative days to subtract
        :return: int, if inplace is false
        """

        return Undated(add_days(super(), days))

    # ---

    def add_months(self, months: int, period_end: bool = False) -> Undated:
        """
        Adds months to the date
        :param months: int, the months to add, use negative months to subtract
        :param period_end: bool, takes the previous day. EG: For last day of a period
        :return: int, if inplace is false
        """

        ymd = add_months(super(), months)
        if period_end:
            ymd = add_days(super(), (1 if months < 0 else -1))
        return Undated(ymd)

    # ---

    def add_weekdays(self, weekdays: int) -> Undated:
        """
        Adds months to the date
        :param weekdays: int, the days to add, use negative days to subtract
        :return: int, if inplace is false
        """

        return Undated(add_weekdays(super(), weekdays))

    # ---

    def add_years(self, years: int, period_end: bool = False) -> Undated:
        """
        Adds years to the date
        :param years: int, the years to add, use negative years to subtract
        :param period_end: bool, takes the previous day. EG: For last day of a period
        """

        return self.add_months(years * 12, period_end=period_end)

    # ---

    def as_type(self) -> Union[date, datetime, float, int, str, None]:
        """
        Converts ymd back to the initial type and format.
        :return: The ymd value in the initial type and format
        """

        idate_type = type(self.idate)
        if idate_type in [float, int, str]:
            return idate_type(self.iymd // (100 if self.options['fmt'] == 'Ym' else 1))
        if idate_type == type(None):  # noqa, ide advises isinstance but it can't with NoneType
            return None
        dtt = datetime.strptime(str(self.iymd), '%Y%m%d')
        return dtt if idate_type == datetime else dtt.date()

    # ---

    def day_of_week(self) -> int:
        """
        Calculates the number for day of the week. Sunday = 0, Monday = 1...
        :return: int, the day number 0 to 6
        """

        return udc.day_of_week(self._get_property(udc.EPOCH))

    # ---

    def is_leap_year(self) -> bool:
        """
        Calculates if the year a leap year
        :return: bool, true when it is a leap year
        """

        return bool(udc.is_leap_year(self.year))

    # ---

    def is_weekday(self) -> bool:
        """
        Calculates if the date is a weekday, Monday - Friday
        :return: bool, true when it is a weekday
        """

        return bool(self.day_of_week() < 5)


# -----------------------------------------------


def add_days(ymd: YMD, days: int) -> YMD:
    """
    Adds a number of days to a date in in Ymd format
    :param ymd: YMD class
    :param days: int, the number of days to add
    :return: YMD class
    """

    return epoch_to_ymd(ymd.epoch() + days)


# -----------------------------------------------


def add_months(ymd: YMD, months: int) -> YMD:
    """
    Adds given months to a date. Use negative months to subtract months
    :param ymd: YMD class
    :param months: int, the number of months
    :return: YMD class
    """

    return YMD(*udc.add_months(ymd.year, ymd.month, ymd.day, months), trusted=True)


# -----------------------------------------------


def add_weekdays(ymd: YMD, weekdays: int) -> YMD:
    """
    Adds a number of weekdays, monday to friday, to a date in in Ymd format
    :param ymd: YMD class
    :param weekdays: int, the number of days to add
    :return: YMD class
    """

    return YMD(
        *udc.add_weekdays(ymd.epoch(), weekdays),
        trusted=True
    )


# -----------------------------------------------


def days_between(from_ymd: YMD, to_ymd: YMD) -> int:
    """
    Calculates the days between two dates
    :param from_ymd: YMD, the from date YMD class
    :param to_ymd: YMD, the to date YMD class
    :return: int, the days between the dates
    """

    return to_ymd.epoch() - from_ymd.epoch()


# -----------------------------------------------


def epoch_to_ymd(epoch: int) -> YMD:
    """
    Converts the epoch day number to a YMD class
    :param epoch: int, the epoch value
    :return: YMD class
    """

    return YMD(*udc.epoch_to_parts(epoch), trusted=True)


# -----------------------------------------------


def months_between(from_ymd: YMD, to_ymd: YMD) -> int:
    """
    Calculates the complete months between two dates
    :param from_ymd: YMD class
    :param to_ymd: YMD class
    :return: int, the complete months between the dates
    """

    if from_ymd.iymd < to_ymd.iymd:
        ymd1 = from_ymd
        ymd2 = to_ymd
        pos_neg = 1
    else:
        ymd1 = to_ymd
        ymd2 = from_ymd
        pos_neg = -1

    # ---

    if ymd2.day == udc.DAYS_IN_MONTH[udc.is_leap_year(ymd2.year)][ymd2.month]:
        day_factor = 0
    else:
        day_factor = 1 if ymd2.day < ymd1.day else 0

    # ---

    return (((ymd2.year - ymd1.year) * 12) + ymd2.month - ymd1.month - day_factor) * pos_neg


# -----------------------------------------------


def quarter(ymd: YMD, to_str: bool = True) -> Union[int, str]:
    """
    Calculates the quarter from a year, returning the quarter end month, or quarter number
    :param ymd: YMD class
    :param to_str: bool, true returns 2021Q3, otherwise 202103 format
    :return: str 2021Q1, 2021Q2, 2021Q3, 2021Q4; or int 202103, 202106, 202109, 202112
    """

    return udc.quarter(ymd.year, ymd.month, to_str)


# -----------------------------------------------


def weekdays_between(from_ymd: YMD, to_ymd: YMD, inclusive: bool = False) -> int:
    """
    Calculates the number of weekdays between two dates
    :param from_ymd: YMD class
    :param to_ymd: YMD class
    :param inclusive: bool, whether to include the to date as a completed day
    :return: int, the number of days between the dates
    """

    return udc.weekdays_between_epochs(
        from_ymd.epoch(),
        to_ymd.epoch(),
        inclusive
    )


# -----------------------------------------------
# End.
