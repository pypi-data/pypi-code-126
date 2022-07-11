# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pymongo303']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pymongo303',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Your Name',
    'author_email': 'william weiss',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=2.7,<3.0',
}


setup(**setup_kwargs)
