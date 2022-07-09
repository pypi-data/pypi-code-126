# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pypasswordgen', 'pypasswordgen.src']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['pypasswordgen = pypasswordgen:generate_password']}

setup_kwargs = {
    'name': 'pypasswordgen',
    'version': '1.0.1',
    'description': 'A python based random password generator',
    'long_description': '# pypasswordgen\n\nA pyton based random password generator\n\n## System Requirements\n\n-   Python3\n\n## Installation Instructions\n\n```py\npip install pypasswordgen\n```\n\n## Options\n\n```\n -h, --help                     show this help message and exit\n\n  -l LENGTH, --length LENGTH    Length of password\n\n  -n NUMBER, --number NUMBER    Number of passwords to generate\n\n  -o PATH, --output PATH        Path to output file\n\n  -p, --punctuation             Include pupnctuation. If another -p is givenit will ONLY include punctuation.\n\n  -d, --digit                   Include digits. If another -d is given, it will ONLY include digits. -dd takes precedence over -pp.\n\n  -u, --upper                   Include uppercase letters. If another -u is given, it will ONLY include uppercase letters. -uu takes precedence over -pp and -dd.\n```\n',
    'author': 'Muhammad Arslan',
    'author_email': 'Arslanswl909@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Arslan909/pypasswordgen',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
