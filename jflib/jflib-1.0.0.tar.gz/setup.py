# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jflib']

package_data = \
{'': ['*']}

install_requires = \
['requests==2.28.1', 'typing-extensions==4.3.0']

setup_kwargs = {
    'name': 'jflib',
    'version': '1.0.0',
    'description': 'A collection of my Python library snippets. Maybe they are useful for someone else.',
    'long_description': '[![pypi.org](http://img.shields.io/pypi/v/jflib.svg)](https://pypi.python.org/pypi/jflib)\n[![Documentation Status](https://readthedocs.org/projects/jflib/badge/?version=latest)](https://jflib.readthedocs.io/en/latest/?badge=latest)\n\n# jflib\n\nA collection of my Python library snippets. Maybe they are useful for\nsomeone else.\n',
    'author': 'Josef Friedrich',
    'author_email': 'josef@friedrich.rocks',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Josef-Friedrich/jflib',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
