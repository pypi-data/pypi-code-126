import typer
from datetime import datetime, timedelta
from timecli.commands import oracle

app = typer.Typer(
    name="pomodoro",
    help="Pomodoro helper",
)


@app.command(
    "timedelta",
)
def timedelta_(
        tomatos: float,
        duration: int = typer.Option(
            25,
            "--duration",
            "-d",
            help="Duration of a pomodoro",
            min=5,
            max=120,
            envvar="TIMECLI_POMODORO_DURATION",
        ),
        _break_duration: int = typer.Option(
            5,
            "--break-duration",
            "-b",
            min=1,
            max=120,
            envvar="TIMECLI_POMODORO_BREAK_DURATION",
        ),
        long_break_duration: int = typer.Option(
            15,
            "--long-break-duration",
            "--lb",
            min=1,
            max=120,
            envvar="TIMECLI_LONG_BREAK_DURATION",
        ),
        long_break_after: int = typer.Option(
            4,
            "--long-break-after",
            "--la",
            min=1,
            max=120,
            envvar="POMODORO_LONG_BREAK_AFTER",
        ),
        current_time: datetime = typer.Option(
            datetime.now(),
            "--current-time",
            "-ct",
            callback=oracle._set_current_year_,
            formats=oracle.DEFAULT_FORMATS,
            envvar="TIME_CLI_CURRENT_TIME",
        ),
        with_break: bool = typer.Option(
            False,
            "--with-break",
            "--wb",
            "-wb",
            is_flag=True,
            envvar="TIMECLI_POMODORO_WITH_BREAK",
        ),
        only_break: bool = typer.Option(
            False,
            "--only-break",
            "--ob",
            "-ob",
            is_flag=True,
            envvar="TIMECLI_POMODORO_ONLY_BREAK",
        ),
):
    local_time = current_time
    break_time = current_time
    for tomato in range(int(tomatos)):
        if (tomato + 1) % long_break_after == 0 and tomato != 0:
            break_duration = long_break_duration
        else:
            break_duration = _break_duration
        if tomato != int(tomatos) - 1 and with_break:
            local_time += timedelta(minutes=break_duration)
            break_time += timedelta(minutes=break_duration)
        local_time += timedelta(minutes=duration)

    if only_break:
        typer.echo(local_time - break_time, color=True)
        return
    typer.echo(local_time - current_time, color=True)
