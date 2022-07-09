# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['notional']

package_data = \
{'': ['*']}

install_requires = \
['html5lib>=1.1,<2.0',
 'notion-client>=1.0.0,<2.0.0',
 'pydantic>=1.9.1,<2.0.0',
 'urllib3>=1.26.10,<2.0.0']

setup_kwargs = {
    'name': 'notional',
    'version': '0.4.2',
    'description': 'A high-level interface for the Notion SDK.',
    'long_description': None,
    'author': 'Jason Heddings',
    'author_email': 'jheddings@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://jheddings.github.io/notional/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
