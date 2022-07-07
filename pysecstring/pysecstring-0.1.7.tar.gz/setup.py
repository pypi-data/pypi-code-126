# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pysecstring']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pysecstring',
    'version': '0.1.7',
    'description': "Python implementation of Window's Securestring forked from aznashwan/py-securestring",
    'long_description': None,
    'author': 'Gwang-Jin Kim',
    'author_email': 'gwang.jin.kim.phd@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
