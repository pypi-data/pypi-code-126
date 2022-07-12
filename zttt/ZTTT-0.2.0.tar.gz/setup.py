# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zttt', 'zttt.zt_base', 'zttt.zt_engines', 'zttt.zt_errors']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'zttt',
    'version': '0.2.0',
    'description': 'A Tic Tac Toe Library with a near perfect engine',
    'long_description': '',
    'author': 'Sumanth NR',
    'author_email': 'sumanthnr62@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
