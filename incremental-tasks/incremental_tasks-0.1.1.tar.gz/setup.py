# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['incremental_tasks']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.22.2,<2.0.0']

setup_kwargs = {
    'name': 'incremental-tasks',
    'version': '0.1.1',
    'description': '',
    'long_description': 'None',
    'author': 'hugcis',
    'author_email': 'hmj.cisneros@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
