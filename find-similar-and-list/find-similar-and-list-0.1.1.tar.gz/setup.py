# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['find_similar_and_list']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['find-similar-and-list = find_similar_and_list.cli:main']}

setup_kwargs = {
    'name': 'find-similar-and-list',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': '0djentd',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
