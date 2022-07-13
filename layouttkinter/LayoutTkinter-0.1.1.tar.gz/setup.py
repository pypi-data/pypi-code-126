# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ladder']

package_data = \
{'': ['*']}

install_requires = \
['PySimpleGUI>=4.60.1,<5.0.0']

setup_kwargs = {
    'name': 'layouttkinter',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'TaiHui',
    'author_email': '1174501146@qq.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
