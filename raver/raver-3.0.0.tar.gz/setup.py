# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['raver']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'semver>=2.13.0,<3.0.0', 'tomli>=2.0.1,<3.0.0']

entry_points = \
{'console_scripts': ['raver = raver.cli:cli']}

setup_kwargs = {
    'name': 'raver',
    'version': '3.0.0',
    'description': 'Ratio package management tool.',
    'long_description': None,
    'author': 'Ratio Innovations B.V.',
    'author_email': 'info@ratio-case.nl',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
