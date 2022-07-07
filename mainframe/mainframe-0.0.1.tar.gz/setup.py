# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mainframe']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.4.3,<2.0.0', 'semopy>=2.3.9,<3.0.0']

setup_kwargs = {
    'name': 'mainframe',
    'version': '0.0.1',
    'description': 'Central Repo for datasets',
    'long_description': None,
    'author': 'chrisaddy',
    'author_email': 'chris.william.addy@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
