# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zero_sdk']

package_data = \
{'': ['*']}

install_requires = \
['python-graphql-client==0.4.3']

setup_kwargs = {
    'name': 'zero-sdk',
    'version': '0.1.9',
    'description': 'zero client sdk',
    'long_description': None,
    'author': 'kirill-ottofeller',
    'author_email': 'kirill.korotkov@ottofeller.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
