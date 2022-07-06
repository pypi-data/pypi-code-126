"""CLint command line interface."""

import click

from . import validator


class CLI:
    """CLI class for command line interface definition."""

    @staticmethod
    def validate_commit_message(message: str) -> None:
        """Validate commit message."""
        try:
            commit = validator.Commit.generate(msg=message)
            commit.validate()
        except validator.GenerationException as exc:
            click.echo(f"Parsing error: {exc}")
        except validator.ValidationException as exc:
            click.echo(f"Validation error: {exc}")
        else:
            click.echo("Your commit message is CC compliant!")

    @staticmethod
    @click.command()
    @click.argument("message", type=click.STRING)
    def entrypoint(message):
        """CLint: A Conventional Commits Linter for your shell."""
        CLI.validate_commit_message(message=message)
