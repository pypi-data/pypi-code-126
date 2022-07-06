# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['celery_gsheets']

package_data = \
{'': ['*']}

install_requires = \
['celery>=5.2.7,<6.0.0',
 'pygsheets>=2.0.5,<3.0.0',
 'python-decouple>=3.6,<4.0',
 'redis>=4.3.4,<5.0.0']

setup_kwargs = {
    'name': 'celery-gsheets',
    'version': '0.1.0',
    'description': 'A celery package for gsheets',
    'long_description': None,
    'author': 'David Jeong',
    'author_email': 'drumrobot@1do.space',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
