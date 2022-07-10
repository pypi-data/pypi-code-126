import os
import argparse
import json

import fastf1
import fastf1.plotting

from .Drivers import Driver
from .Layout import Layout, JSONLayout

CACHE_DIR = "./cache"

parser = argparse.ArgumentParser(description='Plot driver data')
parser.add_argument('driver', type=str, help='Driver name', nargs="*")
parser.add_argument('--season', type=int, help='Season number')
parser.add_argument('--circuit', type=str, help='Circuit name')
parser.add_argument('--session', type=str, help='Session name',
                    choices=['FP1', 'FP2', 'FP3', 'SQ', 'Q', 'S', 'R'])
parser.add_argument('--lap', type=int, help='Lap number', default=None)
parser.add_argument('--xaxis', type=str, help='X axis Metric', default="Time")
parser.add_argument('--yaxis', type=str, help='Y axis Metric',
                    default="Speed", nargs="+")
parser.add_argument('--json_layout', type=str,
                    help='JSON layout file path', default=None)
parser.add_argument('--clear_cache', type=bool, default=False, help='Clear cache')
parser.add_argument('--disable_cache', type=bool, default=False, help='Disable cache')
parser.add_argument('--cache_dir', type=str, default=None, help='Cache directory')

args = parser.parse_args()

if args.cache_dir is not None:
    CACHE_DIR = args.cache_dir

if args.clear_cache:
    if os.path.exists(CACHE_DIR):
        fastf1.Cache.clear_cache(CACHE_DIR)

fastf1.plotting.setup_mpl()

if not args.disable_cache:
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)
    fastf1.Cache.enable_cache(CACHE_DIR)
else:
    fastf1.Cache.disabled()

if args.json_layout is None:

    if args.season is None or args.circuit is None or args.session is None or len(args.driver) == 0:
        parser.error("--season, --circuit --session and at least one driver are required")
    
    session = fastf1.get_session(args.season, args.circuit, args.session)

    session.load()

    if args.driver is None or len(args.driver) == 0:
        args.driver = session.drivers
    
    drivers = []

    for driver in args.driver:
        drivers.append(Driver(driver, session))
    # The rest is just plotting

    layout = Layout(drivers=drivers, session=session,
                    lap_number=args.lap, x_axis=args.xaxis, y_axis=args.yaxis)
    layout.plot()
else:

    json_obj = {}

    with open(args.json_layout) as json_file:
        json_obj = json.load(json_file)

    session = fastf1.get_session(json_obj["season"], json_obj["circuit"], json_obj["session"])
    session.load()

    drivers = []
    for driver in json_obj["drivers"]:
        drivers.append(Driver(driver, session))

    json_obj["drivers"] = drivers
    json_obj["session"] = session

    layout = JSONLayout(json_obj=json_obj)
    layout.plot()
