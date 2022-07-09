# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['trustfall_py']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'trustfall-py',
    'version': '0.1.0',
    'description': 'Placeholder package for the Trustfall project: https://github.com/obi1kenobi/trustfall',
    'long_description': None,
    'author': 'Predrag Gruevski',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
