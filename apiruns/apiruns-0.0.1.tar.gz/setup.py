# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['apiruns']

package_data = \
{'': ['*'], 'apiruns': ['.pytest_cache/*', '.pytest_cache/v/cache/*']}

install_requires = \
['flake8>=4.0.1,<5.0.0', 'typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['apiruns = apiruns.main:app']}

setup_kwargs = {
    'name': 'apiruns',
    'version': '0.0.1',
    'description': 'Apiruns CLI is a tool to make self-configurable rest API.',
    'long_description': '# apiruns-cli\n\nApiruns CLI is a tool to make self-configurable rest API. Create an API rest has never been so easy.\n\n## Requirements\n\n- Python 3.6+\n\n## Installation.\n\n```bash\npoetry install\n```\n\n# Example\n\n```bash\napiruns --help\n\n Usage: apiruns [OPTIONS] COMMAND [ARGS]...\n \n╭─ Options───────────────────────────────────────────────────────────────────╮\n│ --help          Show this message and exit.                                │\n╰────────────────────────────────────────────────────────────────────────────╯\n╭─ Commands ─────────────────────────────────────────────────────────────────╮\n│ build                                   Build API                          │\n│ version                                 Get current version.               │\n╰────────────────────────────────────────────────────────────────────────────╯\n```\n',
    'author': 'Jose Salas',
    'author_email': 'jose.salas@apiruns.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/apiruns/apiruns-cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
