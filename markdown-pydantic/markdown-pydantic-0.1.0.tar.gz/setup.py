# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['markdown_pydantic']

package_data = \
{'': ['*']}

install_requires = \
['Markdown>=3.3.7,<4.0.0']

setup_kwargs = {
    'name': 'markdown-pydantic',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Piotr Katolik',
    'author_email': 'katolus@ventress.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
