# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ucplotter']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'ucplotter',
    'version': '0.1.0',
    'description': 'For plotting (repeating) unit cell images of composite materials',
    'long_description': None,
    'author': 'Rajesh Nakka',
    'author_email': '338rajesh@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
