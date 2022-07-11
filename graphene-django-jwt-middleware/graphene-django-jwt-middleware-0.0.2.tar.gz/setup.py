# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['graphene_django_jwt_middleware']

package_data = \
{'': ['*']}

install_requires = \
['django', 'pyjwt>=2.4.0,<3.0.0']

setup_kwargs = {
    'name': 'graphene-django-jwt-middleware',
    'version': '0.0.2',
    'description': 'Middleware to check JWT validation in GraphQL schemas',
    'long_description': '# Graphene Django JWT Middleware\n\nThis is a [Graphene Django](https://docs.graphene-python.org/projects/django/en/latest/) middleware to check JWT in GraphQL schemas.\n',
    'author': 'Instruct Developers',
    'author_email': 'oss@instruct.com.br',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/instruct-br/graphene-django-jwt-middleware',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
