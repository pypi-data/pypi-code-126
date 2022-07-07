# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['python-wordle-helper']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.23.0,<2.0.0', 'requests>=2.28.1,<3.0.0', 'wordfreq>=3.0.1,<4.0.0']

entry_points = \
{'console_scripts': ['wordle-helper = python-wordle-helper.cli:main']}

setup_kwargs = {
    'name': 'python-wordle-helper',
    'version': '0.1.0',
    'description': 'Cheat at Wordle!',
    'long_description': None,
    'author': 'Hugh Enxing',
    'author_email': 'henxing@gmail.com',
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
