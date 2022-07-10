# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['net_sniffer']

package_data = \
{'': ['*']}

install_requires = \
['netprotocols>=0.5.0,<0.6.0', 'pyinstaller>=5.1,<6.0']

setup_kwargs = {
    'name': 'net-sniffer',
    'version': '3.0.0',
    'description': 'A Network Packet Sniffing tool developed in Python 3',
    'long_description': None,
    'author': 'EONRaider',
    'author_email': 'livewire_voodoo@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
