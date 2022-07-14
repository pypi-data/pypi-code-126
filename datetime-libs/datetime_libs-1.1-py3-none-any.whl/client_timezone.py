def get_client_timezone(tz: str = '') -> str:
    import pytz

    default_ctz = "UTC"
    if tz:
        client_timezone = tz
    else:
        client_timezone = default_ctz

    if client_timezone:
        if client_timezone not in pytz.all_timezones:
            client_timezone = default_ctz
    else:
        client_timezone = default_ctz
    return client_timezone


def add_one(num_1: float = 0, num_2: float = 0) -> float:
    return num_1 + num_2
