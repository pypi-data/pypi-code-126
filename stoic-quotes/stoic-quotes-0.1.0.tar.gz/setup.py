# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['main']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'stoic-quotes',
    'version': '0.1.0',
    'description': 'Quotes to inspire you everytime!',
    'long_description': None,
    'author': 'Gurupratap Matharu',
    'author_email': 'gurupratap.matharu@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
