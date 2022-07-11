# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['conf2levels']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'conf2levels',
    'version': '0.1.0',
    'description': 'A configuration reader which reads values stored in two key levels. The first key level is named “section” and the second level “key”.',
    'long_description': None,
    'author': 'Josef Friedrich',
    'author_email': 'josef@friedrich.rocks',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
