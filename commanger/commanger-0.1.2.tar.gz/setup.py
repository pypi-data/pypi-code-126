# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['commanger']

package_data = \
{'': ['*']}

install_requires = \
['colorama>=0.4.5,<0.5.0', 'pyparsing>=3.0.9,<4.0.0']

setup_kwargs = {
    'name': 'commanger',
    'version': '0.1.2',
    'description': 'A easy to use, extremely configurable shell/terminal command manager for python.',
    'long_description': None,
    'author': 'ThatRandomPerson',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
