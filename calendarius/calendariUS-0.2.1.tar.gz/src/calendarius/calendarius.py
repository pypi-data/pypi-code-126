import argparse
import datetime
import logging
import random
import calendar
import copy

from collections import OrderedDict

from dateutil.rrule import rrule, WEEKLY, MO

from .people import People
from .calendarius_utils import (
    fmt_day,
    _date,
    logger,
    weekday_name,
    create_ics,
    statistics,
)


def calendarius(start, end, people, randomize):
    logger.debug(f"start date: {start}")
    logger.debug(f"end date: {end}")
    logger.debug(f"people: {', '.join(people)}")

    # shuffle people
    if randomize:
        random.shuffle(people)

    logger.debug(f"people: {', '.join(people)}")

    p = People(people)

    if start.weekday() == 0:
        monday = start
    else:
        monday = start + datetime.timedelta(days=-7)

    logger.debug(f"adjust start date: {monday.date()}")

    d = OrderedDict()
    for date in rrule(WEEKLY, byweekday=MO, dtstart=monday, until=end):

        d[date.date()] = p.get_monday()

        logger.debug(f"date: {date.date()} {weekday_name(date)}")

        for i in range(1, 5):
            day = date + datetime.timedelta(days=i)
            d[day.date()] = p.get()

            logger.debug(f"date: {day.date()} {weekday_name(day)}")

    # exclude day before start date
    dstrict = OrderedDict()
    for i in d:
        if i >= start.date():
            dstrict[i] = d[i]

    return dstrict


def main():

    parser = argparse.ArgumentParser(
        prog="calendarius",
        description=__doc__,
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument("--version", action="version", version="0.2.1", help="version")

    parser.add_argument(
        "-v", "--verbose", action="count", default=0, help="increase verbosity"
    )

    parser.add_argument(
        "-s",
        "--start-date",
        type=_date,
        default=datetime.datetime(1970, 1, 1).strftime(fmt_day),
        metavar="YYYY-MM-DD",
        help="start date YYYY-MM-DD",
    )

    parser.add_argument(
        "-e",
        "--end-date",
        type=_date,
        default=datetime.datetime.now().strftime(fmt_day),
        metavar="YYYY-MM-DD",
        help="end date YYYY-MM-DD",
    )

    parser.add_argument(
        "-i",
        "--ics-file",
        default=None,
        help="ics file for calendar",
    )

    parser.add_argument(
        "--random",
        action="store_true",
        help="randomize list of people. (default %(default)s)",
    )

    parser.add_argument(
        "-S",
        "--stats",
        action="store_true",
        help="statistics on shifts. (default %(default)s)",
    )

    parser.add_argument(
        "-q",
        "--silent",
        action="store_true",
        help="silent mode. (default %(default)s)",
    )

    # Positional parameters
    parser.add_argument("people", default=[], nargs="+", help="list of people")

    args = parser.parse_args()

    if args.verbose:
        logger.setLevel(logging.DEBUG)

    logger.debug(args)

    d = calendarius(args.start_date, args.end_date, args.people, args.random)

    if not args.silent:
        for i in d:
            if i < args.start_date.date():
                continue
            print(f"{i} {weekday_name(i)[:3]} : {', '.join(d[i])}")

    if args.ics_file is not None:

        cal = create_ics(d)

        with open(args.ics_file, "w") as f:
            f.writelines(cal.serialize_iter())

    if args.stats:
        statistics(d)


if __name__ == "__main__":
    main()
