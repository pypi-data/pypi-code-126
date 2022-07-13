# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dad_sql_pandas']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'dad-sql-pandas',
    'version': '0.1.0',
    'description': 'Pandas implementation of the SQL Data Action Definition for FRIDAAY',
    'long_description': None,
    'author': 'Ernest Prabhakar',
    'author_email': 'ernest.prabhakar@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
