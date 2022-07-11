# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['conf2levels']

package_data = \
{'': ['*']}

install_requires = \
['type-extensions>=0.1.2,<0.2.0']

setup_kwargs = {
    'name': 'conf2levels',
    'version': '0.3.0',
    'description': 'A configuration reader which reads values stored in two key levels. The first key level is named “section” and the second level “key”.',
    'long_description': "A configuration reader which reads values stored in two key levels.\nThe first key level is named ``section`` and the second level ``key``.\n\nargparse arguments (`argparse`): (You have to specify a mapping)\n\n.. code:: python\n\n    mapping = {\n        'section.key': 'args_attribute'\n    }\n\nA python dictionary (`dictonary`):\n\n.. code:: python\n\n    {\n        'section':  {\n            'key': 'value'\n        }\n    }\n\nEnvironment variables (`environ`):\n\n.. code:: shell\n\n    export prefix__section__key=value\n\nINI file (`ini`):\n\n.. code:: ini\n\n    [section]\n    key = value\n",
    'author': 'Josef Friedrich',
    'author_email': 'josef@friedrich.rocks',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
