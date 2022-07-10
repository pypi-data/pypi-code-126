from datetime import datetime, time
import pytz


# TODO: Convert this to use a locale for user
def localise_tz(type_, obj):
    tz = pytz.timezone("UTC")

    if type_ == "environment":
        tz_time = tz.localize(obj.created)
        obj.created = tz_time.astimezone(tz=pytz.timezone("Europe/London"))
    elif type_ == "reading":
        tz_time = tz.localize(obj.time)
        obj.time = tz_time.astimezone(tz=pytz.timezone("Europe/London"))
    return obj


def convert_dt_to_iso(data):
    for k, v in data.items():
        if isinstance(v, datetime) or isinstance(v, time):
            data[k] = v.isoformat()
    return data
