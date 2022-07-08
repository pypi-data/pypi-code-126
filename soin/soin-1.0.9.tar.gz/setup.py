# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['soin']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'redis>=4.3.4,<5.0.0', 'requests>=2.28.1,<3.0.0']

entry_points = \
{'console_scripts': ['soin = soin.cli:cli']}

setup_kwargs = {
    'name': 'soin',
    'version': '1.0.9',
    'description': 'soin is a tool collections for spiders',
    'long_description': None,
    'author': 'chenglu',
    'author_email': 'chenglu.she@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
