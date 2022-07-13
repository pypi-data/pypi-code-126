import os
import yaml
from fiopy.enums import ConfigType

__all__ = ["Config"]


class Config:
    _config_dir = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "config")))

    api = {}
    with open(os.path.join(_config_dir, f"{ConfigType.API}.yaml")) as fp:
        api = yaml.safe_load(fp)

    user = None

    @staticmethod
    def update_config(*, config=None, config_type: ConfigType):
        setattr(Config, config_type.value, config)

