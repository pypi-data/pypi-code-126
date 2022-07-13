# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['shalaby_cli_demo']

package_data = \
{'': ['*']}

install_requires = \
['typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['shalaby-cli-demo = shalaby_cli_demo.main:app']}

setup_kwargs = {
    'name': 'shalaby-cli-demo',
    'version': '0.1.0',
    'description': 'This is a demo cli app package',
    'long_description': '# SHALABY CLI DEMO\nThis package is a demo for learning how to publish command line interface app\n',
    'author': 'Mohamed Shalaby',
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
