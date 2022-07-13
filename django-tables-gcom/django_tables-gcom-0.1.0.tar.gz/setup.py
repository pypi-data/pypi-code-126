# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_tables_gcom']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'django-tables-gcom',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Your Name',
    'author_email': 'eltonmeurer2022@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=2.7,<3.0',
}


setup(**setup_kwargs)
