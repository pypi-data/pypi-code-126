# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lulugai']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'lulugai',
    'version': '0.0.1',
    'description': '',
    'long_description': None,
    'author': 'gelulu',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
