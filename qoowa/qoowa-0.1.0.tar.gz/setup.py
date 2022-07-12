# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['qoowa']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'qoowa',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Gen Xu',
    'author_email': 'gen@nimble.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
