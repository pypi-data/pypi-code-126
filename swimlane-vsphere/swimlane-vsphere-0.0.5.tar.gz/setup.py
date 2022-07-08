# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['swimlane_vsphere']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.1', 'fire>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['swimlane-vsphere = swimlane_vsphere.__main__:main']}

setup_kwargs = {
    'name': 'swimlane-vsphere',
    'version': '0.0.5',
    'description': 'Swimlane Vsphere',
    'long_description': "# Swimlane Vsphere\n\n[![PyPI](https://img.shields.io/pypi/v/swimlane-vsphere.svg)][pypi status]\n[![Status](https://img.shields.io/pypi/status/swimlane-vsphere.svg)][pypi status]\n[![Python Version](https://img.shields.io/pypi/pyversions/swimlane-vsphere)][pypi status]\n[![License](https://img.shields.io/pypi/l/swimlane-vsphere)][license]\n\n[![Read the documentation at https://swimlane-vsphere.readthedocs.io/](https://img.shields.io/readthedocs/swimlane-vsphere/latest.svg?label=Read%20the%20Docs)][read the docs]\n[![Tests](https://github.com/MSAdministrator/swimlane-vsphere/workflows/Tests/badge.svg)][tests]\n[![Codecov](https://codecov.io/gh/MSAdministrator/swimlane-vsphere/branch/main/graph/badge.svg)][codecov]\n\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]\n\n[pypi status]: https://pypi.org/project/swimlane-vsphere/\n[read the docs]: https://swimlane-vsphere.readthedocs.io/\n[tests]: https://github.com/MSAdministrator/swimlane-vsphere/actions?workflow=Tests\n[codecov]: https://app.codecov.io/gh/MSAdministrator/swimlane-vsphere\n[pre-commit]: https://github.com/pre-commit/pre-commit\n[black]: https://github.com/psf/black\n\n## Features\n\n- TODO\n\n## Requirements\n\n- TODO\n\n## Installation\n\nYou can install _Swimlane Vsphere_ via [pip] from [PyPI]:\n\n```console\n$ pip install swimlane-vsphere\n```\n\n## Usage\n\nPlease see the [Command-line Reference] for details.\n\n## Contributing\n\nContributions are very welcome.\nTo learn more, see the [Contributor Guide].\n\n## License\n\nDistributed under the terms of the [MIT license][license],\n_Swimlane Vsphere_ is free and open source software.\n\n## Issues\n\nIf you encounter any problems,\nplease [file an issue] along with a detailed description.\n\n## Credits\n\nThis project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.\n\n[@cjolowicz]: https://github.com/cjolowicz\n[pypi]: https://pypi.org/\n[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python\n[file an issue]: https://github.com/MSAdministrator/swimlane-vsphere/issues\n[pip]: https://pip.pypa.io/\n\n<!-- github-only -->\n\n[license]: https://github.com/MSAdministrator/swimlane-vsphere/blob/main/LICENSE\n[contributor guide]: https://github.com/MSAdministrator/swimlane-vsphere/blob/main/CONTRIBUTING.md\n[command-line reference]: https://swimlane-vsphere.readthedocs.io/en/latest/usage.html\n",
    'author': 'Josh Rickard',
    'author_email': 'josh.rickard@swimlane.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/MSAdministrator/swimlane-vsphere',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
