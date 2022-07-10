# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['s4sdk', 's4sdk.package', 's4sdk.resource']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'argparse>=1.4.0,<2.0.0',
 'click>=8.1.3,<9.0.0',
 'pandas>=1.4.3,<2.0.0']

setup_kwargs = {
    'name': 's4sdk',
    'version': '0.2.1a1',
    'description': '',
    'long_description': None,
    'author': 'Roy Chotechuang',
    'author_email': 'htraexd@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
