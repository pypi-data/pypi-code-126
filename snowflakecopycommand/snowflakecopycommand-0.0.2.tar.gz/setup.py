# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['snowflakecopycommand']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'snowflakecopycommand',
    'version': '0.0.2',
    'description': '',
    'long_description': None,
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10',
}


setup(**setup_kwargs)
