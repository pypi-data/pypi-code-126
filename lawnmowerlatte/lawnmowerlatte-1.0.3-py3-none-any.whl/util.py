import os

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib


def tomlrc(filename="~/.tomlrc", section=None):
    filename = os.path.expanduser(filename)

    with open(filename, "rb") as f:
        toml = tomllib.load(f)

    if section is None:
        return toml
    else:
        for key in section:
            toml = toml[key]

        return toml
