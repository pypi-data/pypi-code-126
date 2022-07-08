# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['funcker', 'funcker.cli', 'funcker.plug', 'funcker.run']

package_data = \
{'': ['*']}

install_requires = \
['docker>=5.0.3,<6.0.0', 'typer[all]>=0.4.2,<0.5.0']

entry_points = \
{'console_scripts': ['funcker = funcker.cli.main:app']}

setup_kwargs = {
    'name': 'funcker',
    'version': '0.1.1',
    'description': 'plug and run funcker function',
    'long_description': '# Funcker\n\n> plug and run funcker function\n',
    'author': 'romainprignon',
    'author_email': 'pro.rprignon@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
