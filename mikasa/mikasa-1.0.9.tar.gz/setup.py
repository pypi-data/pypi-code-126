# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mikasa']

package_data = \
{'': ['*']}

install_requires = \
['typer[all]>=0.4.2,<0.5.0']

entry_points = \
{'console_scripts': ['mikasa = mikasa.main:app']}

setup_kwargs = {
    'name': 'mikasa',
    'version': '1.0.9',
    'description': 'Simple Project Manager ',
    'long_description': '# Simple Projects Manager (mikasa)',
    'author': 'Hussein Naim',
    'author_email': 'phusseinnaim@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
