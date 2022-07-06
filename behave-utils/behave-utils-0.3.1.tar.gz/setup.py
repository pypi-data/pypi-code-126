# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'stubs'}

packages = \
['behave-stubs', 'behave_utils']

package_data = \
{'': ['*'], 'behave-stubs': ['formatter/*']}

install_requires = \
['behave>=1.2,<2.0',
 'jsonpath-python>=1.0,<2.0',
 'orjson>=3.6,<4.0',
 'packaging>=21',
 'parse>=1.19,<2.0',
 'requests>=2.26,<3.0',
 'trio>=0.20.0,<0.21.0',
 'xdg>=5.1,<6.0']

setup_kwargs = {
    'name': 'behave-utils',
    'version': '0.3.1',
    'description': 'Utilities for writing Behave step implementations',
    'long_description': '[![gitlab-ico]][gitlab-link]\n[![pre-commit-ico]][pre-commit-link]\n[![licence-apache2]](/LICENCE.txt)\n[![pipeline-status]][pipeline-report]\n\n\nMiscellaneous Utilities for Behave Tests\n========================================\n\nThis Python package contains various helpful functions and classes for writing behaviour \ntests suites with [Behave](https://behave.readthedocs.io/en/stable/).\n\n\nUsage\n-----\n\nAdd as a Git URL to your project\'s test dependencies:\n\n```\ngit+https://code.kodo.org.uk/dom/behave-utils@v0.2\n```\n\n\n---\n\n[gitlab-ico]:\n  https://img.shields.io/badge/GitLab-code.kodo.org.uk-blue.svg?logo=gitlab\n  "GitLab"\n\n[gitlab-link]:\n  https://code.kodo.org.uk/dom/behave-utils\n  "Behave-Utils at code.kodo.org.uk"\n\n[pre-commit-ico]:\n  https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white\n  "Pre-Commit: enabled"\n\n[pre-commit-link]:\n  https://github.com/pre-commit/pre-commit\n  "Pre-Commit at GitHub.com"\n\n[licence-apache2]:\n  https://img.shields.io/badge/Licence-Apache--2.0-blue.svg\n  "Licence: Apache License 2.0"\n\n[pipeline-status]:\n  https://code.kodo.org.uk/dom/behave-utils/badges/master/pipeline.svg\n\n[pipeline-report]:\n  https://code.kodo.org.uk/dom/behave-utils/pipelines?ref=master\n  "Pipelines"\n',
    'author': 'Dominik Sekotill',
    'author_email': 'dom.sekotill@kodo.org.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://code.kodo.org.uk/dom/behave-utils',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
