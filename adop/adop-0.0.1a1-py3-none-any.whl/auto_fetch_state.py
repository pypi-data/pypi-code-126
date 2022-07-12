import configparser
import pathlib
from hashlib import sha256


class State:
    def __init__(self, cache_root_name: str) -> None:
        cache_root = pathlib.Path.cwd().joinpath(cache_root_name)
        cache_root.mkdir(parents=True, exist_ok=True)
        config = configparser.ConfigParser()
        config_file_path = cache_root.joinpath("autofetchstate.ini")
        config.read(config_file_path)
        self.config = config
        self.config_file_path = config_file_path

    def get(self, source: str):
        if self.config.has_section(source):
            return self.config.get(source, "last_update")

    def update(self, source: str, updated: str):
        if not self.config.has_section(source):
            self.config.add_section(source)
        self.config.set(source, "last_update", updated)

    def store(self):
        with self.config_file_path.open(mode="w") as f:
            self.config.write(f)

    @staticmethod
    def make(bin_data):
        return sha256(bin_data).hexdigest()
