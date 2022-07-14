import typer


from ratelimitcli import RATELIMIT_CLI_NAME, __version__
from ratelimitcli.billing import billing
from ratelimitcli.limits import limits
from ratelimitcli.config.configure import configure as _configure, help

app = typer.Typer()
app.add_typer(billing.app, name="billing")
app.add_typer(limits.app, name="limits")


@app.command(short_help="Configure RateLimit CLI options", help=help)
def configure():
    return _configure()


@app.command()
def version():
    """Print the CLI version."""
    typer.echo(f"{RATELIMIT_CLI_NAME} version {__version__}")
