# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pypactl']

package_data = \
{'': ['*']}

install_requires = \
['aioconsole>=0.5.0,<0.6.0']

entry_points = \
{'console_scripts': ['pypactl = pypactl.pypactl:main']}

setup_kwargs = {
    'name': 'pypactl',
    'version': '0.1.3',
    'description': 'Sends commands and gets information from PulseAudio.',
    'long_description': None,
    'author': 'Peter Haight',
    'author_email': 'peterh@giantrabbit.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Dawnthorn/pypactl',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
