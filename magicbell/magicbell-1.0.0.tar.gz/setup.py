# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['magicbell', 'magicbell.api', 'magicbell.model']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.0,<0.24.0', 'orjson>=3.7.6,<4.0.0', 'pydantic>=1.9.1,<2.0.0']

setup_kwargs = {
    'name': 'magicbell',
    'version': '1.0.0',
    'description': 'Unofficial Python SDK for MagicBell',
    'long_description': '# magicbell-python-sdk\n\n![magicbell logo purple](./assets/MB_logo_Purple_2800x660.png)\n\nAn unofficial Python SDK for [MagicBell](https://magicbell.com).\n\n[Install](#installation--usage) | [Getting Started](#getting-started) | [Examples](./examples) | [License](./LICENSE) | [Code of Conduct](./CODE_OF_CONDUCT.md) | [Contributing](./CONTRIBUTING.md)\n\n- API Version: 1.0\n- Package Version: 1.0.0\n\n## Requirements\n\nPython 3.8+\n\n## Installation & Usage\n\n### Poetry\n\n```shell\npoetry add magicbell\n```\n\nThen import the package:\n\n```python\nimport magicbell\n```\n\n### Pip\n```shell\npip install magicbell\n```\n\nThen import the package:\n\n```python\nimport magicbell\n```\n\n## Getting Started\n\n```python\nimport magicbell\nfrom magicbell.configuration import Configuration\n\nconfig = Configuration(\n    api_key="YOUR_API_KEY",\n    api_secret="YOUR_API_SECRET",\n)\nasync with magicbell.MagicBell(config) as mb:\n    # Send a notification\n    await mb.realtime.create_notification(\n        magicbell.WrappedNotification(\n            notification=magicbell.Notification(\n                title="My first notification from python!",\n                recipients=[magicbell.Recipient(email="dan@example.com")],\n            )\n        )\n    )\n```\n\n### Authentication\n\nMost API calls require your MagicBell project API Key and API Secret.\nSome API calls (i.e. projects) require your MagicBell user JWT (enterprise only).\n\nSee the [MagicBell API documentation](https://www.magicbell.com/docs/rest-api/reference#authentication) for more information.\n\n### Configuration\n\nConfiguration can be done explicitly using the `magicbell.Configuration` class,\nor implicitly by setting environment variables with the `MAGICBELL_` prefix.\n\n#### Explicit Configuration\n\n```python\nfrom magicbell.configuration import Configuration\n\n\n# Create a configuration object with the required parameters\nconfig = Configuration(\n    api_key="YOUR_API_KEY",\n    api_secret="YOUR_API_SECRET",\n)\n```\n\n#### Implicit Configuration\n\n```shell\nexport MAGICBELL_API_KEY="YOUR_API_KEY"\nexport MAGICBELL_API_SECRET="YOUR_API_SECRET"\n```\n\n```python\nfrom magicbell.configuration import Configuration\n\n\nconfig = Configuration()\n```\n\n### Examples\n\nFor more examples see the [`examples` directory](./examples).\n\n## Contributing\n\nSee [CONTRIBUTING.md](./CONTRIBUTING.md).\n\n-------\n\n<p align="center">Open sourced with ❤️ by <a href="https://noteable.io">Noteable</a> for the community.</p>\n\n[![boost data collaboration with notebooks](./assets/noteable.png)](https://noteable.io)\n',
    'author': 'Elijah Wilson',
    'author_email': 'eli@noteable.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/noteable-io/magicbell-python-sdk',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
