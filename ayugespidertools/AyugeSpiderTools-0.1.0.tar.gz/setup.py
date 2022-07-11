# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ayugespidertools']

package_data = \
{'': ['*']}

install_requires = \
['PyExecJS==1.5.1', 'pytest==5.2.0']

setup_kwargs = {
    'name': 'ayugespidertools',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'ayuge',
    'author_email': 'ayuge.s@qq.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
