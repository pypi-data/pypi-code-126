# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zntrack',
 'zntrack.core',
 'zntrack.core.functions',
 'zntrack.descriptor',
 'zntrack.dvc',
 'zntrack.interface',
 'zntrack.metadata',
 'zntrack.project',
 'zntrack.utils',
 'zntrack.zn']

package_data = \
{'': ['*']}

install_requires = \
['dot4dict>=0.1.1,<0.2.0',
 'dvc>=2.12.0,<3.0.0',
 'pandas>=1.4.3,<2.0.0',
 'pyyaml>=6.0,<7.0',
 'tqdm>=4.64.0,<5.0.0',
 'znjson>=0.1.2,<0.2.0']

setup_kwargs = {
    'name': 'zntrack',
    'version': '0.4.2',
    'description': 'Create, Run and Benchmark DVC Pipelines in Python',
    'long_description': None,
    'author': 'zincwarecode',
    'author_email': 'zincwarecode@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
