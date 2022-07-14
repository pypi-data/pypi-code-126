# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['setdiff']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['sett = setdiff.sett:run']}

setup_kwargs = {
    'name': 'setdiff',
    'version': '1.0.1',
    'description': 'Sizes of sets of lines of two files',
    'long_description': '# setdiff\nGiven two files, show the size of set difference, union, intersection, and more of their lines.\n\n## Example:\n\nFile a:\n```\n123\na\na\nab\ncd\n```\n\nFile b:\n```\na\na\nab\n456\n```\n### Usage:\n\n`sett a b`\n\nOutput:\n```\n     {A}  4\n       A  5\n     {B}  3\n       B  4\n |A|-|B|  1\n   A ∖ B  2\n   B ∖ A  1\n   A ∪ B  5\n   A ∩ B  2\n```\n\n\n\n',
    'author': 'Ondřej Měkota',
    'author_email': 'ondrej.mekota@me.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pixelneo/setdiff',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
