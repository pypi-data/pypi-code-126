from dataclasses import dataclass, asdict
from pathlib import Path
import typing

import pytomlpp
import typer


@dataclass
class User:
    first_name: str = None
    last_name: str = None
    email: str = None


@dataclass
class Config:
    user: User = None
    ratelimit_api_key: str = None


class ConfigFileSerDe:
    ATTR_PATHS = [
        "user.first_name",
        "user.last_name",
        "user.email",
        "ratelimit_api_key",
    ]

    def __init__(self, file_path: Path):
        self.config_file = file_path.resolve()
        self.config_file.parent.mkdir(exist_ok=True)
        self.data = None

    def _parse_user(self, user_data: typing.Dict) -> User:
        if not user_data:
            return None

        return User(**user_data)

    def _parse(self, data: typing.Dict) -> Config:
        if not data:
            return None

        user_data = (data or {}).get("user", {})
        user = self._parse_user(user_data)
        ratelimit_api_key = data.get("ratelimit_api_key", None)
        if user or ratelimit_api_key:
            return Config(user=user, ratelimit_api_key=ratelimit_api_key)
        return None

    def load(self) -> typing.Optional[Config]:
        """Deserialize the config file."""
        if self.data:
            return self.data

        if not self.config_file.exists():
            return None

        try:
            data = pytomlpp.load(self.config_file)
        except Exception:
            typer.echo(f"Unable to open config file at ({self.config_file}).")
            raise

        self.data = self._parse(data)
        return self.data

    def dump(self, config: Config) -> None:
        """Serialize the config file."""
        data = _compact(asdict(config))
        if not data:
            typer.echo(f"Nothing updated.")
            return

        pytomlpp.dump(data, self.config_file)
        typer.echo(f"Updated config file ({self.config_file}).")

        with self.config_file.open("a") as f:
            f.write("\n")


def setattr_nested(obj, path: str, value) -> None:
    parts = path.split(".")
    for attr in parts[:-1]:
        if obj is None:
            raise ValueError(f"Unable to set value for ({path}).")
        obj = getattr(obj, attr, None)
    if obj is None:
        raise ValueError(f"Unable to set value for ({path}).")
    setattr(obj, parts[-1], value)


def _compact(data) -> typing.Dict:
    if not isinstance(data, dict):
        return data

    if not data:
        return {}

    compacted = {}
    for k, v in data.items():
        value = _compact(v)
        if value:
            compacted[k] = value
    return compacted
