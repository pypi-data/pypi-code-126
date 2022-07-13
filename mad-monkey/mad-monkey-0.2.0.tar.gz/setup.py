# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mad_monkey']

package_data = \
{'': ['*']}

install_requires = \
['typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['monkey = mad_monkey.main:app']}

setup_kwargs = {
    'name': 'mad-monkey',
    'version': '0.2.0',
    'description': '',
    'long_description': "\n<h1 align='center'>Mad Monkey</h1>\n\n![Mad Monkey](https://raw.githubusercontent.com/Aadityansha/Mad-Monkey/main/Mad%20Monkey.png)\n\n\n<p align='center'>Mad Monkey is a command-line utility which helps developers to view file without opening it.</p>\n\n> Just like cat command in linux and unix\n## Installation\n\nInstall Mad Monkey with pip\n\n```bash\npip install mad-monkey\n```\n    \n## Usage\n\n```bash\nmonkey <path-to-file>\n```\n\n## Examples\n\nI have created a file `hello-world.txt` and running monkey command to view this file.\n\n```bash\nmonkey hello-world.txt\n```\n\n**Output**\n```txt\nHello world\n```\n\n\n## Authors\n\n- [@Aadityansha](https://www.github.com/Aadityansha)\n\n\n## License\n\n[MIT](https://github.com/Aadityansha/Mad-Monkey/blob/main/LICENSE)\n\n",
    'author': 'Aadityansha',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
