# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pitot']

package_data = \
{'': ['*']}

install_requires = \
['Pint-Pandas>=0.2,<0.3',
 'Pint>=0.19.2,<0.20.0',
 'numpy>=1.23.0,<2.0.0',
 'pandas>=1.4.3,<2.0.0']

setup_kwargs = {
    'name': 'pitot',
    'version': '0.1.0',
    'description': 'Toolbox for aeronautic units and conversions',
    'long_description': '# pitot\n\n',
    'author': 'Xavier Olive',
    'author_email': 'git@xoolive.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
