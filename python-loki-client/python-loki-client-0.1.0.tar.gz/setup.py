# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['grafana_loki_client',
 'grafana_loki_client.api',
 'grafana_loki_client.api.query',
 'grafana_loki_client.models']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=20.1.0', 'httpx>=0.23.0', 'python-dateutil>=2.8.0']

setup_kwargs = {
    'name': 'python-loki-client',
    'version': '0.1.0',
    'description': 'Python client for Grafana Loki',
    'long_description': '# python-loki-client\n\n> WARNING: This is a beta release of the loki-client, the client is incomplete.\n\n![main build status](https://github.com/expobrain/python-loki-client/actions/workflows/main.yml/badge.svg?branch=main)\n\nA client library for accessing Grafana Loki APIs.\n\n## Installation\n\nTo install the client:\n\n```shell\npip install python-loki-client\n```\n\n## Implemented endpoints\n\nThis client is still incomplete and implements only the following endpoints:\n\n- `GET /loki/api/v1/query`\n\n## Usage\n\nFirst, create a client:\n\n```python\nfrom loki_client import Client\n\nclient = Client(base_url="https://loki.grafana.com")\n```\n\nNow call your endpoint and use your models:\n\n```python\nfrom loki_client.models import MyDataModel\nfrom loki_client.api.my_tag import get_my_data_model\nfrom loki_client.types import Response\n\nmy_data: MyDataModel = get_my_data_model.sync(client=client)\n# or if you need more info (e.g. status_code)\nresponse: Response[MyDataModel] = get_my_data_model.sync_detailed(client=client)\n```\n\nOr do the same thing with an async version:\n\n```python\nfrom loki_client.models import MyDataModel\nfrom loki_client.api.my_tag import get_my_data_model\nfrom loki_client.types import Response\n\nmy_data: MyDataModel = await get_my_data_model.asyncio(client=client)\nresponse: Response[MyDataModel] = await get_my_data_model.asyncio_detailed(client=client)\n```\n\nBy default, when you\'re calling an HTTPS API it will attempt to verify that SSL is working correctly. Using certificate verification is highly recommended most of the time, but sometimes you may need to authenticate to a server (especially an internal server) using a custom certificate bundle.\n\n```python\nclient = Client(\n    base_url="https://internal_loki.grafana.com",\n    verify_ssl="/path/to/certificate_bundle.pem",\n)\n```\n\nYou can also disable certificate validation altogether, but beware that **this is a security risk**.\n\n```python\nclient = Client(\n    base_url="https://internal_loki.grafana.com", verify_ssl=False\n)\n```\n\nThings to know:\n\n1. Every path/method combo becomes a Python module with four functions:\n\n   1. `sync`: Blocking request that returns parsed data (if successful) or `None`\n   1. `sync_detailed`: Blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.\n   1. `asyncio`: Like `sync` but the async instead of blocking\n   1. `asyncio_detailed`: Like `sync_detailed` by async instead of blocking\n\n1. All path/query params, and bodies become method arguments.\n1. If your endpoint had any tags on it, the first tag will be used as a module name for the function (my_tag above)\n1. Any endpoint which did not have a tag will be in `grafana_loki_client.api.default`\n\n## Generate code\n\nThis client is automatically generated from the OpenAPI 3.x specs manually defined in `grafana_loki_openapi.yaml`.\n\nAPIs are manually declared in the YAML file by reading the Grafana [Loki API\'s documentation](https://grafana.com/docs/loki/latest/api/).\n\nA code generator tool will use the OpenAPI document to generates a sync/async client.\n\nTo generare an updated copy of the client:\n\n```shell\npoetry install\npoetry run make generate\n```\n',
    'author': 'Daniele Esposti',
    'author_email': 'daniele.esposti@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/expobrain/python-loki-client',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)
