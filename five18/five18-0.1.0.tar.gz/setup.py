# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['five18']

package_data = \
{'': ['*']}

extras_require = \
{':python_version < "3.11"': ['tomli>=2.0.1,<3.0.0']}

setup_kwargs = {
    'name': 'five18',
    'version': '0.1.0',
    'description': 'Utilities for dealing with pyproject.toml files',
    'long_description': "# five18\n\nLightweight library for dealing with your project's pyproject.toml file.\n\n## Installation\n\n```shell\npip install five18\n```\n\n## Usage\n\n### Access [tool table](https://peps.python.org/pep-0518/#tool-table) attributes\n\n```python\nfrom five18 import PyProjectToml\n\npytoml = PyProjectToml()\n\n# get version from poetry tool table\nprint(pytoml.tool_table.poetry.version)\n\n# get dependencies from poetry tool table\nprint(pytoml.tool_table.poetry.dependencies)\n\n# get dev dependencies from poetry tool table\nprint(pytoml.tool_table.poetry.dev_dependencies)\n```\n",
    'author': 'Michael Harris',
    'author_email': 'mharris@luabase.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mharrisb1/five18',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
