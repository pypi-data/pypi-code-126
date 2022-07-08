# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bashsnakegame']

package_data = \
{'': ['*']}

install_requires = \
['colorama>=0.4.5,<0.5.0',
 'pydantic>=1.9.1,<2.0.0',
 'pytimedinput>=2.0.1,<3.0.0',
 'rich>=12.4.4,<13.0.0']

setup_kwargs = {
    'name': 'bashsnakegame',
    'version': '0.1.0',
    'description': 'A Terminal Snake for Terminal Persons',
    'long_description': '# terminal_snake',
    'author': 'sakthiRatnam',
    'author_email': 'sakthiratnam050@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sakthiRathinam/gamesortvisualize',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
