# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['prefixcommons']

package_data = \
{'': ['*'], 'prefixcommons': ['registry/*']}

install_requires = \
['requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'prefixcommons',
    'version': '0.1.11',
    'description': 'A python API for working with ID prefixes',
    'long_description': None,
    'author': 'cmungall',
    'author_email': 'cjm@berkeleybop.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
