# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['assertions']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pyssertions',
    'version': '0.0.1',
    'description': 'A library for writing fluent assertions in tests.',
    'long_description': '# pyssertions\nA Python library for writing fluent assertions in tests.\n',
    'author': 'Michael Dimchuk',
    'author_email': 'michaeldimchuk@gmail.com',
    'maintainer': 'Michael Dimchuk',
    'maintainer_email': 'michaeldimchuk@gmail.com',
    'url': 'https://github.com/michaeldimchuk/pyssertions',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
