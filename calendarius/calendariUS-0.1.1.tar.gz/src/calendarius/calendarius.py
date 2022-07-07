import argparse
import datetime
import logging
import random
import calendar
import copy

from collections import OrderedDict

from dateutil.rrule import rrule, WEEKLY, MO

from .people import People
from .calendarius_utils import fmt_day, _date, logger, weekday_name


def calendarius(start, end, people):
    logger.debug(f"start date: {start}")
    logger.debug(f"end date: {end}")
    logger.debug(f"people: {', '.join(people)}")

    # shuffle people
    # random.shuffle(people)
    logger.debug(f"people: {', '.join(people)}")

    p = People(people)

    if start.weekday() == 0:
        monday = start
    else:
        monday = start + datetime.timedelta(days=-7)

    d = OrderedDict()
    for date in rrule(WEEKLY, byweekday=MO, dtstart=monday, until=end):

        d[date.date()] = p.get_monday()

        logger.debug(f"date: {date.date()} {weekday_name(date)}")

        for i in range(1, 5):
            day = date + datetime.timedelta(days=i)
            d[day.date()] = p.get()

            logger.debug(f"date: {day.date()} {weekday_name(day)}")

    for i in d:
        if i < start.date():
            continue
        print(f"{i} {weekday_name(i)[:3]} : {', '.join(d[i])}")


def main():

    parser = argparse.ArgumentParser(
        prog="calendarius",
        description=__doc__,
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument("--version", action="version", version="0.1.1", help="version")

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

    # Positional parameters
    parser.add_argument("people", default=[], nargs="+", help="list of people")

    args = parser.parse_args()

    if args.verbose:
        logger.setLevel(logging.DEBUG)

    logger.debug(args)

    calendarius(args.start_date, args.end_date, args.people)


if __name__ == "__main__":
    main()
