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
    'version': '0.2.0',
    'description': '',
    'long_description': '# find-similar-and-list\n## Installation\n```\npip install find-similar-and-list\n```\n\n## How to use\n```\nusage: find-similar-and-list [-h] [--files FILES [FILES ...]]\n                             [--ignore-file IGNORE_FILE]\n\noptions:\n  -h, --help            show this help message and exit\n  --files FILES [FILES ...]\n                        Files to filter\n  --ignore-file IGNORE_FILE\n```\n',
    'author': '0djentd',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/0djentd/find-similar-and-list',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
