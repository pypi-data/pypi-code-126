from importlib import metadata

from mixsim.conf_schema import Config
from mixsim.config.argparsing import parse
from mixsim.pipeline import entry

__version__: str = metadata.metadata(__package__)["version"]


def main() -> None:
    conf = parse(config_class=Config)
    entry(conf)
