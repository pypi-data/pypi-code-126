# -*- coding: utf-8 -*-
import sys
import os
import time
import importlib
import subprocess
from dataclasses import dataclass
from typing import Callable, Optional

import dotenv


@dataclass
class Config:
    # Maximum number of retries
    retry_times: int = 3

    # Delay before each retry (seconds)
    retry_delay: float = 5

    # Cleanup function, format 'module:func'
    cleaner: Callable = None

    # Alarm function, format 'module:func'
    alerter: Callable = None

    @classmethod
    def load_from_dotenv(cls):
        dotenv.load_dotenv(dotenv.find_dotenv(usecwd=True), override=True)

        result = cls()
        result.retry_times = int(os.getenv('NURSE_RUN_RETRY_TIMES', result.retry_times))
        result.retry_delay = float(os.getenv('NURSE_RUN_RETRY_DELAY', result.retry_delay))
        result.cleaner = cls.load_plugin_func('NURSE_RUN_CLEANER')
        result.alerter = cls.load_plugin_func('NURSE_RUN_ALERTER')
        return result

    @classmethod
    def load_plugin_func(cls, name: str) -> Optional[Callable]:
        """
        Load plugin function
        format 'module:func'
        """
        func_define = os.getenv(name)
        if not func_define:
            return

        module_name, func_name = func_define.split(':')
        module = importlib.import_module(module_name)
        func = getattr(module, func_name)
        return func


def run():
    p = subprocess.run(subprocess.list2cmdline(sys.argv[1:]), shell=True)
    if p.returncode != 0:
        print('\n******** Return Code: %d ********\n' % p.returncode)

    return p.returncode


def main():
    config = Config.load_from_dotenv()

    if not len(sys.argv) > 1:
        print('Command line arguments not specified')
        return -1

    print(config)
    print(sys.argv)
    print()

    if config.cleaner:
        # Clean up
        print('\n******** Clean ********\n')
        config.cleaner()

    return_code = 0
    for i in range(config.retry_times + 1):
        if i:
            print('\n******** Retry %d/%d ********\n' % (i, config.retry_times))
            if config.retry_delay:
                print('  wait %d seconds ...\n' % config.retry_delay)
                time.sleep(config.retry_delay)

        return_code = run()
        if return_code == 0:
            break

    # A return value other than 0 means failed
    if return_code and config.alerter:
        # alert
        print('\n******** Alert ********\n')
        config.alerter()

    print('\n******** Exit Code: %d ********' % return_code)
    return return_code


if __name__ == '__main__':
    ret = main()
    sys.exit(ret)
