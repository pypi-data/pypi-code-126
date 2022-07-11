# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['python_lambda_builder']

package_data = \
{'': ['*']}

install_requires = \
['toml>=0.10.2,<0.11.0', 'typer>=0.5.0,<0.6.0']

setup_kwargs = {
    'name': 'python-lambda-builder',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Python Lambda Builder\nThis library is a simple side project to solve the problem of \nbuilding together a python project and its dependencies for lambda \ndeployment. This command with could be integrated into pipeline \nfor deployment.\n\n## Usage\nFor poetry:\n',
    'author': 'Damilola Adeyemi',
    'author_email': 'adeyemidamilola3@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
