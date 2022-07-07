# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['devind_dictionaries',
 'devind_dictionaries.migrations',
 'devind_dictionaries.models',
 'devind_dictionaries.schema',
 'devind_dictionaries.services',
 'devind_dictionaries.tasks',
 'devind_dictionaries.tests']

package_data = \
{'': ['*'],
 'devind_dictionaries': ['fixtures/*'],
 'devind_dictionaries.tests': ['data/*']}

install_requires = \
['Django>=4.0.5,<5.0.0',
 'beautifulsoup4>=4.11.1,<5.0.0',
 'celery>=5.2.7,<6.0.0',
 'devind-helpers>=1.0.0,<2.0.0',
 'python-dotenv>=0.20.0,<0.21.0',
 'requests>=2.28.0,<3.0.0',
 'strawberry-django-plus>=1.17.0,<2.0.0',
 'strawberry-graphql-django>=0.3.1,<0.4.0',
 'strawberry-graphql>=0.116.4,<0.117.0']

setup_kwargs = {
    'name': 'devind-dictionaries',
    'version': '1.0.0',
    'description': 'Common dictionaries for devind applications',
    'long_description': None,
    'author': 'Victor',
    'author_email': 'lyferov@yandex.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
