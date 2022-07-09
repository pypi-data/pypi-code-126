from configparser import ConfigParser
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CONFIG_FILE = os.path.join(BASE_DIR,"config.ini")

DBNAME = "mikasa.sqlite3"

# Get the configparser object
config_object = ConfigParser()

config_object.read(CONFIG_FILE)

reader = config_object



def read(group="config", var="db"):
    config_object.read(CONFIG_FILE)

    return config_object.get(group, var)


def write( val):
    config_object['config'] = {
        'db':val
    }

    with open(CONFIG_FILE, "w") as config:
        config_object.write(config)
        
    print("great you're readt to go ")