from pathlib import Path

RATELIMIT_DIR = ".ratelimit"
CONFIG_FILE = "config"
CONFIG_PATH = Path.home() / Path(f"{RATELIMIT_DIR}/{CONFIG_FILE}")
