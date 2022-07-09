# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['genesisapi', 'genesisapi.services']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.4.0,<2.0.0', 'typeguard>=2.13.3,<3.0.0']

setup_kwargs = {
    'name': 'genesisapi',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Roland Abel',
    'author_email': 'roland.abel@live.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
