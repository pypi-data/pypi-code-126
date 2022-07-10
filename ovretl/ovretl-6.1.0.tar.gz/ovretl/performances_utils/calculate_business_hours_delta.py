from typing import Optional
import datetime
import numpy as np
import pandas as pd
import pytz

START_TIME_PARIS = datetime.time(9, 0)
END_TIME_PARIS = datetime.time(18, 0)
TOTAL_WORKED_HOURS = END_TIME_PARIS.hour - START_TIME_PARIS.hour


def calculate_time_difference_within_day_in_hours(date_1: datetime.time, date_2: datetime.time):
    date_1 = datetime.datetime.combine(datetime.date.today(), date_1)  # type: ignore
    date_2 = datetime.datetime.combine(datetime.date.today(), date_2)  # type: ignore
    datetime_difference = date_2 - date_1  # type: ignore
    return max(0.0, round(datetime_difference.total_seconds() / 3600, 2))


def is_weekday(date: datetime.datetime) -> bool:
    if date.isoweekday() in [6, 7]:
        return False
    return True


def calculate_business_hours_delta(date_1: Optional[datetime.datetime], date_2: Optional[datetime.datetime]):
    """
    Calculate time difference in worked hours, based on Mo-Fr, working from 9:00 to 18:00 in the Paris office
    Careful: in this function we only consider the Paris office case (to change when we'll deal with other timezones)
    :param date_1:
    :param date_2:
    :return:
    """
    if date_1 is None or date_2 is None or pd.isna(date_1) or pd.isna(date_2):
        return None
    # we need to convert the UTC times we pull from the DB into Paris time
    date_1 = pytz.timezone("UTC").localize(date_1, is_dst=None).astimezone('Europe/Paris').replace(tzinfo=None)
    date_2 = pytz.timezone("UTC").localize(date_2, is_dst=None).astimezone('Europe/Paris').replace(tzinfo=None)
    business_days_diff = np.busday_count(date_1.strftime("%Y-%m-%d"), date_2.strftime("%Y-%m-%d"))
    if business_days_diff == 0 and date_1.date() == date_2.date():
        return calculate_time_difference_within_day_in_hours(date_1.time(), date_2.time())
    if business_days_diff < 0:
        return np.nan
    if not np.is_busday(date_1.strftime("%Y-%m-%d")):
        business_days_diff += 1
    first_day_remaining_h = (
        calculate_time_difference_within_day_in_hours(date_1.time(), END_TIME_PARIS) if is_weekday(date_1) else 0
    )
    second_day_remaining_h = (
        calculate_time_difference_within_day_in_hours(START_TIME_PARIS, date_2.time()) if is_weekday(date_2) else 0
    )
    return max(0, (business_days_diff - 1)) * TOTAL_WORKED_HOURS + first_day_remaining_h + second_day_remaining_h
