# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['raver']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'semver>=2.13.0,<3.0.0', 'tomli>=2.0.1,<3.0.0']

entry_points = \
{'console_scripts': ['raver = raver.cli:cli']}

setup_kwargs = {
    'name': 'raver',
    'version': '3.0.1',
    'description': 'Ratio package management tool.',
    'long_description': '#####\nRaver\n#####\n\nRatio versioning checker.\n\n\n**********\nQuickstart\n**********\n\n\nInstallation\n============\n\nRaver can be installed using ``pip install raver`` for any Python version >=3.9. Or, for\nPoetry managed projects, use ``poetry add -D raver`` to add it as a development\ndependency.\n\n\nUsing raver\n===========\n\nTo just check if Raver can fetch and check your current version, use ``raver`` in your\nfavorite terminal while in your project directory (where ``pyproject.toml`` is).\n\nRaver detects any Python module that is set up using Poetry by default. It will then\ncheck if the version in the module/package\'s main file contains a ``__version__ = "..."``\nline that matches the version in your ``pyproject.toml`` file.\n\n\nCheck w.r.t. git reference\n--------------------------\n\nTo check the current version versus a git branch as reference (e.g. ``origin/master``),\nuse:\n\n``raver --ref origin/master``\n\nwhere ``origin/master`` is the reference branch. It then performs a comparison using\n``git diff`` to check for committed changes. ``-r`` works as well as a shorthand.\n\n\nCheck changelog\n---------------\n\nTo check whether a changelog entry exists for the current version. There are two\nsupported changelog methods, file and directory.\n\n``raver --changelog ./path/to/changelog.rst``\n\nwhere the changelog file can be of any extension. Raver checks whether the earlier\ndetected Python file version (only ``{major}.{minor}.{patch}``, no metadata) is included\nin the document.\n\n``raver --changelog ./path/to/changelog/``\n\nis also allowed, where the changelog directory has to contain an entry in the format of\n``v{major}.{minor}.{patch}*`` of the current version (the star is a glob wildcard).\n\n\nTOML configuration\n------------------\n\nRaver supports TOML configuration! It **takes precedence over** any command-line\nparameters. The following would be a sensible default for raver:\n\n.. code-block:: toml\n\n   [tool.raver]\n   module = "raver"  # Change to your package name or remove to use Poetry\'s entry.\n   reference = "origin/master"\n   changelog = "./doc/source/changelog.rst"\n   debug = false\n\n\n***************\nDeveloper guide\n***************\n\n\nPython packaging information\n============================\n\nThis project is packaged using `poetry <https://python-poetry.org/>`_. Packaging\ninformation as well as dependencies are stored in `pyproject.toml <./pyproject.toml>`_.\n\nInstalling the project and its development dependencies can be done using ``poetry install``.\n\n\nInvoke tasks\n============\n\nMost elemental maintenance tasks can be accomplished using\n[Invoke](https://www.pyinvoke.org/). After installing using ``poetry install`` and\nenabling the environment using ``poetry shell``, you can run all tasks using ``inv\n[taskname]`` or ``invoke [taskname]``. E.g. ``inv docs`` builds the documentation.\n\n\nVersioning\n==========\n\nThis project uses `semantic versioning <https://semver.org>`_. Version increments are\nchecked using `Raver <https://gitlab.com/ratio-case/raver>`_.\n\n\nChangelog\n=========\n\nChangelog format as described by https://keepachangelog.com/ has been adopted.\n',
    'author': 'Ratio Innovations B.V.',
    'author_email': 'info@ratio-case.nl',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/ratio-case/python/raver',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
