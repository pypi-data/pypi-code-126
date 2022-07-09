# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['twitter_remove_strangers']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'tweepy>=4.10.0,<5.0.0']

entry_points = \
{'console_scripts': ['twitter_remove_strangers = '
                     'twitter_remove_strangers:main']}

setup_kwargs = {
    'name': 'twitter-remove-strangers',
    'version': '0.1.0',
    'description': "Removing followers whom you don't follow",
    'long_description': None,
    'author': '51naa',
    'author_email': None,
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
