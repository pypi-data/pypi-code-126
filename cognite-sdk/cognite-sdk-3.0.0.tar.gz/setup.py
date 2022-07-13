# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['cognite',
 'cognite.client',
 'cognite.client._api',
 'cognite.client._api.transformations',
 'cognite.client.data_classes',
 'cognite.client.data_classes.model_hosting',
 'cognite.client.data_classes.transformations',
 'cognite.client.utils']

package_data = \
{'': ['*']}

install_requires = \
['msal>=1,<2', 'requests>=2,<3', 'requests_oauthlib>=1,<2']

extras_require = \
{'all': ['sympy', 'pandas', 'geopandas>=0.10.0', 'shapely>=1.7.0'],
 'geo': ['geopandas>=0.10.0', 'shapely>=1.7.0'],
 'pandas': ['pandas'],
 'sympy': ['sympy']}

setup_kwargs = {
    'name': 'cognite-sdk',
    'version': '3.0.0',
    'description': 'Cognite Python SDK',
    'long_description': None,
    'author': 'Erlend Vollset',
    'author_email': 'erlend.vollset@cognite.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
