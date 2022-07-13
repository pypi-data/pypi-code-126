# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['substack']

package_data = \
{'': ['*']}

install_requires = \
['python-dotenv>=0.20.0,<0.21.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'python-substack',
    'version': '0.0.5',
    'description': 'A Python wrapper around the Substack API.',
    'long_description': '# Python Substack\n\n# Introduction\n\nThis is an unofficial library providing a Python interface for [Substack](https://substack.com/).\nI am in no way affiliated with Substack. It works with\nPython versions from 3.8+.\n\n# Installation\n\nYou can install python-substack using:\n\n    $ pip install python-substack',
    'author': 'Paolo Mazza',
    'author_email': 'mazzapaolo2019@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/hogier/python-substack',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
