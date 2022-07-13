# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['colo']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['colo = colo.colo:colo']}

setup_kwargs = {
    'name': 'colo',
    'version': '1.1.0',
    'description': 'A simple script to print out the 256 terminal colors in various formats',
    'long_description': '# colo\n\nA simple script that prints out the 256 terminal colors in different formats.</br>\nIt can print the numbers, the hex value, rgb,hsi and the ansi escape sequence.</br>\n\n```txt\ncolo --help\nusage: colo [-h] [--ansi] [--hsi] [--rgb] [--number] [--name] [--hex]\n\noptional arguments:\n  -h, --help  show this help message and exit\n  --ansi      bool\n  --hsi       bool\n  --rgb       bool\n  --number    bool\n  --name      bool\n  --hex       bool\n```\n\n![Image](./img/ansi.png)\n\n## How to get\n```sh\npip3 install colo\n```\n',
    'author': 'terminaldweller',
    'author_email': 'thabogre@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/terminaldweller/colo',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
