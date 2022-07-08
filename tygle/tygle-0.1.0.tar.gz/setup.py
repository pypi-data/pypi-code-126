# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tygle', 'tygle.base']

package_data = \
{'': ['*']}

install_requires = \
['aiogoogle==4.0.0', 'pydantic>=1.9.0,<2.0.0']

setup_kwargs = {
    'name': 'tygle',
    'version': '0.1.0',
    'description': 'Typed Google or simply tygle.',
    'long_description': '# **tygle**\n\n**Ty**ped Goo**gle** or simply *~~tiger~~* tygle.  \nCreated using [Aiogoogle](https://github.com/omarryhan/aiogoogle) for interaction with Google APIs and [pydantic](https://github.com/samuelcolvin/pydantic) for typing.\n\n## Work In Progress\n🛑 This is a WIP package. Expect bugs and changes.\n\n## Installation\nIn order to install the package, install tygle itself and APIs you need.  \nFor example:  \n`pip install tygle[tygle-sheets]`\n\n## Supported APIs\nCurrently, tygle only supports following APIs:  \n1. Sheets\n2. Drive',
    'author': 'shmookoff',
    'author_email': 'shmookoff@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/typed-google/tygle',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
