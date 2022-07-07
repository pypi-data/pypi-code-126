# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pcr', 'pcr.model', 'pcr.utils']

package_data = \
{'': ['*']}

install_requires = \
['timm>=0.5.4,<0.6.0']

setup_kwargs = {
    'name': 'hyperpcr',
    'version': '0.3.0',
    'description': 'Point Cloud Reconstruction with HyperNetwork',
    'long_description': None,
    'author': 'andrearosasco',
    'author_email': 'andrea.rosasco@iit.it',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
