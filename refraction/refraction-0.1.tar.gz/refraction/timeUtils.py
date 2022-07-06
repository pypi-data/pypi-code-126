"""
Functions for dealing with time.
"""

import datetime, dateutil.tz

#-----------#
# Constants #
#-----------#

TS_FORMAT_NO_TZ = "%Y-%m-%d %H:%M:%S"
"""
The time format without a timezone (for parsing attempts).
"""

TS_FORMAT = TS_FORMAT_NO_TZ + " %z"
"""
The time format string for timestamps. Note that apparently %Z can parse
a time zone but will still result in a time-zone-naive object, which we
don't want...
"""

UTC = dateutil.tz.tzutc()
"""
A tzinfo object from `dateutil.tz` representing Universal Time,
Coordinated.
"""


#-----------#
# Functions #
#-----------#

def now():
    """
    Returns a time-zone-aware datetime representing the current time.
    """
    return datetime.datetime.now(UTC)


def timeString(when=None):
    """
    Returns a timestamp string based on the current time, or a specified
    datetime object. Timezone is assumed to be UTC.
    """
    if when is None:
        when = now()

    if when.tzinfo is None:
        when = when.replace(tzinfo=UTC)
    else:
        when = when.astimezone(UTC)

    return when.strftime(TS_FORMAT)


def timeFromTimeString(timeString):
    """
    Converts a time string back into a time-zone-aware datetime
    object.
    """
    try:
        result = datetime.datetime.strptime(timeString, TS_FORMAT)
        result = result.astimezone(UTC)
        print("A", result, result.tzinfo)
    except ValueError:
        result = datetime.datetime.strptime(timeString, TS_FORMAT_NO_TZ)
        result = result.replace(tzinfo=UTC)
        print("B", result)
    return result


def timeFromTimestamp(timestamp):
    """
    Returns a timezone-free `time.struct_time` object representing the
    time encoded in the given timestamp.
    """
    result = datetime.datetime.fromtimestamp(timestamp)
    if result.tzinfo is None:
        result = result.replace(tzinfo=UTC)
    else:
        result = result.astimezone(UTC)
    return result


def describeTime(when):
    """
    Formats a datetime using 24-hour notation w/ extra a.m./p.m.
    annotations in the morning for clarity, and a timezone attached.
    """
    # Use a.m. for extra clarity when hour < 12, and p.m. for 12:XX
    am_hint = ''
    if when.hour < 12:
        am_hint = ' a.m.'
    elif when.hour == 12:
        am_hint = ' p.m.'

    tz = when.strftime("%Z")
    if tz != '':
        tz = ' ' + tz
    return when.strftime("%H:%M{}{} on %Y-%m-%d".format(am_hint, tz))


def toDatetime(timeData):
    """
    Converts any kind of time data (time string, floating-point
    timestamp, or `datetime.datetime` object) into a `datetime.datetime`
    object. Strings must match the format used by `timeString`.
    """
    if isinstance(timeData, datetime.datetime):
        return timeData
    elif isinstance(timeData, str):
        return timeFromTimeString(timeData)
    elif isinstance(timeData, (int, float)):
        return timeFromTimestamp(timeData)
    else:
        raise TypeError(
            "Cannot convert from {} to a datetime object.".format(
                type(timeData)
            )
        )
