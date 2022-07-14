import requests
import typer

from ratelimitcli.limits.read_write import ThriftReadWrite, Base64ReadWrite
from ratelimitcli.limits import cli_thrift as T

from ratelimitcli.config.middlewear import check_for_config_file

app = typer.Typer(
    short_help="Create and update rate limits.",
    help="""
NAME:

    limits

DESCRIPTION

    Create and update rate limits as well as record requests against rate
    limits you have created.

SYNOPSIS

    ratelimitcli limits
""",
)

_MAX_INT = 1 << 32


def throttling_burst_limit_callback(value: int) -> int:
    error = "Invalid burst limit value. Must be between [0, 2^32]."
    if value < 0 or value > _MAX_INT:
        raise typer.BadParameter(error)
    return value


def throttling_rate_limit_callback(value: int) -> int:
    error = "Invalid rate limit value. Must be between [0, 2^32]."
    if value < 0 or value > _MAX_INT:
        raise typer.BadParameter(error)
    return value


@app.command()
def upsert(
    throttling_burst_limit: int = typer.Option(
        ..., callback=throttling_burst_limit_callback
    ),
    throttling_rate_limit: int = typer.Option(
        ..., callback=throttling_rate_limit_callback
    ),
    limit_id: str = None,
    purpose: str = "cmdline",
    tracking_id: str = "cmdline",
):
    """Create or update a rate limit."""
    existing_config = check_for_config_file()

    thrift = T.SetLimitRequest(
        meta=T.Metadata(
            client_id=existing_config.user.email,
            purpose=purpose,
            tracking_id=tracking_id,
        ),
        limit_id=limit_id,
        throttling_burst_limit=throttling_burst_limit,
        throttling_rate_limit=throttling_rate_limit,
    )
    rw = ThriftReadWrite(T.SetLimitRequest)
    brw = Base64ReadWrite()
    data = brw.to_base64(rw.to_bytes(thrift))

    response = requests.post(
        "https://api.ratelimit.xyz/api/config",
        headers={
            "X-CLIENT-ID": existing_config.user.email,
            "Authorization": existing_config.ratelimit_api_key,
            "Content-Type": "application/text",
        },
        data=data,
    )
    if response.status_code != 200:
        typer.echo(f"Bad API response ({response.text}).", err=True)
        raise typer.Exit(code=1)
    else:
        typer.echo(f"Ok: API response ({response.text}).")


@app.command()
def record(limit_id: str, purpose: str = "cmdline", tracking_id: str = "cmdline"):
    """Record a request against a rate limit."""
    existing_config = check_for_config_file()

    thrift = T.GetRemainingCapacityRequest(
        meta=T.Metadata(
            client_id=existing_config.user.email,
            purpose=purpose,
            tracking_id=tracking_id,
        ),
        limit_id=limit_id,
    )
    rw = ThriftReadWrite(T.GetRemainingCapacityRequest)
    brw = Base64ReadWrite()
    data = brw.to_base64(rw.to_bytes(thrift))

    response = requests.post(
        "https://api.ratelimit.xyz/api/bucket",
        headers={
            "X-CLIENT-ID": existing_config.user.email,
            "Authorization": existing_config.ratelimit_api_key,
            "Content-Type": "application/text",
        },
        data=data,
    )
    if response.status_code == 200:
        typer.echo(f"Ok: API response ({response.text}).")
    elif response.status_code == 429:
        typer.echo(f"Too Many Requests: API response ({response.text}).", err=True)
        raise typer.Exit(code=1)
    else:
        typer.echo(f"Error: API response ({response.text}).", err=True)
        raise typer.Exit(code=1)
