# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['f1']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'f1-packets',
    'version': '2022.1.0',
    'description': 'Python library for the official F1 game UDP telemetry data',
    'long_description': '# F1 Packets\n\nPython library for the official F1 game UDP telemetry data\n\n## Packet spec generation\n\nTo generate the spec from the official document, follow these steps. Make sure\nthat `cog` is installed (`pipx install cogapp`) before continuing.\n\n- Copy-paste the documentation into `data/spec.h`\n- Comment-out (or delete) anything that is not part of the actual data spec\n- Run `cog -Pr .\\f1\\packets.py` from the root folder.\n\n## Credits\n\nMost of the code is based on\n[Telemetry-F1-2021](https://github.com/chrishannam/Telemetry-F1-2021).',
    'author': 'Gabriele N. Tornetta',
    'author_email': 'phoenix1987@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/P403n1x87/f1-packets',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
