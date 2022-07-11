import typer
from typer import Option, Argument, Context, echo, progressbar, BadParameter
from typing import Optional
from datetime import datetime, timedelta

app = typer.Typer(
    short_help="Oracle sub-command to calculate the travel time",
    help="Oracle sub-command to calculate the travel time"
)

DEFAULT_FORMATS = [
    '%Y-%m-%d',
    '%Y-%m-%dT%H:%M:%S',
    '%Y-%m-%d %H:%M:%S',
    '%d %H:%M',
    '%H:%M',
    '%H',
]


def _set_current_year(ctx: Context, t: datetime):
    if ctx.resilient_parsing:
        return t
    if t is None:
        raise BadParameter("No date given")
    if t.year == 1900:
        now = datetime.now()
        t = datetime(
            now.year,
            now.month,
            now.day,
            t.hour,
            t.minute,
            t.second,
        )

    return t


def _set_current_year_(ctx: Context, t: datetime):
    if ctx.resilient_parsing:
        return t
    if t.year == 1900:
        now = datetime.now()
        t = datetime(
            now.year,
            now.month if t.month == 1 else t.month,
            now.day if t.day == 1 else t.day,
            t.hour,
            t.minute,
            t.second,
        )

    return t


@app.command(
    "timedelta",
    help="Show timedelta between two dates",
)
def timedelta_(
        hours: int = Option(
            default=0,
        ),
        minutes: int = Option(
            0,
            "--minutes",
            "-m",
            envvar="TIMECLI_ORACLE_TIMEDELTA_MINUTES",
        ),
        from_date: Optional[datetime] = Option(
            datetime.now(),
            "--from-date",
            "-f",
            callback=_set_current_year,
            formats=DEFAULT_FORMATS,
            envvar="TIMECLI_ORACLE_TIMEDELTA_CURRENT_TIME",
        ),
        time_format: Optional[str] = Option(
            '%Y-%m-%dT%H:%M:%S',
            "--time-format",
            "-t",
            envvar="TIMECLI_ORACLE_TIMEDELTA_TIME_FORMAT",
        ),
        only_date: bool = Option(
            False,
            "--only-date",
            "-od",
            is_flag=True,
            envvar="TIMECLI_ORACLE_TIMEDELTA_ONLY_DATE",
        )
):
    calculated_time = from_date + timedelta(
        hours=hours,
        minutes=minutes,
    )
    if only_date:
        echo(calculated_time.strftime(time_format))
        return
    echo(f"Time is {calculated_time.strftime(time_format)}")


@app.command(
    "diff",
    help="Show diff between two dates",
)
def diff(
        from_date: datetime = Argument(
            formats=DEFAULT_FORMATS,
            default=None,
            callback=_set_current_year_,
        ),
        to_date: datetime = Argument(
            formats=DEFAULT_FORMATS,
            default=None,
            callback=_set_current_year_,
        ),
        lunch: int = Option(
            0,
            "--lunch",
            "-l",
            envvar="TIMECLI_ORACLE_DIFF_LUNCH",
        ),
        hours: bool = Option(
            False,
            "--hours",
            "-h",
            is_flag=True,
            envvar="TIMECLI_ORACLE_DIFF_HOURS",
        ),
        minutes: bool = Option(
            False,
            "--minutes",
            "-m",
            is_flag=True,
            envvar="TIMECLI_ORACLE_DIFF_MINUTES",
        )
):
    d = (to_date - from_date) - timedelta(hours=lunch)
    if hours:
        echo(int(d.seconds / 3600))
    elif minutes:
        echo(int(d.seconds / 60))
    else:
        echo(d)


@app.command(
    "progress",
    help="Show progress bar between two dates",
    short_help="Show progress bar between two dates",
)
def progress(
        from_date: datetime = Argument(
            formats=DEFAULT_FORMATS,
            default=None,
            callback=_set_current_year_,
        ),
        to_date: datetime = Argument(
            formats=DEFAULT_FORMATS,
            default=None,
            callback=_set_current_year_,
        ),
        current_time: datetime = Option(
            datetime.now(),
            "--current-time",
            "-c",
            formats=DEFAULT_FORMATS,
            callback=_set_current_year_,
            envvar="TIMECLI_ORACLE_PROGRESS_CURRENT_TIME",
        ),
        template: str = Option(
            "Total time passed percent -> {percent}%\n"
                    "Total diff -> {time_diff}"
            "--template",
            "-t",
            envvar="TIMECLI_ORACLE_PROGRESS_TEMPLATE",
        ),
        bar: bool = Option(
            True,
            is_flag=True,
            envvar="TIMECLI_ORACLE_PROGRESS_BAR",
        )
):
    from_ts = from_date.timestamp()
    to_ts = to_date.timestamp()

    percent = round(((current_time.timestamp() - from_ts) * 100) / (to_ts - from_ts), 2)
    time_diff = to_date - current_time

    if current_time.timestamp() > to_ts:
        raise BadParameter("--current-time shouldn't be greater than [TO_DATE]")

    if from_date.timestamp() > current_time.timestamp():
        raise BadParameter("[FROM_DATE] shouldn't bea greater than --current-time")

    echo(template.format(
        percent=percent,
        time_diff=time_diff,
    ))
    if not bar:
        return
    with progressbar(range(10000), bar_template="[%(bar)s]  %(info)s") as progress_bar:
        limit = "{:.2f}".format(percent).replace(".", "")
        limit = int(limit)
        for point in progress_bar:
            if limit == point:
                break
