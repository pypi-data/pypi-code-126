# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tfprotocol_client',
 'tfprotocol_client.connection',
 'tfprotocol_client.misc',
 'tfprotocol_client.models',
 'tfprotocol_client.security']

package_data = \
{'': ['*']}

install_requires = \
['multipledispatch>=0.6.0,<0.7.0', 'pycryptodome>=3.15.0,<4.0.0']

setup_kwargs = {
    'name': 'tfprotocol-client',
    'version': '1.0.0',
    'description': 'Transfer Protocol client implemented in python, the specifications for this protocol is in https://github.com/GoDjango-Development/TFProtocol/blob/main/doc/',
    'long_description': None,
    'author': 'Leonel Garcia',
    'author_email': 'lagcleaner@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.2,<4.0.0',
}


setup(**setup_kwargs)
