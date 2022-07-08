# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['snx_util']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0', 'tqdm>=4.64.0,<5.0.0']

setup_kwargs = {
    'name': 'snx-util',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'supernovalx',
    'author_email': 'hoanganhgo9@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
