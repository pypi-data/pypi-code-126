# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sqlalchemy_helpers']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.3.0', 'alembic>=1.6.5']

extras_require = \
{'docs': ['Flask>=2.0.0,<3.0.0', 'sphinx>=5.0.0,<6.0.0', 'myst-parser'],
 'flask': ['Flask>=2.0.0,<3.0.0']}

setup_kwargs = {
    'name': 'sqlalchemy-helpers',
    'version': '0.10.0',
    'description': 'SQLAlchemy Helpers',
    'long_description': "# SQLAlchemy Helpers\n\nThis project contains a tools to use SQLAlchemy and Alembic in a project.\n\nIt has a Flask integration, and other framework integrations could be added in the future.\n\nThe full documentation is [on ReadTheDocs](https://sqlalchemy-helpers.readthedocs.io).\n\nYou can install it [from PyPI](https://pypi.org/project/sqlalchemy-helpers/).\n\n![PyPI](https://img.shields.io/pypi/v/sqlalchemy-helpers.svg)\n![Supported Python versions](https://img.shields.io/pypi/pyversions/sqlalchemy-helpers.svg)\n![Tests status](https://github.com/fedora-infra/sqlalchemy-helpers/actions/workflows/tests.yml/badge.svg?branch=develop)\n![Documentation](https://readthedocs.org/projects/sqlalchemy-helpers/badge/?version=latest)\n\n## Features\n\nHere's what sqlalchemy-helpers provides:\n\n- Alembic integration:\n  - programmatically create or upgrade your schema,\n  - get information about schema versions and status\n  - drop your tables without leaving alembic information behind\n  - use a function in your `env.py` script to retrieve the database URL, and\n    thus avoid repeating your configuration in two places.\n  - migration helper functions such as `is_sqlite()` or `exists_in_db()`\n- SQLAlchemy naming convention for easier schema upgrades\n- Automatically activate foreign keys on SQLite\n- Enablement of the `query` property on your models\n- A query function `get_or_create()` that you can call directly or use on your model classes\n- Optional Flask integration: you can use sqlalchemy-helpers outside of a Flask app and feel at home\n- The models created with sqlalchemy-helpers work both inside and outside the Flask application\n  context\n\nThis project has 100% code coverage and aims at reliably sharing some of the basic boilerplate\nbetween applications that use SQLAlchemy.\n\nCheck out the [User Guide](https://sqlalchemy-helpers.readthedocs.io/en/latest/user.html) to learn\nhow to use it in your application, with or without Flask.\n\n## FAQ\n\n- Why not use [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com) and\n  [Flask-Migrate](https://github.com/miguelgrinberg/Flask-Migrate/)?\n\nThose projects are great, but we also have apps that are not based on Flask and that would benefit\nfrom the features provided by sqlalchemy-helpers.\n",
    'author': 'Fedora Infrastructure',
    'author_email': 'admin@fedoraproject.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'http://github.com/fedora-infra/sqlalchemy-helpers',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.0,<4.0.0',
}


setup(**setup_kwargs)
