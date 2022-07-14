import typer

from ratelimitcli.config import CONFIG_PATH
from ratelimitcli.config.config_file_serde import (
    ConfigFileSerDe,
    User,
    Config,
    setattr_nested,
)

help = """
NAME:

    configure

DESCRIPTION

    Configure  RateLimit  CLI  options. If this command is run with no
    arguments, you will be prompted for various configuration values such
    as your name and your email. If your config file does not exist (the
    default location is ~/.ratelimit/config), the RateLimit CLI will
    create it for you.

    To keep an existing value, hit enter when prompted for the value. When
    you are prompted for information, the current value will be displayed
    in [brackets].  If the config item has no value, it be displayed as
    [None].  Note that the configure command only works with values from
    the config file. It does not use any configuration values from
    environment variables.

    Note: the values you provide for the ratelimit_api_key will be written
    to the config file.

CONFIGURATION VARIABLES

    The following configuration variables are supported in the config
    file:

    o ratelimit_api_key - The ratelimit api key

SYNOPSIS

    ratelimitcli configure
"""


def configure() -> None:
    """Write a configuration file to `~/.ratelimit/configure`."""
    serde = ConfigFileSerDe(CONFIG_PATH)
    existing_config = serde.load()

    new_config = Config(
        user=User(
            first_name=None,
            last_name=None,
            email=None,
        ),
        ratelimit_api_key=None,
    )

    prompt_and_replace(
        "API key   ", existing_config, new_config, "ratelimit_api_key", sensitive=True
    )
    prompt_and_replace("First name", existing_config, new_config, "user.first_name")
    prompt_and_replace("Last name ", existing_config, new_config, "user.last_name")
    prompt_and_replace("Email name", existing_config, new_config, "user.email")
    serde.dump(new_config)


def _getattr_nested(obj, path: str):
    parts = path.split(".")
    for attr in parts:
        if obj is None:
            return None
        obj = getattr(obj, attr, None)
    return obj


def prompt_and_replace(
    prompt: str,
    existing_config: Config,
    new_config: Config,
    path: str,
    sensitive=False,
):
    existing = _getattr_nested(existing_config, path)
    obscured = "*****"
    default = "None" if existing is None else existing if not sensitive else obscured
    new_value = typer.prompt(
        prompt,
        default=default,
    )
    if new_value == obscured:
        new_value = existing
    if new_value == "None":
        new_value = None
    setattr_nested(new_config, path, new_value)
