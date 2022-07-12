# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['colo']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['colo = colo.colo:colo']}

setup_kwargs = {
    'name': 'colo',
    'version': '0.1.0',
    'description': 'A simple script to print out the 256 terminal colors in various formats',
    'long_description': '# colo',
    'author': 'terminaldweller',
    'author_email': 'thabogre@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/terminaldweller/colo',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
