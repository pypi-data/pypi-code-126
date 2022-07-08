# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jwt_kms']

package_data = \
{'': ['*']}

install_requires = \
['cryptography>=37.0.4,<38.0.0']

entry_points = \
{'console_scripts': ['test = scripts:test']}

setup_kwargs = {
    'name': 'jwt-kms',
    'version': '0.1.0',
    'description': 'Library to offload some JWT crypto operations to KMS',
    'long_description': None,
    'author': 'Juha-Matti Tapio',
    'author_email': 'jmtapio@verkkotelakka.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
