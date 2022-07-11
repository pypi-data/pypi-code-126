# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rtbhouse_sdk']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.0,<0.24.0', 'inflection>=0.5.1,<0.6.0', 'pydantic>=1.9.0,<2.0.0']

setup_kwargs = {
    'name': 'rtbhouse-sdk',
    'version': '9.0.0',
    'description': 'RTB House SDK',
    'long_description': None,
    'author': 'RTB House Apps Team',
    'author_email': 'apps@rtbhouse.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rtbhouse-apps/rtbhouse-python-sdk',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.2,<4.0',
}


setup(**setup_kwargs)
