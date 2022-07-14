# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['fate', 'fate.cli', 'fate.cli.base', 'fate.cli.command']

package_data = \
{'': ['*']}

install_requires = \
['argcmdr>=0.12,<0.13']

entry_points = \
{'console_scripts': ['fate = fate:main']}

setup_kwargs = {
    'name': 'fate-scheduler',
    'version': '0.0.1.post1',
    'description': 'The operating system-level command scheduler and manager.',
    'long_description': None,
    'author': 'Jesse London',
    'author_email': 'jesselondon@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/chicago-cdac/fate',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
