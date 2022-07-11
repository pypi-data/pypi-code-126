# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['python_lambda_builder']

package_data = \
{'': ['*']}

install_requires = \
['toml>=0.10.2,<0.11.0', 'typer[all]>=0.5.0,<0.6.0']

entry_points = \
{'console_scripts': ['python_lambda_builder = python_lambda_builder.build:run']}

setup_kwargs = {
    'name': 'python-lambda-builder',
    'version': '0.1.1',
    'description': 'A CLI application for building lambda python functions and dependencies',
    'long_description': '# Python Lambda Builder\nThis library is a CLI tool to solve the problem of \nbuilding together a python project and its dependencies for lambda \ndeployment. This command with could be integrated into pipeline \nfor deployment.\n\n## Usage\nFor poetry (pyproject.toml):\n```shell\npython_lambda_builder --func-src src/ --build_dest dist/\n```\n\nFor pip (requirements.txt):\n```shell\npython_lambda_builder --func-src src/ --build_dest dist/ --manager pip\n```\n\nOther arguments you can pass include:\n- `pyproject_path`: (defaults to `./pyproject.toml`) This can be the relative or absolute \npath to the pyproject.toml file.\n- `requirements_path`: (defaults to `./requirements.txt`) This can be the relative or absolute \npath to the requirements.txt file.',
    'author': 'Damilola Adeyemi',
    'author_email': 'adeyemidamilola3@gmail.com',
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
