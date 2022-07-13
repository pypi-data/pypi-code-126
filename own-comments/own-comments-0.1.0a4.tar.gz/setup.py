# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['own_comments']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.4.39,<2.0.0',
 'aiosmtplib>=1.1.6,<2.0.0',
 'fastapi>=0.78.0,<0.79.0',
 'pydantic[dotenv]>=1.9.1,<2.0.0',
 'python-multipart>=0.0.5,<0.0.6',
 'uvicorn>=0.18.2,<0.19.0']

setup_kwargs = {
    'name': 'own-comments',
    'version': '0.1.0a4',
    'description': '',
    'long_description': None,
    'author': 'Nicolas Cedilnik',
    'author_email': 'nicolas.cedilnik@inheart.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://sr.ht/~nicoco/own-comments/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
