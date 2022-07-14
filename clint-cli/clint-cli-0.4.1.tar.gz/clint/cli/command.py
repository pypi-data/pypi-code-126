"""CLint command line interface."""
import sys
from typing import TextIO

import click

import clint

from ..result import Result
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
        result: Result = None
        if enable_hook is None:
            if message:
                result = Runner.validate(message=message)
            elif file:
                result = Runner.validate(message=file.read())
        else:
            result = Runner.change_hook_handler(is_enabling=enable_hook)
        Command.show_result(result=result)
        sys.exit(result.return_code)

    @staticmethod
    def show_result(result: Result):
        """Print result values to the user."""
        for action, message in result.actions.items():
            click.echo(f"{action}: {message}")
