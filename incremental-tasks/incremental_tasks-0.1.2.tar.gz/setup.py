# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['incremental_tasks']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.22.2,<2.0.0']

entry_points = \
{'console_scripts': ['generate_tasks_cli = incremental_tasks:main']}

setup_kwargs = {
    'name': 'incremental-tasks',
    'version': '0.1.2',
    'description': 'A benchmark of progressively more difficult AI tasks to measure learning speed of ML systems ',
    'long_description': 'None',
    'author': 'hugcis',
    'author_email': 'hmj.cisneros@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
