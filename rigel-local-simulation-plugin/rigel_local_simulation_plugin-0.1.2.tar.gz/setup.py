# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rigel_local_simulation_plugin']

package_data = \
{'': ['*']}

install_requires = \
['docker>=5.0.3,<6.0.0', 'rigelcore>=0.1.16,<0.2.0', 'roslibpy>=1.3.0,<2.0.0']

setup_kwargs = {
    'name': 'rigel-local-simulation-plugin',
    'version': '0.1.2',
    'description': 'A plugin for Rigel to locally run a containerized ROS application.',
    'long_description': None,
    'author': 'Pedro Miguel Melo',
    'author_email': 'pedro.m.melo@inesctec.pt',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
