# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pcr', 'pcr.model']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'hyperpcr',
    'version': '0.2.6',
    'description': 'Point Cloud Reconstruction with HyperNetwork',
    'long_description': None,
    'author': 'andrearosasco',
    'author_email': 'andrea.rosasco@iit.it',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
