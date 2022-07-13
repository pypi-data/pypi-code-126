# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['brain_games', 'brain_games.games', 'brain_games.scripts']

package_data = \
{'': ['*']}

install_requires = \
['prompt>=0.4.1,<0.5.0']

entry_points = \
{'console_scripts': ['brain-calc = brain_games.scripts.brain_calc:main',
                     'brain-even = brain_games.scripts.brain_even:main',
                     'brain-games = brain_games.scripts.brain_games:main',
                     'brain-gcd = brain_games.scripts.brain_gcd:main',
                     'brain-prime = brain_games.scripts.brain_prime:main',
                     'brain-progression = '
                     'brain_games.scripts.brain_progression:main']}

setup_kwargs = {
    'name': 'hexlet-code-dddarknight',
    'version': '0.1.0',
    'description': 'Provides oppotunity to play games with mathematical calculations. In version 0.1.0 there are 5 games: calculations of two numbers, identification of an even number, finding the greatest common divisor of given numbers, identification of a prime number, finding missing number in the progression.',
    'long_description': '# Brain Games\nBrain Games is a Python library that provides oppotunity to play games with mathematical calculations.\n\n____\n\n### Hexlet tests and linter status:\n[![Actions Status](https://github.com/Dddarknight/python-project-lvl1/workflows/hexlet-check/badge.svg)](https://github.com/Dddarknight/python-project-lvl1/actions)\n\n![Linter](https://github.com/Dddarknight/python-project-lvl1/actions/workflows/linter.yml/badge.svg)\n\n### CodeClimate:\n<a href="https://codeclimate.com/github/Dddarknight/python-project-lvl1/maintainability"><img src="https://api.codeclimate.com/v1/badges/f0825e54a6e1af78ca05/maintainability" /></a>\n\n## Links\nThis project was built using these tools:\n| Tool | Description |\n|----------|---------|\n| [poetry](https://python-poetry.org/) |  "Python dependency management and packaging made easy" |\n\n## Description\nIn each game you have to give 3 right answers to become a winner, otherwise the game ends. \nYou can play any of the following games:\n| Game name | Description |\n|----------|---------|\n| brain-calc | You need to make calculations with 2 given numbers|\n| brain-even | You need to answer whether the given number is even or not|\n| brain-gcd | You need to find the greatest common divisor of given numbers|\n| brain-prime | You need to answer whether the given number is prime or not|\n| brain-progression | You need to find the missing number in the progression|\n\n\n## Usage\n```\n$ brain-calc\n$ brain-even\n$ brain-gcd\n$ brain-prime\n$ brain-progression\n```\n\n### Asciinema record:\n[![asciinema](https://asciinema.org/a/uESMOk94NHGA705nEkQGoNAQh)](https://asciinema.org/a/uESMOk94NHGA705nEkQGoNAQh)\n\n## License\n[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)\n',
    'author': 'Dddarknight',
    'author_email': '9801677@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Dddarknight/python-project-lvl1',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.10,<4.0.0',
}


setup(**setup_kwargs)
