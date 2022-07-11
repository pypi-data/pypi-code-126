from importlib import resources
try:
    import tomllib  # python 3.11
except ModuleNotFoundError:
    import tomli as tomllib


# Version of the Python package
__version__ = "1.0.0"

# Read URL of the Real Python feed from config file
_cfg = tomllib.loads(resources.read_text("pippy_ls", "config.toml"))
URL = _cfg["feed"]["url"]

# from ._version import get_versions


# __version__ = _version.get_versions()["version"]
# del get_versions
