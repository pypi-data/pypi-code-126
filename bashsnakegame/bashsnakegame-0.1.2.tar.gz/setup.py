# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bashsnakegame']

package_data = \
{'': ['*']}

install_requires = \
['colorama>=0.4.5,<0.5.0',
 'pre-commit>=2.19.0,<3.0.0',
 'pydantic>=1.9.1,<2.0.0',
 'pytimedinput>=2.0.1,<3.0.0',
 'rich>=12.4.4,<13.0.0']

setup_kwargs = {
    'name': 'bashsnakegame',
    'version': '0.1.2',
    'description': 'A Terminal Snake for Terminal Persons',
    'long_description': '# terminal_snake\n\n[![image](https://img.shields.io/pypi/v/bashsnakegame.svg?style=flat)](https://pypi.python.org/pypi/bashsnakegame)\n[![image](https://img.shields.io/github/license/sakthiRathinam/terminal_snake\n)](https://github.com/sakthiRathinam/terminal_snake)\n[![image](https://github.com/sakthiRathinam/terminal_snake/workflows/pypi/badge.svg)](https://github.com/sakthiRathinam/terminal_snake/actions?query=workflow:pypi)\n\nA cli for snake game in python using graph algo and vanilla python without using no gui libraries nothing only logic and python.\n\n## Installation\n\nYou can just install from pypi.\n\n```shell\npip install bashsnakegame\n```\n\n## Quick Start\n### create a python file and paste this  \n```                                                   \nfrom bashsnakegame.game import SnakeGame\n\ndef main():\n    #width will be the first arg and height will be the second arg based on that i will draw the cells in the terminal\n    game = SnakeGame(10,20)\n    game.start_game()\nmain()\n\nCommands:\n  shell  run the python file and your game starts.\n\n```\n## Demo\n![snakegame](https://user-images.githubusercontent.com/61803261/177983429-9dd2361e-2dea-40f2-9e48-dbff87b52f8e.gif)\n\n## License\n\n\nThis project is licensed under the\n[MIT](https://github.com/tortoise/tortoise-cli/blob/main/LICENSE) License.\n',
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
