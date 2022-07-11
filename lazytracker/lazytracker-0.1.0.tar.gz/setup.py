# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lazytracker']

package_data = \
{'': ['*']}

install_requires = \
['dill>=0.3.5,<0.4.0']

setup_kwargs = {
    'name': 'lazytracker',
    'version': '0.1.0',
    'description': 'Caching of functions with respect to code changes and disk-file changes',
    'long_description': None,
    'author': 'Michal Pogoda',
    'author_email': 'michal.pogoda@bards.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mipo57/lazytracker',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
