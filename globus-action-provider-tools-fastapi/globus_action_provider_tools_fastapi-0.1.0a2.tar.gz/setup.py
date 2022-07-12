# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['globus_action_provider_tools_fastapi']

package_data = \
{'': ['*']}

install_requires = \
['arrow>=1,<2',
 'fastapi>=0.78,<0.79',
 'globus-action-provider-tools>=0.12.0,<0.13.0']

setup_kwargs = {
    'name': 'globus-action-provider-tools-fastapi',
    'version': '0.1.0a2',
    'description': '',
    'long_description': None,
    'author': 'Jim Pruyne',
    'author_email': 'pruyne@uchicago.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
