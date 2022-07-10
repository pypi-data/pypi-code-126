# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mybox', 'mybox.package', 'mybox.state']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0', 'requests>=2.28.1,<3.0.0', 'tqdm>=4.64.0,<5.0.0']

setup_kwargs = {
    'name': 'mybox',
    'version': '0.0.2',
    'description': 'Manage the configuration and tools on your workstation without bothering the OS too much',
    'long_description': "# Mybox\n\n🖥️ This is a box. 📦 And it is mine. 🐱\n\nThere are many 🍱 nice things in there. I wouldn't want 🧰 to be without them.\n\nEven if I move 🏠 or work 🏢 I want to be comfortable.\n\n---\n\nManage the configuration and tools on your workstation without bothering the OS\ntoo much (maybe your favorite one isn't supported by `$WORK` or you have\ndifferent ones for different roles).\n\n## Status\n\nIn development, for the current horrible state of affairs see\n[install](https://github.com/koterpillar/desktop/blob/main/install).\n",
    'author': 'Alexey Kotlyarov',
    'author_email': 'a@koterpillar.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/koterpillar/mybox',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
