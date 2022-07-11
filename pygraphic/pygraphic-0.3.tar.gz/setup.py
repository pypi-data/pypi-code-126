# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pygraphic']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.9.1,<2.0.0']

setup_kwargs = {
    'name': 'pygraphic',
    'version': '0.3',
    'description': 'Client-side GraphQL query generator based on Pydantic',
    'long_description': '# pygraphic\n\nClient-side GraphQL query generator based on [pydantic].\n\n## Why?\n\nWorking with GraphQL in Python seems simple... If you\'re fine with dictionaries, lack of\nautocompletion and unexpected errors.\n\nSome tools allow you to generate Python code from GraphQL schemas. One of them, [turms],\neven generates pydantic models from GQL documents. This approach can be problematic:\nqueries are written in GraphQL, not Python, so the codebase you\'re actually working with\nis out of your control; and the main advantage of pydantic — data validation — is\nmissing!\n\n## Workflow\n\nPygraphic is the opposite of [turms]:\n\n1. For each individual query, you define pydantic models that you want to request,\n   optionally with validators and other configuration;\n\n2. Pygraphic converts those definitions to raw GraphQL documents *(basically strings)*;\n\n3. Using a GraphQL or an HTTP client, you make requests with those documents and get\n   back JSON responses;\n\n4. Pydantic converts those responses to instances of the defined models and validates\n   them;\n\n5. You use the validated data, while enjoying autocompletion and type safety!\n\n## Release Checklist\n\nPygraphic is in development stage. Major features might either be missing or work\nincorrectly. The API may change at any time.\n\n- [x] Basic queries\n- [x] Queries with parameters\n- [x] Custom scalars (not needed, comes with pydantic)\n- [ ] Conversion between camelCase and snake_case\n- [ ] Mutations\n- [ ] Subscriptions\n- [x] Tests\n- [ ] Stable codebase\n\n## Example\n\n### Server schema\n``` gql\ntype User {\n  id: int!\n  username: String!\n  friends: [User!]!\n}\n```\n\n### get_all_users.py\n\n``` python\nfrom __future__ import annotations\nfrom pygraphic import GQLQuery, GQLType\n\nclass User(GQLType):\n    id: int\n    username: str\n    friends: list[UserFriend]\n\nclass UserFriend(GQLType):\n    id: int\n    username: str\n\nclass GetAllUsers(GQLQuery):\n    users: list[User]\n```\n\n### main.py\n\n``` python\nimport requests\nfrom .get_all_users import GetAllUsers\n\n# Generate query string\ngql = GetAllUsers.get_query_string()\n\n# Make the request\nurl = "http://127.0.0.1/graphql"\nresponse = requests.post(url, json={"query": gql})\n\n# Extract data from the response\njson = response.json()\ndata = json.get("data")\nif data is None:\n    raise Exception("Query failed", json.get("error"))\n\n# Parse the data\nresult = GetAllUsers.parse_obj(data)\n\n# Print validated data\nfor user in result.users:\n    print(user.username)\n    print(user.friends)\n```\n\n### Generated query string\n\n``` gql\nquery GetAllUsers {\n  users {\n    id\n    username\n    friends {\n      id\n      username\n    }\n  }\n}\n```\n\nSee more in [/examples](https://github.com/lonelyteapot/pygraphic/tree/main/examples).\n\n## Contribution\n\nThis project is developed on [GitHub].\n\nIf you have any general questions or need help — you\'re welcome in the [Discussions]\nsection.\n\nIf you encounter any bugs or missing features — file new [Issues], but make sure to\ncheck the existing ones first.\n\nIf you want to solve an issue, go ahead and create a [Pull Request][Pulls]! It will be\nreviewed and hopefully merged. Help is always appreciated.\n\n## License\n\nCopyright &copy; 2022, Dmitry Semenov. Released under the [MIT license][License].\n\n\n[GitHub]: https://github.com/lonelyteapot/pygraphic\n[Discussions]: https://github.com/lonelyteapot/pygraphic/discussions\n[Issues]: https://github.com/lonelyteapot/pygraphic/issues\n[Pulls]: https://github.com/lonelyteapot/pygraphic/pulls\n[License]: https://github.com/lonelyteapot/pygraphic/blob/main/LICENSE\n\n[pydantic]: https://pypi.org/project/pydantic/\n[turms]: https://pypi.org/project/turms/\n',
    'author': 'Dmitry Semenov',
    'author_email': 'lonelyteapot@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/lonelyteapot/pygraphic',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
