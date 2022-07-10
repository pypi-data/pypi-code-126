# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['rics',
 'rics._internal_support',
 'rics.mapping',
 'rics.performance',
 'rics.translation',
 'rics.translation.dio',
 'rics.translation.fetching',
 'rics.translation.offline',
 'rics.utility',
 'rics.utility.collections']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.1']

extras_require = \
{'plotting': ['matplotlib', 'seaborn'],
 'translation': ['sqlalchemy>=1.0.0', 'toml>=0.10.2']}

setup_kwargs = {
    'name': 'rics',
    'version': '0.13.0',
    'description': 'My personal little ML engineering library.',
    'long_description': '# Readme\n\n<div align="center">\n\n[![PyPI - Version](https://img.shields.io/pypi/v/rics.svg)](https://pypi.python.org/pypi/rics)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/rics.svg)](https://pypi.python.org/pypi/rics)\n[![Tests](https://github.com/rsundqvist/rics/workflows/tests/badge.svg)](https://github.com/rsundqvist/rics/actions?workflow=tests)\n[![Codecov](https://codecov.io/gh/rsundqvist/rics/branch/main/graph/badge.svg)](https://codecov.io/gh/rsundqvist/rics)\n[![Read the Docs](https://readthedocs.org/projects/rics/badge/)](https://rics.readthedocs.io/)\n[![PyPI - License](https://img.shields.io/pypi/l/rics.svg)](https://pypi.python.org/pypi/rics)\n\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)\n\n</div>\n\nMy personal little ML engineering library.\n\n* GitHub repo: <https://github.com/rsundqvist/rics.git>\n* Documentation: <https://rics.readthedocs.io>\n* Free software: MIT\n\n## Setting up for local development\nAssumes a "modern" version of Ubuntu (guide written under `Ubuntu 20.04.2 LTS`) with basic dev dependencies installed.\n\nTo get started, run the following commands:\n\n1. Installing Poetry and Invoke\n   ```bash\n   curl -sSL https://install.python-poetry.org/ | python -\n   pip install invoke\n   ```\n\n2. Installing the project\n   ```bash\n   git clone git@github.com:rsundqvist/rics.git\n   cd rics\n   poetry install -E translation -E plotting\n   inv install-hooks\n   ./run-invocations.sh\n   ```\n   \n    The last step is optional, but serves to verify that the project is ready-to-run.\n\n## Credits\n\nThis package was created with [Cookiecutter][cookiecutter] and\nthe [fedejaure/cookiecutter-modern-pypackage][cookiecutter-modern-pypackage] project template.\n\n[cookiecutter]: https://github.com/cookiecutter/cookiecutter\n[cookiecutter-modern-pypackage]: https://github.com/fedejaure/cookiecutter-modern-pypackage\n',
    'author': 'Richard Sundqvist',
    'author_email': 'richard.sundqvist@live.se',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rsundqvist/rics',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
