# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tavolo']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.19.0,<2.0.0', 'tensorflow>=2.7.2,<3.0.0', 'toml>=0.10.2,<0.11.0']

setup_kwargs = {
    'name': 'tavolo',
    'version': '0.8.0',
    'description': 'Collection of deep learning modules and layers for the TensorFlow framework',
    'long_description': None,
    'author': 'elior',
    'author_email': 'elior.cohen.p@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<3.10',
}


setup(**setup_kwargs)
