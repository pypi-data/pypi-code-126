import typer

from benchling_cli.apps.cli import apps_cli

cli = typer.Typer()
cli.add_typer(
    apps_cli,
    name="app",
    help="Benchling apps are portable and transferable integrations administered within Benchling.",
)
