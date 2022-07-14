# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['calculation_test']

package_data = \
{'': ['*']}

install_requires = \
['addict==2.4.0', 'geographiclib==1.50', 'numpy>=1.23.1,<2.0.0']

setup_kwargs = {
    'name': 'calculation-test',
    'version': '0.1.0',
    'description': 'mapilio calculation',
    'long_description': '# DENEME\n',
    'author': 'Kadir Coşar',
    'author_email': 'kadircosarnew@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
