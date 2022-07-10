import subprocess
from .logger import Logger
import json


class Utils:
    def __init__(self) -> None:
        self.log = Logger()

    def write_config(self, config, config_path) -> None:
        """
            Store config file inside ~/.vpnr-client/config
        """
        json_object = json.dumps(config, indent=4)

        with open(config_path, "w") as file:
            self.log.info(f"Storing json credentials inside {config_path}")
            file.writelines(json_object)
            subprocess.call(['chmod', '0700', config_path])

    def read_config(self, config_path):
        """
            Read file and return json object
        """
        with open(config_path, "r") as file:
            self.log.info(f"Loading credentials from {config_path}")
            credentials = json.load(file)
            return credentials
    
    def write_tunnel_config(self, config, config_path) -> None:
        """
            Write tunnel config
        """
        with open(config_path, "w") as file:
            self.log.info(f"Storing json credentials inside {config_path}")
            file.write(config)
            subprocess.call(['chmod', '0700', config_path])
