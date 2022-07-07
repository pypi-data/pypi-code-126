# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['token_auth_cli']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0',
 'click>=8.1.3,<9.0.0',
 'pydantic>=1.9.1,<2.0.0',
 'rich>=12.4.4,<13.0.0',
 'toml>=0.10.2,<0.11.0']

entry_points = \
{'console_scripts': ['token-auth-cli = token_auth_cli.cli:main']}

setup_kwargs = {
    'name': 'token-auth-cli',
    'version': '0.1.2',
    'description': 'Simple tool for testing token authentication during development.',
    'long_description': '[![Python package](https://github.com/0djentd/token-auth-cli/actions/workflows/python-package.yml/badge.svg)](https://github.com/0djentd/token-auth-cli/actions/workflows/python-package.yml)\n# token-auth-cli\n## Description\nSimple tool for testing token authentication during development.\n\n## How to use\n```\ntoken-auth-cli\n```\n',
    'author': '0djentd',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/0djentd/token-auth-cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
