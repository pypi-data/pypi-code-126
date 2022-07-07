# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['l2s']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'bidict>=0.22.0,<0.23.0',
 'cri-simulations>=1.0,<2.0',
 'matplotlib>=3.5.1,<4.0.0',
 'numba>=0.55.1,<0.56.0',
 'numpy>=1.18']

setup_kwargs = {
    'name': 'l2s',
    'version': '1.0',
    'description': 'CRI User Software',
    'long_description': None,
    'author': 'Justin Frank & Abhinav Uppal',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
