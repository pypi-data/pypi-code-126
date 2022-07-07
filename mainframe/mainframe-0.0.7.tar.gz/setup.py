# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mainframe', 'mainframe.components']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.9.1,<2.0.0', 'pyro-ppl>=1.8.1,<2.0.0']

setup_kwargs = {
    'name': 'mainframe',
    'version': '0.0.7',
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
    'python_requires': '>=3.8,<3.10',
}


setup(**setup_kwargs)
