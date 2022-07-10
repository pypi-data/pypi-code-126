# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['fpob', 'fpob.utils']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'fpob.utils',
    'version': '2.0.0',
    'description': 'Various useful utilities.',
    'long_description': None,
    'author': 'Filip Pobořil',
    'author_email': 'tsuki@fpob.cz',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/fpob-dev/fpob-utils',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
