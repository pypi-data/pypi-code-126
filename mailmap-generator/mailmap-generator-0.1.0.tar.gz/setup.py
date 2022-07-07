# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mailmap_generator']

package_data = \
{'': ['*']}

install_requires = \
['docopt>=0.6.2,<0.7.0', 'pandas>=1.4.3,<2.0.0']

entry_points = \
{'console_scripts': ['mailmap = mailmap_generator.cli:main']}

setup_kwargs = {
    'name': 'mailmap-generator',
    'version': '0.1.0',
    'description': 'A small command line tool to create git .mailmap files from a commit history.',
    'long_description': None,
    'author': 'HelgeCPH',
    'author_email': 'ropf@itu.dk',
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
