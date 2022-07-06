# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonemoji']

package_data = \
{'': ['*']}

install_requires = \
['noneprompt>=0.1.0,<0.2.0']

entry_points = \
{'console_scripts': ['nonemoji = nonemoji.__main__:main']}

setup_kwargs = {
    'name': 'nonemoji',
    'version': '0.1.0',
    'description': 'Simple gitmoji cli written in python',
    'long_description': '# Nonemoji\n\n自维护的 gitmoji-cli，删减了部分 emoji\n',
    'author': 'jigsaw',
    'author_email': 'j1g5aw@foxmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.3,<4.0.0',
}


setup(**setup_kwargs)
