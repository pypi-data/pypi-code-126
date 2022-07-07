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


def statistics(d):

    # get list of names
    p = set()
    for day in d:
        for i in d[day]:
            p.add(i)
    p = sorted(list(p))

    # count shift number
    stats = {"monday": {}, "other": {}}
    for i in p:
        stats["monday"].setdefault(i, 0)
        stats["other"].setdefault(i, 0)

    for day in d:
        if day.weekday() == 0:
            key = "monday"
        else:
            key = "other"
        for i in d[day]:
            stats[key][i] += 1

    print(f"{'Name':25s} Mon. NoMon.")
    for i in p:
        print(f"{i:.<25s} {stats['monday'][i]:3d}   {stats['other'][i]:4d}")
