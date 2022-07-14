# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['qlient', 'qlient.aiohttp']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0', 'qlient-core']

setup_kwargs = {
    'name': 'qlient-aiohttp',
    'version': '0.1.0b1',
    'description': 'A blazingly fast and modern graphql client based on qlient-core and aiohttp',
    'long_description': '# Qlient AIOHTTP: Python GraphQL Client\n\n[![DeepSource](https://deepsource.io/gh/qlient-org/python-qlient-aiohttp.svg/?label=active+issues&token=2ZJ0b1dinekjVtwgJHSy286C)](https://deepsource.io/gh/qlient-org/python-qlient-aiohttp/?ref=repository-badge)\n[![DeepSource](https://deepsource.io/gh/qlient-org/python-qlient-aiohttp.svg/?label=resolved+issues&token=2ZJ0b1dinekjVtwgJHSy286C)](https://deepsource.io/gh/qlient-org/python-qlient-aiohttp/?ref=repository-badge)\n[![pypi](https://img.shields.io/pypi/v/qlient-aiohttp.svg)](https://pypi.python.org/pypi/qlient-aiohttp)\n[![versions](https://img.shields.io/pypi/pyversions/qlient-aiohttp.svg)](https://github.com/qlient-org/python-qlient-aiohttp)\n[![license](https://img.shields.io/github/license/qlient-org/python-qlient-aiohttp.svg)](https://github.com/qlient-org/python-qlient-aiohttp/blob/master/LICENSE)\n\nA blazingly fast and modern graphql client based on qlient-core and aiohttp\n\n## Key Features\n\n* Compatible with Python 3.7 and above\n* Build on top of ``qlient-core`` and ``aiohttp``\n* support for subscriptions\n\n## Help\n\nSee the [documentation](https://qlient-org.github.io/python-qlient-aiohttp/site/) for more details.\n\n## Quick Preview\n\n_This preview is using the official [github/graphql/swapi-graphql]() graphql api._\n\n```python\nimport asyncio\n\nfrom qlient.aiohttp import AIOHTTPClient, GraphQLResponse\n\n\nasync def main():\n    async with AIOHTTPClient("https://swapi-graphql.netlify.app/.netlify/functions/index") as client:\n        result: GraphQLResponse = await client.query.film(\n            ["title", "id"],  # fields selection\n            id="ZmlsbXM6MQ=="  # query arguments\n        )\n\n        print(result.request.query)\n        print(result.data)\n\n\nasyncio.run(main())\n```\n\nWhich results in the following query being sent to the server\n\n```graphql\nquery film($id: ID) {\n    film(id: $id) {\n        title\n        id\n    }\n}\n```\n\nAnd returns the body below\n\n```json\n{\n  "film": {\n    "title": "A New Hope",\n    "id": "ZmlsbXM6MQ=="\n  }\n}\n```',
    'author': 'Daniel Seifert',
    'author_email': 'info@danielseifert.ch',
    'maintainer': 'Daniel Seifert',
    'maintainer_email': 'info@danielseifert.ch',
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
