from mixsim.config.parsers.config_parsers import TOMLParser


class ConfigType:
    TOML = TOMLParser


class Options:
    _config_type = TOMLParser
