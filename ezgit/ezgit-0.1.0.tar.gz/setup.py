# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ezgit']

package_data = \
{'': ['*']}

install_requires = \
['typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['ezgit = ezgit.ezgit:cli']}

setup_kwargs = {
    'name': 'ezgit',
    'version': '0.1.0',
    'description': 'A cli tool to simplify working with git',
    'long_description': None,
    'author': 'Harold Karibiye',
    'author_email': 'haroldkaribiye@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
