# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nicefid']

package_data = \
{'': ['*']}

install_requires = \
['clean-fid>=0.1.24,<0.2.0']

setup_kwargs = {
    'name': 'nicefid',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Richard Löwenström',
    'author_email': 'samedii@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
