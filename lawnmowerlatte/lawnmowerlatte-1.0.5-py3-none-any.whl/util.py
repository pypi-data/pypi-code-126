import os

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib


def tomlrc(*path, filename="~/.tomlrc"):
    filename = os.path.expanduser(filename)

    with open(filename, "rb") as f:
        toml = tomllib.load(f)

    if path is None:
        return toml
    else:
        for key in section:
            toml = toml[key]

        return toml
