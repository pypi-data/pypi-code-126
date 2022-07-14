import typing

from ratelimitcli.config import CONFIG_PATH
from ratelimitcli.config.config_file_serde import ConfigFileSerDe, Config

import typer


def check_for_config_file() -> typing.Union[typing.NoReturn, Config]:
    serde = ConfigFileSerDe(CONFIG_PATH)
    existing_config = serde.load()
    if not existing_config:
        typer.echo(
            "No existing config file found. Please run `ratelimit configure` first.",
            err=True,
        )
        raise typer.Exit(code=1)
    return existing_config
