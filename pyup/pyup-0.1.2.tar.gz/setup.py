# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyup']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0',
 'loguru>=0.5.3',
 'paramiko>=2.10.2',
 'pymongo[srv]>=4.0.2',
 'pyperclip>=1.8.2',
 'rich>=10.11.0',
 'tqdm>=4.62.3']

entry_points = \
{'console_scripts': ['pyup = pyup:run.main']}

setup_kwargs = {
    'name': 'pyup',
    'version': '0.1.2',
    'description': 'Caddy file server in Python with many additional features!',
    'long_description': '# pyup\n\n## Install\n\n```\npip install pyup\n```\n\n## Getting started\n\n```\nmv .env.example .env\nnano .env  # or any other text editor\ndocker-compose up -d\n```\n\n- Configure `pyup`:\n\n```\npyup --configure\n```\n\n## Basic Usage\n\n```\nusage: pyup [-h] [-d DOMAIN_NAME] [-k] [--overwrite] [-l] [--no-notifications]\n            [-v {0,1,2,3,4,5}] [-p] [--show-config] [--configure]\n            [--save-logs]\n            [files ...]\n\npositional arguments:\n  files                 Files to upload\n\noptional arguments:\n  -h, --help            show this help message and exit\n  -d DOMAIN_NAME, --domain-name DOMAIN_NAME\n                        The domain name to use for the URL\n  -k, --keep-name       Keep the original file name\n  --overwrite           Overwrite if name is kept and the file name already\n                        exists on the server\n  -l, --local-only      Allow uploads from local IP addresses only\n  --no-notifications    Suppress notifications (notifications are supported on\n                        macOS only)\n  -v {0,1,2,3,4,5}, --verbosity-level {0,1,2,3,4,5}\n                        Set the logging verbosity level\n  -p, --parallel        Upload files in parallel\n  --show-config         Show the current configuration and exit\n  --configure           Configure pyup\n  --save-logs           Save logs to a file\n```\n',
    'author': 'Alyetama',
    'author_email': 'malyetama@pm.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
