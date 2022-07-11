import click
from eliot import start_task

from .file_management import initialize_build_directory, start_log

__version__ = "0.3.2"


@click.command()
@click.version_option(version=__version__)
def cli():
    start_log()
    with start_task(action_type="MonkeytaleBuild") as task:
        initialize_build_directory()


if __name__ == "__main__":
    cli()  # pragma: no cover
