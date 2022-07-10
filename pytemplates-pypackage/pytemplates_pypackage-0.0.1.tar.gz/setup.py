# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pytemplates_pypackage', 'pytemplates_pypackage.core']

package_data = \
{'': ['*']}

extras_require = \
{'dev': ['pytest>=7.1.2,<8.0.0',
         'pytest-cov>=3.0.0,<4.0.0',
         'black>=22.3.0,<23.0.0',
         'isort>=5.10.1,<6.0.0',
         'flake8>=4.0.1,<5.0.0',
         'pylint>=2.13.8,<3.0.0',
         'mypy>=0.961,<0.962',
         'pre-commit>=2.19.0,<3.0.0',
         'Sphinx>=4.5.0,<5.0.0',
         'sphinx-rtd-theme>=1.0.0,<2.0.0'],
 'docs': ['Sphinx>=4.5.0,<5.0.0', 'sphinx-rtd-theme>=1.0.0,<2.0.0'],
 'lint': ['black>=22.3.0,<23.0.0',
          'isort>=5.10.1,<6.0.0',
          'flake8>=4.0.1,<5.0.0',
          'pylint>=2.13.8,<3.0.0',
          'mypy>=0.961,<0.962',
          'pre-commit>=2.19.0,<3.0.0'],
 'test': ['pytest>=7.1.2,<8.0.0', 'pytest-cov>=3.0.0,<4.0.0']}

setup_kwargs = {
    'name': 'pytemplates-pypackage',
    'version': '0.0.1',
    'description': 'A template for a python package.',
    'long_description': '```bash\n\n   ___        _____                         _         _\n  / _ \\ _   _/__   \\ ___  _ __ ___   _ __  | |  __ _ | |_  ___  ___\n / /_)/| | | | / /\\// _ \\| \'_ ` _ \\ | \'_ \\ | | / _` || __|/ _ \\/ __|\n/ ___/ | |_| |/ /  |  __/| | | | | || |_) || || (_| || |_|  __/\\__ \\\n\\/      \\__, |\\/    \\___||_| |_| |_|| .__/ |_| \\__,_| \\__|\\___||___/\n        |___/                       |_|\n\n```\n<!-- source - https://patorjk.com/software/taag/#p=display&h=1&f=Ogre&t=PyTemplates -->\n\n[![License](https://img.shields.io/badge/License-Creative%20Commons%20Zero%20v1.0-informational?style=flat)](./LICENSE)\n[![Documentation: Sphinx](https://img.shields.io/badge/Documentation-Sphinx-08476D?style=flat)](https://pytemplate.github.io/python_package/)\n[![codecov](https://codecov.io/gh/PyTemplate/python_package/branch/main/graph/badge.svg?token=HG1NQ8HRA4)](https://codecov.io/gh/PyTemplate/python_package)\n[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/PyTemplate/python_package/main.svg)](https://results.pre-commit.ci/latest/github/PyTemplate/python_package/main)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-151515?style=flat)](https://github.com/psf/black)\n\n## Description\n\nA basic python package template which includes proper package structure with a functioning package installation. The package is built using poetry; metadata and dependency information is stored in the pyproject.toml. This template includes flake8, pylint, isort, and pytest settings with configurations compatible with the black autoformatter. Pylint settings are based on the Google style standards for python and adapted for black compatibility.  Testing is automated using github workflows, codecov.io, and pre-commit.ci. Application deployment is managed using multi-staged docker builds for fast develop/deploy cycles.\n\n## Setup\n\nUsing `poetry`:\n\n```bash\ngit clone https://github.com/crabtr26/pytemplates.git\ncd pytemplates\npoetry install --no-dev\n```\n\n## Usage\n\nFrom a `.py` file:\n\n```python\nimport pytemplates\npytemplates.__version__\npytemplates.greet(user="Jacob")\n\nfrom pytemplates import wish_farewell\nwish_farewell(user="Jacob")\n```\n\n## Development Setup\n\nUsing `poetry`:\n\n```bash\ngit clone https://github.com/crabtr26/pytemplates.git\ncd pytemplates\npoetry install\n```\n\n## Testing\n\nTo run the tests locally using the development environment:\n\n```bash\ncd pytemplates\npoetry run pytest\n```\n\n## Documentation\n\nTo build and view the documentation locally using the development environment:\n\n```bash\ncd pytemplates/docs\nmake html\ngoogle-chrome build/html/index.html\n```\n',
    'author': 'crabtr26',
    'author_email': 'crabtr26@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/PyTemplate/python_package',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
