#!/usr/bin/env python

import cProfile

from fameio.scripts.make_config import run as make_config
from fameio.scripts.make_config import DEFAULT_CONFIG as DEFAULT_MAKE_CONFIG
from fameio.scripts.convert_results import run as convert_results
from fameio.scripts.convert_results import DEFAULT_CONFIG as DEFAULT_CONVERT_CONFIG
from fameio.source.cli import arg_handling_make_config, arg_handling_convert_results


if __name__ == '__main__':
    input_file, run_config = arg_handling_convert_results(DEFAULT_CONVERT_CONFIG)
#    input_file, run_config = arg_handling_make_config(DEFAULT_MAKE_CONFIG)
    profiler = cProfile.Profile()
    profiler.enable()

    convert_results(input_file, run_config)
#    make_config(input_file, run_config)

    profiler.disable()
    profiler.dump_stats("profile.prof")
