# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hamrobazaar']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp[speedups]>=3.8.1,<4.0.0', 'python-slugify>=6.1.2,<7.0.0']

setup_kwargs = {
    'name': 'hamrobazaar',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Sulav Maharjan',
    'author_email': 'sulavmaharjan63@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
