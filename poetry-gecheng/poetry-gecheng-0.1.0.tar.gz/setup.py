# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poetry_gecheng']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'poetry-gecheng',
    'version': '0.1.0',
    'description': 'test',
    'long_description': None,
    'author': 'Cheng Ge',
    'author_email': '13851520957@163.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
