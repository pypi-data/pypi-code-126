# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['deci_adk']

package_data = \
{'': ['*']}

install_requires = \
['deci-lab-client>=2.15.1', 'pickle-mixin>=1.0.2,<2.0.0', 'torch>=1.9.0']

setup_kwargs = {
    'name': 'deci-adk',
    'version': '1.0.3',
    'description': 'Deci AutoNAC Development Kit',
    'long_description': None,
    'author': 'Deci AI',
    'author_email': 'rnd@deci.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<3.10',
}


setup(**setup_kwargs)
