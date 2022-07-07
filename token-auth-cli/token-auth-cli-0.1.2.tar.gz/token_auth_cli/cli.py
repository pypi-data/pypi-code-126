import logging

import rich
import click

from .config import Settings, App
from . import utils, commands

logger = logging.getLogger(__name__)


@click.group()
@click.option("--verbose/--no-verbose",
              help="Show additional information")
@click.option("-d", "--debug/--no-debug",
              help="Show debug information")
@click.option("--api", type=str,
              help="API url.")
@click.option("--api-get-token", type=str,
              help="API url to use when trying to get token.")
@click.option("--api-get", type=str,
              help="API url to check if token valid.")
@click.option("--config", type=click.Path(),
              help="Config file.")
@click.pass_context
def cli_commands(context, **kwargs):
    """CLI commands."""
    filtered = utils.filter_none(kwargs)
    settings = Settings(**filtered)
    rich.inspect(settings)
    if not click.confirm("Are these settings correct?", default=False):
        raise click.Abort
    app = App(settings=settings)
    context.obj = app


@cli_commands.command("get")
@click.option("--username", prompt="Username")
@click.password_option("--password", prompt="Password")
@click.pass_context
def get_token(*args, **kwargs):
    """Get token."""
    return utils.run_async_command(commands.get_token, *args, **kwargs)


def main():
    """Main function"""
    cli_commands()  # pylint: disable=no-value-for-parameter


if __name__ == "__main__":
    main()
