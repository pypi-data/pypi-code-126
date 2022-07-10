# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['les_louisdelatech',
 'les_louisdelatech.extensions',
 'les_louisdelatech.models',
 'les_louisdelatech.utils']

package_data = \
{'': ['*'], 'les_louisdelatech': ['templates/discord/*', 'templates/google/*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0',
 'aiosqlite>=0.17.0,<0.18.0',
 'cryptography>=37.0.4,<38.0.0',
 'discord.py>=1.7.3,<2.0.0',
 'google-api-python-client>=2.52.0,<3.0.0',
 'google-auth-httplib2>=0.1.0,<0.2.0',
 'httpx>=0.23.0,<0.24.0',
 'pyotp>=2.6.0,<3.0.0',
 'sentry-sdk>=1.6.0,<2.0.0',
 'toml>=0.10.2,<0.11.0',
 'tortoise-orm>=0.19.1,<0.20.0']

setup_kwargs = {
    'name': 'les-louisdelatech',
    'version': '0.1.1',
    'description': 'LouisDeLaTech is a discord bot manager for Lyon e-Sport',
    'long_description': '# LouisDeLaTech is a discord bot manager for Lyon e-Sport\n\n[![PyPI](https://img.shields.io/pypi/v/les-louisdelatech.svg)](https://pypi.python.org/pypi/les-louisdelatech)\n[![PyPI versions](https://img.shields.io/pypi/pyversions/les-louisdelatech.svg)](https://pypi.python.org/pypi/les-louisdelatech)\n[![Python test](https://github.com/lyon-esport/LouisDeLaTech/actions/workflows/test.yml/badge.svg)](https://github.com/lyon-esport/LouisDeLaTech/actions/workflows/test.yml)\n[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)\n\n## Requirements\n\n- Python (check version in setup.py)\n\n## Setup\n\n### Discord\n\nCreate a [discord bot](https://discord.com/developers/applications) and get the token\n\n### Google\n\n- Create a [google project](https://console.cloud.google.com/iam-admin)\n- Create a [google service account](https://console.cloud.google.com/iam-admin/serviceaccounts)\n- Enable Google workspace delegation\n- Generate keys and download the file (used by the bot `-g`)\n- [Add required scopes](https://admin.google.com/ac/owl/domainwidedelegation) for the service account (see config.example for the list of scopes)\n\nYou must create [user custom attribute](https://admin.google.com/ac/customschema?hl=fr)\n\n```json\ncustom: {\n pseudo: ""\n discordId: ""\n}\n```\n\n# Install\n\n```bash\npip install les_louisdelatech\n```\n\n# Configure\n\nGenerate a secret_key to encrypt database secrets\n\n```python\n>>> from cryptography.fernet import Fernet\n>>> Fernet.generate_key()\n```\n\nFill `config.toml` with `config.example`\n\n# Run\n\n```bash\npython3 -m les_louisdelatech.main -c config.toml -g google.json\n```\n\n# Dev\n\nInstall [Poetry](https://python-poetry.org/docs/master/#installing-with-the-official-installer) with version >= 1.2.0a1\n\n```bash\npoetry install\npoetry shell\npre-commit install\n```\n\n### Run pre-commit\n```\npre-commit run --all-files\n```\n\n## Licence\n\nThe code is under CeCILL license.\n\nYou can find all details here: <https://cecill.info/licences/Licence_CeCILL_V2.1-en.html>\n\n## Credits\n\nCopyright © Lyon e-Sport, 2021\n\nContributor(s):\n\n- Ortega Ludovic - ludovic.ortega@lyon-esport.fr\n- Etienne "PoPs" G. - etienne.guilluy@lyon-esport.fr\n- Pierre "DrumSlayer" Sarret - pierre.sarret@lyon-esport.fr\n',
    'author': 'Ludovic Ortega',
    'author_email': 'ludovic.ortega@lyon-esport.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/lyon-esport/LouisDeLaTech',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
