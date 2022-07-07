# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiobiketrax']

package_data = \
{'': ['*']}

install_requires = \
['PyJWT>=2.4.0,<3.0.0', 'aiohttp>=3.8.1,<4.0.0', 'auth0-python>=3.23.1,<4.0.0']

setup_kwargs = {
    'name': 'aiobiketrax',
    'version': '0.1.0',
    'description': 'Python library for interacting with the PowUnity BikeTrax GPS tracker.',
    'long_description': '# aiobiketrax\nPython library for interacting with the PowUnity BikeTrax GPS tracker.\n\n## Introduction\nThis library is mainly written to work with a custom component for\nHome Assistant.\n\nThe [PowUnity BikeTrax](https://powunity.com/) is a GPS tracker for electric\nbicycles. It provides real-time updates every when the bike is in motion, using\na 2G modem. It works in Europe, and requires a subscription after a trial\nperiod of one year.\n\n### Features\n* Multi-device support.\n* Traccar and admin API support.\n* Live updates using websocket.\n\nNot implemented:\n\n* Geofencing.\n* Global configuration, such as webhooks.\n\n## Usage\n```python\nfrom aiobiketrax import Account\n\nimport aiohttp\n\nasync with aiohttp.ClientSession() as session:\n    account = Account(\n        username="someone@example.org",\n        password="secret",\n        session=session)\n\n    await account.update_devices()\n\n    for device in account.devices:\n        print(device.name)\n```\n\n## Contributing\nTo contribute to this repository, use GitHub pull-requests.\n\n- Dependencies are managed using [poetry](https://python-poetry.org/).\n- Code is formatted using [black](https://github.com/psf/black).\n- Your branch is linear (rebase) and logical.\n\nThe models have been generated using [quicktype](https://quicktype.io/). See\nthe `contrib/generator/` folder for more information.\n\n## License\nSee the `[LICENSE](LICENSE.md)` file (MIT license).\n\n## Disclaimer\nUse this library at your own risk. I cannot be held responsible for any\ndamages.\n\nThis page and its content is not affiliated with PowUnity.',
    'author': 'Bas Stottelaar',
    'author_email': 'basstottelaar@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/basilfx/aiobiketrax',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
