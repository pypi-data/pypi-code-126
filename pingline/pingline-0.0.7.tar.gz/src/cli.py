#!python3

import click
import os

from .recorder import Recorder
from .plotter import plot, plot_interactive


@click.group()
def cli():
    pass


@click.command(help="Record ping data for router and an internet host")
@click.option("--interval", default=1, help="Pause for _ seconds before pinging again")
@click.option("--router-host", default="192.168.10.1")
@click.option("--internet-host", default="google.com")
@click.option("--log-file", default="ping_log.csv")
def recorder(interval, router_host, internet_host, log_file):
    recorder_ = Recorder(
        interval,
        {"router": router_host, "internet": internet_host},
        log_file,
    )
    click.echo("Starting recorder, press Ctrl+C to finish")
    try:
        recorder_.start()
    except KeyboardInterrupt:
        click.echo("Finishing recorder")


@click.command(help="Explore recorded ping data")
@click.option("--interval", default=1, help="How often to refresh in interactive mode")
@click.option(
    "--last-n-minutes", default=2, help="How much data to show in interactive mode"
)
@click.option("--log-file", default="ping_log.csv")
@click.option("--interactive", is_flag=True, help="Auto refresh the graph?")
def plotter(interval, last_n_minutes, log_file, interactive):
    click.echo("Starting plotter, press Ctrl+C to finish")
    try:
        if interactive:
            plot_interactive(interval, last_n_minutes, log_file)
        else:
            plot(log_file)
    except KeyboardInterrupt:
        click.echo("Finishing plotter")


@click.command(help="Permanently remove the log file with recording data")
@click.option("--log-file", default="ping_log.csv")
def cleanup(log_file):
    os.remove(log_file)
    click.echo(f"Removed {log_file}")


cli.add_command(recorder)
cli.add_command(plotter)
cli.add_command(cleanup)

if __name__ == "__main__":
    cli()
