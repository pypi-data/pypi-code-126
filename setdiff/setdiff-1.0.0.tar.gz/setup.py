# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['setdiff']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['sett = setdiff.sett:run']}

setup_kwargs = {
    'name': 'setdiff',
    'version': '1.0.0',
    'description': 'Sizes of sets of lines of two files',
    'long_description': None,
    'author': 'Ondřej Měkota',
    'author_email': 'ondrej.mekota@me.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pixelneo/setdiff',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
