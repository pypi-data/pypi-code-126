# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tidy3d', 'tidy3d.components', 'tidy3d.components.grid']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'tidy3d-model',
    'version': '0.1.2',
    'description': '',
    'long_description': None,
    'author': 'An Li',
    'author_email': 'kidylee@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
