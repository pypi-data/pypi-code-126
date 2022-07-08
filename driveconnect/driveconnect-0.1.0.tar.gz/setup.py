# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['driveconnect']

package_data = \
{'': ['*']}

install_requires = \
['pysecstring>=0.1.8,<0.2.0']

setup_kwargs = {
    'name': 'driveconnect',
    'version': '0.1.0',
    'description': 'Test whether a Windows drive is connected, and connect it.',
    'long_description': None,
    'author': 'Gwang-Jin Kim',
    'author_email': 'gwang.jin.kim.phd@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
