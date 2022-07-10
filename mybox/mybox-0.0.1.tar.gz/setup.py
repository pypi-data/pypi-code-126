# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mybox', 'mybox.package', 'mybox.state']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0', 'requests>=2.28.1,<3.0.0', 'tqdm>=4.64.0,<5.0.0']

setup_kwargs = {
    'name': 'mybox',
    'version': '0.0.1',
    'description': 'Manage the configuration and tools on your workstation without bothering the OS too much',
    'long_description': None,
    'author': 'Alexey Kotlyarov',
    'author_email': 'a@koterpillar.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
