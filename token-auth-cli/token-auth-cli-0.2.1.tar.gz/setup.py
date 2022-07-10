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
    'version': '0.2.1',
    'description': 'Simple tool for testing token authentication during development.',
    'long_description': '\n![PyPI](https://img.shields.io/pypi/v/token-auth-cli)\n![GitHub release (latest SemVer including pre-releases)](https://img.shields.io/github/v/release/0djentd/token-auth-cli?include_prereleases)\n![GitHub all releases](https://img.shields.io/github/downloads/0djentd/token-auth-cli/total)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/token-auth-cli)\n\n![GitHub issues](https://img.shields.io/github/issues/0djentd/token-auth-cli)\n![GitHub commit activity](https://img.shields.io/github/commit-activity/m/0djentd/token-auth-cli)\n![GitHub Repo stars](https://img.shields.io/github/stars/0djentd/token-auth-cli?style=social)\n\n[![Python package](https://github.com/0djentd/token-auth-cli/actions/workflows/python-package.yml/badge.svg)](https://github.com/0djentd/token-auth-cli/actions/workflows/python-package.yml)\n[![Pylint](https://github.com/0djentd/token-auth-cli/actions/workflows/pylint.yml/badge.svg)](https://github.com/0djentd/token-auth-cli/actions/workflows/pylint.yml)\n\n# token-auth-cli\n## Description\nSimple tool for testing token authentication during development.\n\n## Installation\n```\npip install token-auth-cli\n```\nor\n```\ngit clone https://github.com/0djentd/token-auth-cli.git\ncd token-auth-cli\npython -m pip install .\n```\n\n## How to use\n```\nUsage: token-auth-cli [OPTIONS] COMMAND [ARGS]...\n\n  token-auth-cli\n\n  Simple tool for testing token authentication during development.\n\nOptions:\n  --verbose / --no-verbose    Show additional information\n  --debug / --no-debug        Show debug information\n  --confirm-settings BOOLEAN  Confirm settings before trying to get token.\n  --show-settings BOOLEAN     Show settings before trying to get token.\n  --api TEXT                  API url.\n  --api-get-token TEXT        API url to use when trying to get token.\n  --api-get TEXT              API url to check if token valid.\n  --config FILE               Config file.\n  --store BOOLEAN             Store users/tokens.\n  --help                      Show this message and exit.\n\nCommands:\n  init     Create config file and users/tokens storage.\n  list     List stored users/tokens.\n  login    Get token and store it.\n  relogin  Try to use stored token for authentication.\n  remove   Remove stored user/token.\n```\n',
    'author': '0djentd',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/0djentd/token-auth-cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
