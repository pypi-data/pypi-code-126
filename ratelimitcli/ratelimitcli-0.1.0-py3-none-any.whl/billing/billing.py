from dataclasses import asdict
import json

from curses.ascii import isdigit
from jose import jwt
import requests
import typer

from ratelimitcli.config import CONFIG_PATH
from ratelimitcli.config.config_file_serde import ConfigFileSerDe, Config
from ratelimitcli.config.middlewear import check_for_config_file

app = typer.Typer(
    short_help="Manage billing and API keys.",
    help="""
NAME:

    billing

DESCRIPTION

    Manage billing and API keys. Configure your payment options for the
    RateLimit CLI.  options. If this command is run with no arguments, you
    will be prompted for various payment values such as your credit card
    number and expiration date.

    These values will not be stored locally but will be transmitted to our
    payment processor for billing purposes. No charges will be processed
    until usage occurs.

SYNOPSIS

    ratelimitcli billing
""",
)


def credit_card_number_callback(value: str):
    error = "Invalid credit card number."
    if not value:
        raise typer.BadParameter(error)
    value = value.strip().replace(" ", "")
    if len(value) != 16:
        raise typer.BadParameter("Invalid credit card number: Must be 16 digits.")

    for digit in value:
        if not isdigit(digit):
            raise typer.BadParameter(error)

    return value


def credit_card_expiration_callback(value: str) -> str:
    if not value:
        raise typer.BadParameter("Invalid expiration.")
    value = value.strip()
    if value.find("/") == -1:
        raise typer.BadParameter("Invalid expiration: Format should be 'MM/YY'.")

    value = value.split("/")
    if len(value) != 2:
        raise typer.BadParameter("Invalid expiration: Format should be 'MM/YY'.")

    month, year = value
    if not month.isdigit() or not year.isdigit():
        raise typer.BadParameter("Invalid expiration: MM and YY must be integers.")

    month = int(month)
    year = int(year)
    if month < 1 or month > 12 or year < 0 or year > 99:
        raise typer.BadParameter(
            "Invalid expiration: MM should be in range [1, 12] YY should be in range [1, 99]."
        )

    return f"{month:02}/{year:02}"


def credit_card_ccv_callback(value: str) -> str:
    error = "Invalid CCV."
    if not value:
        raise typer.BadParameter(error)

    value = value.strip()
    if len(value) != 3:
        raise typer.BadParameter("Invalid CCV: Must be 3 digits.")

    for digit in value:
        if not isdigit(digit):
            raise typer.BadParameter(error)

    return value


@app.command()
def configure(
    card_number: str = typer.Option(
        ...,
        metavar="CARD_NUMBER",
        callback=credit_card_number_callback,
        prompt="Enter a credit card number",
    ),
    expiration: str = typer.Option(
        ...,
        metavar="MM/YY",
        callback=credit_card_expiration_callback,
        prompt="Enter the expiration date for that credit card",
    ),
    ccv: str = typer.Option(
        ...,
        metavar="###",
        callback=credit_card_ccv_callback,
        prompt="Enter the CCV for that credit card",
    ),
):
    """Request an API key."""
    existing_config = check_for_config_file()
    data = json.dumps(
        dict(
            config=asdict(existing_config.user),
            credit_card=dict(number=card_number, expiration=expiration, ccv=ccv),
        )
    )
    response = requests.post(
        "https://api.ratelimit.xyz/billing/create_customer",
        data=data,
        headers={"content-type": "application/json"},
    )
    if response.status_code != 200:
        typer.echo(f"Bad API response ({response.text}).", err=True)
        raise typer.Exit(code=1)

    config = response.json()
    if not isinstance(config, dict):
        typer.echo(f"Bad config ({config}).", err=True)
        raise typer.Exit(code=1)

    api_key = config.get("api_key", None)
    if api_key is None:
        typer.echo(f"Bad API key ({api_key}).", err=True)
        raise typer.Exit(code=1)

    serde = ConfigFileSerDe(CONFIG_PATH)
    existing_config = serde.load() or Config(user=None, ratelimit_api_key=None)
    existing_config.ratelimit_api_key = api_key
    serde.dump(existing_config)
    typer.echo("API key has been written to the config file.")

    claims = jwt.decode(api_key, None, options=dict(verify_signature=False))
    existing_config.user.email = claims["sub"]
    serde.dump(existing_config)
    typer.echo("User email has been updated in the config file.")
