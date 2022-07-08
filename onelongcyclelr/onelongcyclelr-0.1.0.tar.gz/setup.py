# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['onelongcyclelr']

package_data = \
{'': ['*']}

install_requires = \
['torch>=1.0.0,<2.0.0']

setup_kwargs = {
    'name': 'onelongcyclelr',
    'version': '0.1.0',
    'description': "An adaptation of pytorch OneCycleLR that doesn't crash when max steps is reached",
    'long_description': '',
    'author': 'Andrea Boscolo Camiletto',
    'author_email': 'abcamiletto@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
