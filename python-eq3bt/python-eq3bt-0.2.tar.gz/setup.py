# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['eq3bt', 'eq3bt.tests']

package_data = \
{'': ['*']}

install_requires = \
['bleak', 'click', 'construct']

extras_require = \
{'bluepy': ['bluepy>=1.0.5'], 'gattlib': ['gattlib']}

entry_points = \
{'console_scripts': ['eq3cli = eq3bt.eq3cli:cli']}

setup_kwargs = {
    'name': 'python-eq3bt',
    'version': '0.2',
    'description': 'EQ3 bluetooth thermostat support library',
    'long_description': '# python-eq3bt\n\nPython library and a command line tool for EQ3 Bluetooth smart thermostats, uses bleak (default), bluepy or gattlib for BTLE communication.\n\n# Features\n\n* Reading device status: locked, low battery, valve state, window open, target temperature, active mode\n* Writing settings: target temperature, auto mode presets, temperature offset\n* Setting the active mode: auto, manual, boost, away\n* Reading the device serial number and firmware version\n* Reading presets and temperature offset in more recent firmware versions.\n\n## Not (yet) supported\n\n* No easy-to-use interface for setting schedules.\n\n# Installation\n\n```bash\npip install python-eq3bt\n```\n\n# Command-line Usage\n\nTo test all available functionality a cli tool inside utils can be used:\n```\n$ eq3cli  --help\nUsage: eq3cli [OPTIONS] COMMAND [ARGS]...\n\n  Tool to query and modify the state of EQ3 BT smart thermostat.\n\nOptions:\n  --mac TEXT                  [required]\n  --interface TEXT\n  --debug / --normal\n  --backend [bleak|bluepy|gattlib]\n  --help                      Show this message and exit.\n\nCommands:\n  away         Enables or disables the away mode.\n  boost        Gets or sets the boost mode.\n  device       Displays basic device information.\n  locked       Gets or sets the lock.\n  low-battery  Gets the low battery status.\n  mode         Gets or sets the active mode.\n  offset       Sets the temperature offset [-3,5 3,5]\n  presets      Sets the preset temperatures for auto mode.\n  schedule     Gets the schedule from the thermostat.\n  state        Prints out all available information.\n  temp         Gets or sets the target temperature.\n  valve-state  Gets the state of the valve.\n  window-open  Gets and sets the window open settings.\n```\n\nEQ3_MAC environment variable can be used to define mac to avoid typing it:\n```bash\nexport EQ3_MAC=XX:XX\n```\n\nWithout parameters current state of the device is printed out.\n```bash\n$ eq3cli\n\n[00:1A:22:XX:XX:XX] Target 17.0 (mode: auto dst, away: no)\nLocked: False\nBatter low: False\nWindow open: False\nWindow open temp: 12.0\nWindow open time: 0:15:00\nBoost: False\nCurrent target temp: 17.0\nCurrent comfort temp: 20.0\nCurrent eco temp: 17.0\nCurrent mode: auto dst locked\nValve: 0\n```\n\nGetting & setting values.\n```bash\n$ eq3cli temp\n\nCurrent target temp: 17.0\n\neq3cli temp --target 20\n\nCurrent target temp: 17.0\nSetting target temp: 20.0\n```\n\n# Pairing\n\nIf you have thermostat with firmware version 1.20+ pairing may be needed. Below simple procedure to do that.\n\n```\nPress and hold wheel on thermostat until Pair will be displayed. Remember or write it.\n\n$ sudo bluetoothctl\n[bluetooth]# power on\n[bluetooth]# agent on\n[bluetooth]# default-agent\n[bluetooth]# scan on\n[bluetooth]# scan off\n[bluetooth]# pair 00:1A:22:06:A7:83\n[agent] Enter passkey (number in 0-999999): <enter pin>\n[bluetooth]# trust 00:1A:22:06:A7:83\n[bluetooth]# disconnect 00:1A:22:06:A7:83\n[bluetooth]# exit\n\nOptional steps:\n[bluetooth]# devices - to list all bluetooth devices\n[bluetooth]# info 00:1A:22:06:A7:83\nDevice 00:1A:22:06:A7:83 (public)\n\tName: CC-RT-BLE\n\tAlias: CC-RT-BLE\n\tPaired: yes\n\tTrusted: yes\n\tBlocked: no\n\tConnected: no\n\tLegacyPairing: no\n\tUUID: Generic Access Profile    (00001800-0000-1000-8000-00805f9b34fb)\n\tUUID: Generic Attribute Profile (00001801-0000-1000-8000-00805f9b34fb)\n\tUUID: Device Information        (0000180a-0000-1000-8000-00805f9b34fb)\n\tUUID: Vendor specific           (3e135142-654f-9090-134a-a6ff5bb77046)\n\tUUID: Vendor specific           (9e5d1e47-5c13-43a0-8635-82ad38a1386f)\n\tManufacturerData Key: 0x0000\n\tManufacturerData Value:\n  00 00 00 00 00 00 00 00 00                       .........\n```\n\nBe aware that sometimes if you pair your device then mobile application (calor BT) can\'t connect with thermostat and vice versa.\n\n\n# Library Usage\n\n```\nfrom eq3bt import Thermostat\n\nthermostat = Thermostat(\'AB:CD:EF:12:23:45\')\nthermostat.update()  # fetches data from the thermostat\n\nprint(thermostat)\n```\n\n<aside class="notice">\nNotice: The device in question has to be disconnected from bluetoothd, since BTLE devices can only hold one connection at a time.\n\nThe library will try to connect to the device second time in case it wasn\'t successful in the first time,\nwhich can happen if you are running other applications connecting to the same thermostat.\n</aside>\n\n## Fetching schedule\n\nThe schedule is queried per day basis and the cached information can be\naccessed through `schedule` property..\n\n```\nfrom eq3bt import Thermostat\n\nthermostat = Thermostat(\'AB:CD:EF:12:34:45\')\nthermostat.query_schedule(0)\nprint(thermostat.schedule)\n```\n\n## Setting schedule\n\nThe \'base_temp\' and \'next_change_at\' paramater define the first period for that \'day\' (the period from midnight up till next_change_at).\n\nThe schedule can be set on a per day basis like follows:\n\n```\nfrom datetime import time\nfrom eq3bt import Thermostat\nfrom eq3bt import HOUR_24_PLACEHOLDER as END_OF_DAY\n\nthermostat = Thermostat(\'12:34:56:78:9A:BC\')\nthermostat.set_schedule(\n    dict(\n        cmd="write",\n        day="sun",\n        base_temp=18,\n        next_change_at=time(8, 0),\n        hours=[\n            dict(target_temp=23, next_change_at=time(20, 0)),\n            dict(target_temp=18, next_change_at=END_OF_DAY),\n            dict(target_temp=23, next_change_at=END_OF_DAY),\n            dict(target_temp=23, next_change_at=END_OF_DAY),\n            dict(target_temp=23, next_change_at=END_OF_DAY),\n            dict(target_temp=23, next_change_at=END_OF_DAY)\n        ]\n    )\n)\n```\n\n# Contributing\n\nFeel free to open pull requests to improve the library!\n\nThis project uses github actions to enforce code formatting using tools like black, isort, flake8, and mypy.\nYou can run these checks locally either by executing `pre-commit run -a` or using `tox` which also runs the test suite.\n\n\n# History\n\nThis library is a simplified version of bluepy_devices from Markus Peter (https://github.com/bimbar/bluepy_devices.git) with support for more features and robuster device handling.\n',
    'author': 'Teemu R.',
    'author_email': 'tpr@iki.fi',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rytilahti/python-eq3bt',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
