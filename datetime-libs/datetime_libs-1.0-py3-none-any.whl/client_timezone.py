def get_client_timezone(tz=''):
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
