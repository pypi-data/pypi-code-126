import logging
import os

import rich
import click
import toml

from .config import Settings, App
from . import utils, commands

logger = logging.getLogger(__name__)

_INFO_TEXT = """
token-auth-cli

Simple tool for testing token authentication during development."""


@click.group(help=_INFO_TEXT)
@click.option("--verbose/--no-verbose",
              help="Show additional information")
@click.option("--debug/--no-debug",
              help="Show debug information")
@click.option("--confirm-settings", type=bool,
              help="Confirm settings before trying to get token.")
@click.option("--show-settings", type=bool,
              help="Show settings before trying to get token.")
@click.option("--api", type=str,
              help="API url.")
@click.option("--api-get-token", type=str,
              help="API url to use when trying to get token.")
@click.option("--api-get", type=str,
              help="API url to check if token valid.")
@click.option("--config",
              type=click.Path(readable=True,
                              file_okay=True, dir_okay=False),
              default=".token_auth_cli_config.toml",
              help="Config file.")
@click.option("--store", type=bool,
              help="Store users/tokens.")
@click.option("--username", type=str)
@click.option("--password", type=str)
@click.option("--repeat/--no-repeat", default=False)
@click.option("--repeat-interval", type=float, default=3.0)
@click.pass_context
def cli_commands(context, **kwargs):
    """CLI commands."""
    config_path = kwargs["config"]
    if (os.path.isfile(config_path) and os.path.exists(config_path)):
        loaded_config = toml.load(config_path)
    else:
        loaded_config = {}
    data = loaded_config.copy()
    filtered_kwargs = utils.filter_none(kwargs)
    filtered_kwargs = utils.filter_keys(filtered_kwargs, ["config"])
    data.update(filtered_kwargs)
    if kwargs['debug'] or data['debug']:
        logging.basicConfig(level=logging.DEBUG)
        logger.debug("--debug is enabled")
    settings = Settings(**data)
    if settings.show_settings:
        rich.inspect(settings, title="Settings")
    if settings.confirm_settings:
        if not click.confirm("Are these settings correct?", default=False):
            raise click.Abort
    app = App(settings=settings, config=config_path)
    context.obj = app
    utils.show_if_debug(kwargs, loaded_config,
                        filtered_kwargs,
                        settings, app)


@cli_commands.command("login")
@click.pass_context
def login(*args, **kwargs):
    """Get token and store it."""
    return utils.run_async_command(commands.login, *args, **kwargs)


@cli_commands.command("relogin")
@click.pass_context
def relogin(*args, **kwargs):
    """Try to use stored token for authentication."""
    return utils.run_async_command(commands.relogin, *args, **kwargs)


@cli_commands.command("list")
@click.pass_context
def tokens_list(*args, **kwargs):
    """List stored users/tokens."""
    return utils.run_async_command(commands.tokens_list, *args, **kwargs)


@cli_commands.command("remove")
@click.pass_context
def tokens_remove(*args, **kwargs):
    """Remove stored user/token."""
    return utils.run_async_command(commands.tokens_remove, *args, **kwargs)


@cli_commands.command("init")
@click.pass_context
def init(*args, **kwargs):
    """Create config file and users/tokens storage."""
    return utils.run_async_command(commands.init, *args, **kwargs)


def main():
    """Main function"""
    cli_commands()  # pylint: disable=no-value-for-parameter


if __name__ == "__main__":
    main()
