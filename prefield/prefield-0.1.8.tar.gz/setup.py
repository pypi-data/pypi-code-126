# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['prefield',
 'prefield.agent',
 'prefield.aws',
 'prefield.cli',
 'prefield.datetime_util',
 'prefield.parsing',
 'prefield.results',
 'prefield.tasks']

package_data = \
{'': ['*']}

install_requires = \
['prefect>=0.15.13,<0.16.0']

entry_points = \
{'console_scripts': ['prefield = prefield.cli.main:main']}

setup_kwargs = {
    'name': 'prefield',
    'version': '0.1.8',
    'description': 'Prefect tasks and CLI functionality to be used across Prefect projects',
    'long_description': None,
    'author': 'atsangarides',
    'author_email': 'andreas@field.energy',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
