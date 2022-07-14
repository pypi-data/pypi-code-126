def get_datetime_and_timestamp():
    """
    Get datetime and timestamp
    :return: datetime and timestamp
    """
    from datetime import datetime
    curr_date = datetime.utcnow()
    dt_ts = {'datetime': curr_date, 'timestamp': curr_date.timestamp()}
    return dt_ts


def get_next_prev_datetime_and_timestamp(**kwargs):
    """
    Get datetime and timestamp after added/subtracted days/weeks/hours/minutes in current datetime
    :return: datetime and timestamp
    """
    from datetime import datetime, timedelta
    days = kwargs.get('days', 0)
    weeks = kwargs.get('weeks', 0)
    hours = kwargs.get('hours', 0)
    minutes = kwargs.get('minutes', 0)
    seconds = kwargs.get('seconds', 0)
    curr_date = datetime.utcnow()
    next_prev_dt_ts = curr_date + timedelta(
        days=days,
        weeks=weeks,
        hours=hours,
        minutes=minutes,
        seconds=seconds
    )
    dt_ts = {
        'datetime': next_prev_dt_ts,
        'timestamp': next_prev_dt_ts.timestamp()
    }
    return dt_ts


def get_timestamp():
    """
    Get current timestamp
    :return: timestamp
    """
    from datetime import datetime
    return datetime.utcnow().timestamp()


def get_datetime():
    """
    Get current datetime
    print(get_datetime())
    2021-05-16 21:43:00.203057
    :return: datetime
    """
    from datetime import datetime
    date_time = datetime.utcnow()
    return date_time


def get_next_prev_timestamp(**kwargs):
    """
    Get timestamp after added/subtracted days/weeks/hours/minutes in current datetime
    :return: timestamp
    """
    from datetime import datetime, timedelta
    days = kwargs.get('days', 0)
    weeks = kwargs.get('weeks', 0)
    hours = kwargs.get('hours', 0)
    minutes = kwargs.get('minutes', 0)
    seconds = kwargs.get('seconds', 0)

    next_prev_timestamp = datetime.utcnow() + timedelta(
        days=days,
        weeks=weeks,
        hours=hours,
        minutes=minutes,
        seconds=seconds
    )
    return next_prev_timestamp.timestamp()


def get_next_prev_datetime(**kwargs):
    """
    Get datetime after added/subtracted days/weeks/hours/minutes in current datetime
    :return: datetime
    """
    from datetime import datetime, timedelta
    days = kwargs.get('days', 0)
    weeks = kwargs.get('weeks', 0)
    hours = kwargs.get('hours', 0)
    minutes = kwargs.get('minutes', 0)
    seconds = kwargs.get('seconds', 0)

    next_prev_datetime = datetime.utcnow() + timedelta(
        days=days,
        weeks=weeks,
        hours=hours,
        minutes=minutes,
        seconds=seconds
    )
    return next_prev_datetime


def get_timestamp_to_datetime(timestamp):
    """
    Get timestamp to date
    timestamp = 1547281745
    print(get_timestamp_to_datetime(timestamp))
    2021-07-12 00:00:00
    :return: datetime
    """
    try:
        import time
        from datetime import timezone, datetime
        datetime_from_ts = datetime.fromtimestamp(timestamp)
        return datetime_from_ts
    except Exception as e:
        print('Error get_timestamp_to_datetime: ', str(e))
        raise Exception("Invalid date for date format")
        # return ''


def date_string_to_datetime_and_timestamp(date_str: str, date_format: str, time_part: bool = True, tz=None):
    """
    Convert date to timestamp, if invalid date_str or date_format, it will return 0 (zero) as timestamp

    date_format = "%d/%m/%Y %H:%M:%S"

    Directive	Description	Example

    %a	Weekday, short version	Wed

    %A	Weekday, full version	Wednesday

    %w	Weekday as a number 0-6, 0 is Sunday	3

    %d	Day of month 01-31	31

    %b	Month name, short version	Dec

    %B	Month name, full version	December

    %m	Month as a number 01-12	12

    %y	Year, short version, without century	18

    %Y	Year, full version	2018

    %H	Hour 00-23	17

    %I	Hour 00-12	05

    %p	AM/PM	PM

    %M	Minute 00-59	41

    %S	Second 00-59	08

    %f	Microsecond 000000-999999	548513

    %z	UTC offset	+0100

    %Z	Timezone	CST

    %j	Day number of year 001-366	365

    %U	Week number of year, Sunday as the first day of week, 00-53	52

    %W	Week number of year, Monday as the first day of week, 00-53	52

    %c	Local version of date and time	Mon Dec 31 17:41:00 2018

    %x	Local version of date	12/31/18

    %X	Local version of time	17:41:00

    %%	A % character	%

    %G	ISO 8601 year	2018

    %u	ISO 8601 weekday (1-7)	1

    %V	ISO 8601 week number (01-53)	01

    :param date_str: str
    :param date_format: str
    :param time_part: bool
    :param tz: bool
    :return: int
    """
    try:
        from datetime import datetime, time, timezone
        from backports.zoneinfo import ZoneInfo
        from .client_timezone import get_client_timezone
        import pytz

        ctz = get_client_timezone(tz=tz)
        local_dt = datetime.strptime(
            date_str, date_format).replace(tzinfo=ZoneInfo(ctz))
        # local_dt = datetime.strptime(date_str, date_format)
        if time_part is True:
            date_time_part = time.max
            local_dt = datetime.combine(local_dt, date_time_part)

        local_dt = local_dt.astimezone(pytz.timezone(ctz))
        dt_utc = local_dt.astimezone(pytz.UTC)
        # dt_utc = local_dt.astimezone()
        dt_ts = {'datetime': dt_utc, 'timestamp': dt_utc.timestamp()}
        return dt_ts
    except Exception as e:
        error_msg = f"Invalid date: {str(e)}"
        print(error_msg)
        raise Exception(error_msg)
        # dt_ts = {'datetime': 0, 'timestamp': 0}
        # return dt_ts


def validate_date_format(date_str, format_str="%Y-%m-%d"):
    from datetime import datetime
    try:
        if date_str == datetime.strptime(date_str, format_str).strftime(format_str):
            return True
        return False
    except ValueError:
        return False


def start_datetime_timestamp(**kwargs):
    try:
        from datetime import datetime, time, timezone
        from backports.zoneinfo import ZoneInfo
        from .client_timezone import get_client_timezone
        import pytz

        date_str = str(kwargs.get("date_str", str(get_datetime())[:10]))
        format_str = kwargs.get("format_str", "%Y-%m-%d")
        tz = kwargs.get("tz", "")
        ctz = get_client_timezone(tz=tz)
        # local_dt = datetime.strptime(date_str, format_str)
        local_dt = datetime.strptime(
            date_str, format_str).replace(tzinfo=ZoneInfo(ctz))
        date_time_part = time.min
        local_dt = datetime.combine(local_dt, date_time_part)
        local_dt = local_dt.astimezone(pytz.timezone(ctz))
        dt_utc = local_dt.astimezone(pytz.UTC)
        dt_ts = {'datetime': dt_utc, 'timestamp': dt_utc.timestamp()}
        return dt_ts
    except Exception:
        raise Exception("Invalid date for date format")
        # dt_ts = {'datetime': 0, 'timestamp': 0}
        # return dt_ts


def end_datetime_timestamp(**kwargs):
    try:
        from datetime import datetime, time, timezone
        from backports.zoneinfo import ZoneInfo
        from .client_timezone import get_client_timezone
        import pytz

        date_str = str(kwargs.get("date_str", str(get_datetime())[:10]))
        format_str = kwargs.get("format_str", "%Y-%m-%d")
        tz = kwargs.get("tz", "")
        ctz = get_client_timezone(tz=tz)
        # local_dt = datetime.strptime(date_str, format_str)
        local_dt = datetime.strptime(
            date_str, format_str).replace(tzinfo=ZoneInfo(ctz))
        date_time_part = time.max
        local_dt = datetime.combine(local_dt, date_time_part)
        local_dt = local_dt.astimezone(pytz.timezone(ctz))
        dt_utc = local_dt.astimezone(pytz.UTC)
        dt_ts = {'datetime': dt_utc, 'timestamp': dt_utc.timestamp()}
        return dt_ts
    except Exception:
        raise Exception("Invalid date for date format")
        # dt_ts = {'datetime': 0, 'timestamp': 0}
        # return dt_ts


def num_days_between_two_dates(start_date_str: str, end_date_str: str, date_format: str = '%Y%m%d') -> int:
    """
    Get number of days between two dates
    Example:
    start_date_str = '20200312'
    end_date_str = '20200411'
    date_format='%Y%m%d'
    days = num_days_between_two_dates(start_date_str, end_date_str, date_format)
    print(days)
    """
    from datetime import datetime

    try:
        start_date_obj = datetime.strptime(start_date_str, date_format).date()
        end_date_obj = datetime.strptime(end_date_str, date_format).date()
        number_of_days_obj = (end_date_obj - start_date_obj)
        number_of_days = number_of_days_obj.days
    except ValueError:
        print('ValueError', ValueError)
        number_of_days = 0
    return number_of_days
