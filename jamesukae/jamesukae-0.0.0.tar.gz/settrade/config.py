import os
import sys
from pathlib import Path

if sys.platform == "win32":
    directory = Path(os.environ["APPDATA"]).parent
else:
    directory = Path("/")

CONFIG_PATH = directory / "settradesdk_config.txt"

DEFAULT_CONFIG = {
    "environment": "prod",
    "clear_log": 30,
    "params": "",
}

try:
    with open(CONFIG_PATH, "r") as f:
        config = f.read().strip()
        config = config.split("\n")
        config = {k.strip(): v.strip() for k, v in (line.split("=") for line in config)}
        config = {**DEFAULT_CONFIG, **config}

        for k, v in config.items():
            if k == "environment":
                config[k] = v.lower()
            elif k == "clear_log":
                config[k] = int(v)
except FileNotFoundError:
    config = DEFAULT_CONFIG.copy()

with open(CONFIG_PATH, "w") as f:
    f.write("\n".join(f"{k}={v}" for k, v in config.items()))
