# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['weather4py']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'weather4py',
    'version': '0.1.0',
    'description': 'a library for your weathery needs.',
    'long_description': None,
    'author': 'MintTeaNeko',
    'author_email': 'neonwinternight1@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
