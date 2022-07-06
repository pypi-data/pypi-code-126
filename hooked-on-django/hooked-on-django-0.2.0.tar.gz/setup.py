# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hooks', 'hooks.apps', 'hooks.apps.startup']

package_data = \
{'': ['*']}

install_requires = \
['django>=4.0.6,<5.0.0']

setup_kwargs = {
    'name': 'hooked-on-django',
    'version': '0.2.0',
    'description': 'Simple django application to trigger hooked methods.',
    'long_description': '## hooked-on-django \n\n[![Version](https://img.shields.io/pypi/v/hooked--on--django?label=pypi&color=blue&logo=pypi)](https://pypi.org/project/hooked-on-django)\n\n\n### startup hook\n\nAll methods listed under this hook will be executed after Django finishes its startup process.\n\n\n`settings.py`\n\n```python\nINSTALLED_APPS = [\n    ...,\n    "hooks.startup",\n    ...,\n]\n\nDJANGO_HOOKS = {\n    "STARTUP": {\n        "path.to.method": {\n            "delay": 0,\n            "args" : [\n                ...\n            ],\n            "kwargs": {\n                ...\n            },\n        }\n    }\n}\n```\n\n##### examples\n\n```\nfile: /path/to.py\n\ndef method(param1: str, param2: int):\n    ...\n\ndef other(param1: str = "", param2: int = 0):\n    ...\n\ndef another():\n    ... \n```\n\nTo add a hook to each of these methods, the following configuration can be used:\n\n\n```\nDJANGO_HOOKS = {\n    "STARTUP": {\n        "path.to.method": {\n            "delay": 10,\n            "args": ["string", 123456]\n        },\n        "path.to.other": {\n            "kwargs": {\n                "param1": "string", \n                "param2": 123456\n            }\n        },\n        "path.to.other": {},  # No params needed.\n    }\n}\n```\n\nnote: additionaly, the method `method` will be executed after a 10 seconds delay.\n\n🎣️\n',
    'author': 'Fede Calendino',
    'author_email': 'fede@calendino.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/fedecalendino/hooked-on-django',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
