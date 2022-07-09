# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lssr']

package_data = \
{'': ['*']}

install_requires = \
['rich>=12.4.4,<13.0.0']

entry_points = \
{'console_scripts': ['lssr = lssr.__main__:main']}

setup_kwargs = {
    'name': 'lssr',
    'version': '0.2.0',
    'description': 'Alternative ls command.',
    'long_description': '# lssr\n\nAlternative ls command.\n\n[![PyPI](https://img.shields.io/pypi/v/lssr)](https://pypi.python.org/pypi/lssr)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/lssr)](https://pypi.python.org/pypi/lssr)\n[![Tests](https://github.com/seijinrosen/lssr/actions/workflows/tests.yml/badge.svg)](https://github.com/seijinrosen/lssr/actions/workflows/tests.yml)\n[![CodeQL](https://github.com/seijinrosen/lssr/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/seijinrosen/lssr/actions/workflows/codeql-analysis.yml)\n[![codecov](https://codecov.io/gh/seijinrosen/lssr/branch/main/graph/badge.svg)](https://codecov.io/gh/seijinrosen/lssr)\n[![Downloads](https://pepy.tech/badge/lssr)](https://pepy.tech/project/lssr)\n[![Downloads](https://pepy.tech/badge/lssr/month)](https://pepy.tech/project/lssr)\n[![Downloads](https://pepy.tech/badge/lssr/week)](https://pepy.tech/project/lssr)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n',
    'author': 'seijinrosen',
    'author_email': '86702775+seijinrosen@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/seijinrosen',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
