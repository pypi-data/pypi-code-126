# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['funtools']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'rich>=12.5.1,<13.0.0']

setup_kwargs = {
    'name': 'funtools',
    'version': '0.1.0',
    'description': 'Useful fun tools',
    'long_description': None,
    'author': 'ischaojie',
    'author_email': 'zhuzhezhe95@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
