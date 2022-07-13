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
         'sphinx-rtd-theme>=1.0.0,<2.0.0',
         'bump2version>=1.0.1,<2.0.0'],
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
    'version': '0.1.2',
    'description': 'A production ready python library template.',
    'long_description': '<p align="center">\n  <a href="https://user-images.githubusercontent.com/20674972/178172752-abd4497d-6a0e-416b-9eef-1b1c0dca8477.png">\n    <img src="https://user-images.githubusercontent.com/20674972/178172752-abd4497d-6a0e-416b-9eef-1b1c0dca8477.png" alt="Pytemplates Banner" style="width:100%;">\n  </a>\n</p>\n\n<p align="center">\n  <a href="https://github.com/PyTemplate/python_package/actions/workflows/test.yaml">\n    <img src="https://github.com/PyTemplate/python_package/actions/workflows/test.yaml/badge.svg" alt="Test status">\n  </a>\n\n  <a href="https://github.com/PyTemplate/python_package/actions/workflows/lint.yaml">\n    <img src="https://github.com/PyTemplate/python_package/actions/workflows/lint.yaml/badge.svg" alt="Linting status">\n  </a>\n\n  <!-- <a href="https://github.com/PyTemplate/python_package/actions/workflows/release.yaml">\n    <img src="https://github.com/PyTemplate/python_package/actions/workflows/release.yaml/badge.svg" alt="Release status">\n  </a> -->\n\n  <a href="https://results.pre-commit.ci/latest/github/PyTemplate/python_package/main">\n    <img src="https://results.pre-commit.ci/badge/github/PyTemplate/python_package/main.svg" alt="pre-commit.ci status">\n  </a>\n\n  <a href="https://codecov.io/gh/PyTemplate/python_package">\n    <img src="https://codecov.io/gh/PyTemplate/python_package/branch/main/graph/badge.svg?token=HG1NQ8HRA4" alt="Code coverage status">\n  </a>\n\n  <a href="https://pypi.org/project/pytemplates-pypackage/">\n    <img src="https://badge.fury.io/py/pytemplates_pypackage.svg" alt="PyPI version">\n  </a>\n</p>\n\n## Description\n\n### A production ready python library template\n\n- Metadata and dependency information is stored in the pyproject.toml for compatibility with both [pip](https://pip.pypa.io/en/stable/) and [poetry](https://python-poetry.org/docs/).\n- [Flake8](https://flake8.pycqa.org/en/latest/), [pylint](https://pylint.pycqa.org/en/latest/index.html), [isort](https://pycqa.github.io/isort/), and [pytest](https://docs.pytest.org/en/latest/) configurations are defined to be compatible with the [black](https://black.readthedocs.io/en/stable/) autoformatter.\n- Pylint settings are based on the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) and adapted for black compatibility.\n- Linting tools run automatically before each commit using [pre-commit](https://pre-commit.com/), black, and isort.\n- Test coverage reports are generated during every commit and pull request using [coverage](https://coverage.readthedocs.io/en/6.4.1/) and [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/). All reports are automatically uploaded and archived on [codecov.io](https://about.codecov.io/).\n- Unit tests are written using [pytest](https://docs.pytest.org/en/latest/) and static type checking is provided by [mypy](http://mypy-lang.org/index.html).\n- Package releases to [PyPI](https://pypi.org/) with dynamic versioning provided by [bump2version](https://github.com/c4urself/bump2version) begin automatically whenever a new tag is created in github.\n- [Sphinx](https://www.sphinx-doc.org/en/master/) documentation is automatically generated and deployed to [github pages](https://docs.github.com/en/pages) during every release.\n- Release notes are automatically generated during every release using [github actions](https://docs.github.com/en/actions).\n\n### [Source code documentation](https://pytemplate.github.io/python_package/)\n\n## Installation\n\nTo install the package using `pip`:\n\n```bash\npip install pytemplates_pypackage\n```\n\nTo add the package as a dependency using `poetry`:\n\n```bash\npoetry add pytemplates_pypackage\n```\n\n## Usage\n\nFrom a `.py` file:\n\n```python\nimport pytemplates_pypackage\nprint(pytemplates_pypackage.__version__)\npytemplates_pypackage.greet(user="Jacob")\n\nfrom pytemplates_pypackage import wish_farewell\nwish_farewell(user="Jacob")\n```\n\n## Developer Setup\n\nInstall the package using `poetry`:\n\n```bash\npoetry install\n```\n\nInstall optional dependencies using the `--extras` flag:\n\n```bash\npoetry install --extras={environment}\n```\n\n### Environments\n\n```python\ntest = [\n    "pytest",\n    "pytest-cov",\n]\n\nlint = [\n    "black",\n    "isort",\n    "flake8",\n    "pylint",\n    "mypy",\n    "pre-commit",\n]\n\ndocs = [\n    "Sphinx",\n    "sphinx-rtd-theme",\n]\n\n# Includes all optional dependencies\ndev = [\n    "pytest",\n    "pytest-cov",\n    "black",\n    "isort",\n    "flake8",\n    "pylint",\n    "mypy",\n    "pre-commit",\n    "Sphinx",\n    "sphinx-rtd-theme",\n    "bump2version",\n]\n```\n\n## Commands\n\n- `make clean` - Remove all build, testing, and static documentation files.\n\n- `make test` - Run the tests using pytest.\n\n- `make lint` - Run the linting tools. Includes pre-commit hooks, black, isort, flake8, pylint, and mypy.\n\n- `make check` - Run the test and lint commands, followed by the clean command.\n\n- `make gen-docs` - Generate Sphinx HTML documentation.\n\n- `make docs` - Generate Sphinx HTML documentation and serve it to the browser.\n\n- `make pre-release increment={major/minor/patch}` - Bump the version and create a release tag. Should only be run from the *main* branch. Passes the increment value to bump2version to create a new version number dynamically. The new version number will be added to *\\__version__.py* and *pyproject.toml* and a new commit will be logged. The tag will be created from the new commit.\n\n## Workflows\n\n- `test` - Run the tests on every push/pull_request to the *main* branch. Writes a coverage report using pytest-cov and uploads it to codecov.io. Optional manual trigger in the github actions tab.\n\n- `lint` - Run the linting tools on every push/pull_request to the *main* branch. Includes pre-commit hooks, black, isort, flake8, pylint, and mypy. Optional manual trigger in the github actions tab.\n\n- `docs` - Build the sphinx documentation, publish to the *sphinx-docs* branch, and release to github pages. Runs on a manual trigger in the github actions tab.\n\n- `release` - Build a package distribution, create a github release, and publish the distribution to PyPI whenever a new tag is created. Linting and testing steps must pass before the release steps can begin. Sphinx documentation is automatically published to the *sphinx-docs* branch and hosted on github pages.\n\n## Releases\n\nA release should consist of the following two steps from a tested, linted, and up to date copy of the *main* branch:\n\n1. `make pre-release increment={major/minor/patch}` - Commit the version number bump and create a new tag locally. The version number follows semantic versioning standards (major.minor.patch) and the tag is the version number prepended with a \'v\'.\n\n2. `git push --follow-tags` - Update the *main* branch with only the changes from the version bump. Publish the new tag and kick off the release workflow.\n\n## File Tree\n\n```bash\n.\n├── docs/\n├── LICENSE\n├── Makefile\n├── poetry.lock\n├── pyproject.toml\n├── README.md\n├── src\n│   └── pytemplates_pypackage\n│       ├── core\n│       │   ├── __init__.py\n│       │   ├── module1.py\n│       │   └── module2.py\n│       ├── __init__.py\n│       └── __version__.py\n└── tests\n    ├── __init__.py\n    ├── test_module1.py\n    └── test_module2.py\n```\n\n## Credits\n\n### Other python package templates\n\n- https://github.com/waynerv/cookiecutter-pypackage\n- https://github.com/AllenCellModeling/cookiecutter-pypackage\n\n### Actions\n\n- https://github.com/JamesIves/github-pages-deploy-action\n- https://github.com/softprops/action-gh-release\n',
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
