# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['shalaby_demo']

package_data = \
{'': ['*']}

install_requires = \
['typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['shalaby-demo = shalaby_demo.__main__:app']}

setup_kwargs = {
    'name': 'shalaby-demo',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Shalaby-Demo\nThis is my first CLI created by typer and poetry\n',
    'author': 'Shalaby',
    'author_email': 'mhdshalabystar@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
