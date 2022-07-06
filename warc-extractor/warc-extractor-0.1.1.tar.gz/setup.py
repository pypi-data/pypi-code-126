# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['warc_extractor']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['warc-extractor = warc_extractor.warc_extractor:main']}

setup_kwargs = {
    'name': 'warc-extractor',
    'version': '0.1.1',
    'description': 'A simple tool for extracting warc files.',
    'long_description': None,
    'author': 'Ryan Chartier',
    'author_email': 'redrecrm@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://blog.ak-rc.net/2022/06/warc-extractor-update/',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
