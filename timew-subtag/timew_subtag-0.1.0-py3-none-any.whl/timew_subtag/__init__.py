__version__ = '0.1.0'

import sys
from timew import TimeWarrior
from rich import pretty, print
import click
import arrow
from datetime import timedelta

timew = TimeWarrior()
pretty.install()

def first_of_this_year():
    return arrow.now().floor("year")

def last_of_this_year():
    return arrow.now().ceil("year")

def first_of_this_month():
    return arrow.now().floor("month")

def last_of_this_month():
    return arrow.now().ceil("month")

def first_of_last_month():
    return arrow.now().shift(months=-1).floor("month")

def last_of_last_month():
    return arrow.now().shift(months=-1).ceil("month")

def seconds_to_hh_mm_ss(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)

    if seconds >= 3600:
        return f"{h:d} hours {m:02d} minutes {s:02d} seconds"
    else:
        return f"{m:d} minutes {s:02d} seconds"

def month_parser(start, end, subtag):
    log = timew.list(start, end)
    duration = timedelta(0)
    for i in log:
        if any(
            s[:len(subtag)] == subtag
            for s in i["tags"]
            ):
            duration += arrow.get(i["end"]) - arrow.get(i["start"])
    return seconds_to_hh_mm_ss(int(duration.total_seconds()))

@click.command()
@click.argument("subtag")
@click.option(":month", default=False, is_flag=True)
@click.option(":lastmonth", default=False, is_flag=True)
@click.option(":year", default=False, is_flag=True)
def cli(subtag, month, lastmonth, year):
    if month:
        print(month_parser(first_of_this_month(), last_of_this_month(), subtag))
    elif lastmonth:
        print(month_parser(first_of_last_month(), last_of_last_month(), subtag))
    elif year:
        print(month_parser(first_of_this_year(), last_of_this_year(), subtag))
    else:
        print(month_parser(arrow.Arrow.fromtimestamp(1), arrow.now(), subtag))
