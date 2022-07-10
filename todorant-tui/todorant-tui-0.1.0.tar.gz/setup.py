# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['todorant_tui', 'todorant_tui.components', 'todorant_tui.views']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.0,<0.24.0',
 'pydantic[dotenv]>=1.9.1,<2.0.0',
 'textual-inputs>=0.2.6,<0.3.0',
 'textual>=0.1.18,<0.2.0']

setup_kwargs = {
    'name': 'todorant-tui',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Artyom Chebotaryov',
    'author_email': 'ideriki@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
