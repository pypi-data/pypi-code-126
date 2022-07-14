# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aybolit']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'aybolit',
    'version': '0.1.0rc3',
    'description': '',
    'long_description': None,
    'author': 'A.Shpak',
    'author_email': 'shpaker@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7.2,<4.0.0',
}


setup(**setup_kwargs)
