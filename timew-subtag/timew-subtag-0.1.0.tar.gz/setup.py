# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['timew_subtag']

package_data = \
{'': ['*']}

install_requires = \
['arrow>=1.1.1,<2.0.0',
 'click>=8.0.1,<9.0.0',
 'rich>=10.9.0,<11.0.0',
 'timew>=0.0.22,<0.0.23']

entry_points = \
{'console_scripts': ['subtag = timew_subtag:cli']}

setup_kwargs = {
    'name': 'timew-subtag',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Hayk Khachatryan',
    'author_email': 'hi@hayk.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
