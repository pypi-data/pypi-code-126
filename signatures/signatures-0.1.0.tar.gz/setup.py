# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['signatures']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'signatures',
    'version': '0.1.0',
    'description': 'Utilities for inspecting and comparing Python function signatures.',
    'long_description': None,
    'author': 'Joseph Hale',
    'author_email': 'me@jhale.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
