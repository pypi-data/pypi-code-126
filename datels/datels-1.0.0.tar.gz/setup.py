# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['datels']

package_data = \
{'': ['*']}

install_requires = \
['fire>=0.4.0,<0.5.0', 'numpy>=1.21']

entry_points = \
{'console_scripts': ['datels = datels.cli:run']}

setup_kwargs = {
    'name': 'datels',
    'version': '1.0.0',
    'description': '`datels` is a simple CLI that displays a list of dates line by line.',
    'long_description': '# datels\n\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/datels?style=plastic)](https://github.com/joe-yama/datels) [![PyPI - License](https://img.shields.io/pypi/l/datels?style=plastic)](https://github.com/joe-yama/datels) [![PyPI](https://img.shields.io/pypi/v/datels?style=plastic)](https://pypi.org/project/datels/) [![codecov](https://codecov.io/gh/joe-yama/datels/branch/main/graph/badge.svg?token=RCQSYF637E)](https://codecov.io/gh/joe-yama/datels)\n\n`datels` is a simple CLI that displays a list of dates line by line.\n\n## Installation\n\nTo install datels with pip, run: `pip install datels`\n\n## Basic Usage\n\n```bash\n$ datels 1994-03-07 1994-03-10\n1994/03/07\n1994/03/08\n1994/03/09\n1994/03/10\n```\n\n### Date format option\n\n```bash\n$ datels 1994-03-07 1994-03-10 --sep="-"\n1994-03-07\n1994-03-08\n1994-03-09\n1994-03-10\n\n$ datels 1994-03-07 1994-03-10 --format "%c"\nMon Mar  7 00:00:00 1994\nTue Mar  8 00:00:00 1994\nWed Mar  9 00:00:00 1994\nThu Mar 10 00:00:00 1994\n```\n\nSee [strftime documentation](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior) for more information.\n\n### Inclusive option\n\n```bash\n$ datels 1994-03-07 1994-03-10 --inclusive both\n1994/03/07\n1994/03/08\n1994/03/09\n1994/03/10\n\n$ datels 1994-03-07 1994-03-10 --inclusive left\n1994/03/07\n1994/03/08\n1994/03/09\n\n$ datels 1994-03-07 1994-03-10 --inclusive right\n1994/03/08\n1994/03/09\n1994/03/10\n```\n\n## Using in your python code not CLI\n\n```bash\n$ python\n>>> from datels import list_dates\n>>> dates = list_dates("1994-03-07", "1994-03-10", sep="-", inclusive="both")\n>>> dates\n[\'1994-03-07\', \'1994-03-08\', \'1994-03-09\', \'1994-03-10\']\n>>> # list_dates retuens list of string\n>>> type(dates)\n<class \'list\'>\n>>> type(dates[0])\n<class \'str\'>\n```',
    'author': 'joe-yama',
    'author_email': 's1r0mqme@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/joe-yama/datels',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<3.10',
}


setup(**setup_kwargs)
