# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hyperpcr', 'hyperpcr.model']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'hyperpcr',
    'version': '0.2.2',
    'description': 'Point Cloud Reconstruction with HyperNetwork',
    'long_description': None,
    'author': 'andrearosasco',
    'author_email': 'andrea.rosasco@iit.it',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
