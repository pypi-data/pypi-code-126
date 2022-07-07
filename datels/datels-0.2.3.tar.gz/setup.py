# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['datels']

package_data = \
{'': ['*']}

install_requires = \
['fire>=0.4.0,<0.5.0', 'pandas>=1,<2']

entry_points = \
{'console_scripts': ['datels = datels.core:main']}

setup_kwargs = {
    'name': 'datels',
    'version': '0.2.3',
    'description': '`datels` is a simple CLI that displays a list of dates line by line.',
    'long_description': '# datels\n\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/datels?style=plastic)](https://github.com/joe-yama/datels) [![PyPI - License](https://img.shields.io/pypi/l/datels?style=plastic)](https://github.com/joe-yama/datels) [![PyPI](https://img.shields.io/pypi/v/datels?style=plastic)](https://pypi.org/project/datels/)\n\n`datels` is a simple CLI that displays a list of dates line by line.\n\n## Installation\n\nTo install datels with pip, run: `pip install datels`\n\nTo install datels from source, first clone the repository and then run:\n`python setup.py install`\n\n## Basic Usage\n\n```bash\n$ datels 1994-03-07 1994-03-10\n1994/03/07\n1994/03/08\n1994/03/09\n1994/03/10\n```\n\nif you want to specify formatting,\n\n```bash\n$ datels 1994-03-07 1994-03-10 --sep="-"\n1994-03-07\n1994-03-08\n1994-03-09\n1994-03-10\n\n$ datels 1994-03-07 1994-03-10 --format "%c"\nMon Mar  7 00:00:00 1994\nTue Mar  8 00:00:00 1994\nWed Mar  9 00:00:00 1994\nThu Mar 10 00:00:00 1994\n```\n\nThe strftime to parse time, eg “%Y/%m/%d”. See strftime documentation for more information: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior.\n',
    'author': 'joe-yama',
    'author_email': 's1r0mqme@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/joe-yama/datels',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<3.9',
}


setup(**setup_kwargs)
