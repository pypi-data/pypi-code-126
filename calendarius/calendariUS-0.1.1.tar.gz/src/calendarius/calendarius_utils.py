import logging
import datetime
import calendar

fmt_day = "%Y-%m-%d"


def _date(s):
    try:
        return datetime.datetime.strptime(s, fmt_day)
    except:
        raise ValueError("invalid date {}".format(s))


def get_logger(name, verbose=False):
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s - %(message)s",
        datefmt="%H:%M:%S",
    )
    logger = logging.getLogger(name)
    if verbose:
        logger.setLevel(logging.DEBUG)
    return logger


logger = get_logger(__name__)


def weekday_name(day):
    return calendar.day_name[day.weekday()]
