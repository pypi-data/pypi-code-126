# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['whatnot']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0', 'gql>=3.3.0,<4.0.0']

setup_kwargs = {
    'name': 'whatnot',
    'version': '0.1.1',
    'description': 'An asynchronous, unofficial Whatnot API wrapper',
    'long_description': "# Whatnot API\n\nVery early work-in-progress asynchronous API wrapper for and documentation of the [Whatnot](https://www.whatnot.com) API.\n\n## Roadmap\n\n- [x] Authentication\n- [x] Get user's livestreams\n- [x] Get a livestream\n- [ ] Get user by ID\n- [ ] Get user by username\n- [ ] Get account information\n- [ ] Get Explore/Recommendations/Saved Streams/etc\n\n## Download\n\n`poetry add whatnot` *or* `pip install whatnot`\n\n## Example\n\n```python\ncode\n```\n\n## Disclaimer\n\nThis project is unofficial and is not affiliated with or endorsed by Whatnot.\n",
    'author': 'wxllow',
    'author_email': 'willow@wxllow.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/wxllow/whatnot',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
