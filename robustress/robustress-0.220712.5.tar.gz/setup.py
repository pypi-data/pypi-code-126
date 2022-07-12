# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['robustress']

package_data = \
{'': ['*']}

install_requires = \
['PyQt5>=5.15.7,<6.0.0',
 'lange>=0.2101.24,<0.2102.0',
 'matplotlib>=3.5.2,<4.0.0',
 'numpy>=1.22.0,<1.23.0',
 'scipy>=1.8.1,<2.0.0',
 'sympy>=1.10.1,<2.0.0']

setup_kwargs = {
    'name': 'robustress',
    'version': '0.220712.5',
    'description': '',
    'long_description': None,
    'author': 'davips',
    'author_email': 'dpsabc@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.10',
}


setup(**setup_kwargs)
