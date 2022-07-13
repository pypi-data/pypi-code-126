# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['telq',
 'telq.authentication',
 'telq.endpoints',
 'telq.networks',
 'telq.results',
 'telq.tests']

package_data = \
{'': ['*']}

install_requires = \
['pytest>=7.1.2,<8.0.0',
 'python-dotenv>=0.20.0,<0.21.0',
 'requests>=2.27.1,<3.0.0']

setup_kwargs = {
    'name': 'telq',
    'version': '0.1.2',
    'description': 'Python SDK for TelQ Telecom API',
    'long_description': None,
    'author': 'Tuvshinbayar Davaa',
    'author_email': 'tuvshinbayar.davaa@telqtele.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
