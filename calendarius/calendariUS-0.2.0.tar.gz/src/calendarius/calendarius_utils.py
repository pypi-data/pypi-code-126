import logging
import datetime
import calendar

from ics import Calendar, Event


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


def create_ics(d):

    c = Calendar()

    for day in d.keys():

        p1 = d[day][0]
        p2 = d[day][1]

        morning = Event(
            begin=f"{day} 07:00:00",
            duration=datetime.timedelta(hours=4),
            name=f"{p1}",
            attendees=[p1],
        )
        afternoon = Event(
            begin=f"{day} 12:00:00",
            duration=datetime.timedelta(hours=4),
            name=f"{p2}",
            attendees=[p2],
        )

        logger.debug(morning)
        logger.debug(afternoon)

        c.events.add(morning)
        c.events.add(afternoon)

    return c
