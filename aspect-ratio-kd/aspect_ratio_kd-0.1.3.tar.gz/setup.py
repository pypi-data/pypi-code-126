# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aspect_ratio_kd']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'aspect-ratio-kd',
    'version': '0.1.3',
    'description': 'Aspect Ratio ',
    'long_description': '# Aspect Ratio Project',
    'author': 'Kadir Coşar',
    'author_email': 'kadircosarnew@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
