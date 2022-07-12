# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['oxalis']

package_data = \
{'': ['*']}

install_requires = \
['aio-pika>=8.0.3',
 'aioredis>=2.0.1',
 'async-timeout>=4.0.2',
 'croniter>=1.3.5']

setup_kwargs = {
    'name': 'oxalis',
    'version': '0.2.1',
    'description': 'Distributed async task/job queue',
    'long_description': '',
    'author': 'strongbugman',
    'author_email': 'strongbugman@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
