# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['firebird_connect', 'firebird_connect.src']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'firebird-connect',
    'version': '0.3.0',
    'description': '',
    'long_description': None,
    'author': 'Isac Martins',
    'author_email': '50426537+isaukywhite@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
