# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sqlalchemy2strawberry']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.3.16,<2.0.0',
 'pydantic-sqlalchemy>=0.0.9,<0.0.10',
 'pydantic>=1.5.1,<2.0.0',
 'strawberry-graphql>=0.116.4,<0.117.0']

setup_kwargs = {
    'name': 'sqlalchemy2strawberry',
    'version': '0.0.1',
    'description': 'A simple tool to convert SQLAlchemy models to Strawberry types',
    'long_description': '# sqlalchemy2strawberry\nA simple tool to convert SQLAlchemy models to Strawberry types\n',
    'author': 'bichanna',
    'author_email': 'nobu.bichanna@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/bichanna/sqlalchemy2strawberry',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
