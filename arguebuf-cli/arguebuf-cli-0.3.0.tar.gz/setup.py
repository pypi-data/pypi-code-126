# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['arguebuf_cli']

package_data = \
{'': ['*']}

install_requires = \
['arguebuf>=0.3.0,<0.4.0', 'deepl-pro>=0.1.4,<0.2.0', 'typer>=0.3.2,<0.4.0']

entry_points = \
{'console_scripts': ['arguebuf = arguebuf_cli.app:cli']}

setup_kwargs = {
    'name': 'arguebuf-cli',
    'version': '0.3.0',
    'description': '',
    'long_description': '# Arguebuf CLI\n',
    'author': 'Mirko Lenz',
    'author_email': 'info@mirko-lenz.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://recap.uni-trier.de',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
