"""CLint command line interface."""
from typing import TextIO

import click

import clint

from .exceptions import HookException
from .hook_handler import HookHandler
from .runner import Runner


class Command:
    """Command class for CLI arguments parsing."""

    @staticmethod
    @click.command(no_args_is_help=True)
    @click.argument("message", type=click.STRING, required=False)
    @click.option(
        "-f",
        "--file",
        type=click.File(),
        help="File path containing the commit message.",
    )
    @click.option(
        "--enable-hook/--disable-hook",
        default=None,
        help="Enable/Disable CLint as a handler for git 'commit-msg' hook.",
    )
    @click.version_option(clint.__version__)
    def entrypoint(
        message: click.STRING,
        file: TextIO,
        enable_hook: click.BOOL,
    ):
        """CLint: A Conventional Commits Linter for your shell."""
        if enable_hook is not None:
            try:
                handler = HookHandler()
            except HookException as exception:
                result = str(exception)
            else:
                if enable_hook:
                    result = handler.enable()
                else:
                    result = handler.disable()
            Command.show_result(result=result)
            return
        result = None
        if message:
            result = Runner.validate(message=message)
        if file:
            result = Runner.validate(message=file.read())
        Command.show_result(result=result)

    @staticmethod
    def show_result(result: str):
        """Print result values to the user."""
        click.echo(result)
