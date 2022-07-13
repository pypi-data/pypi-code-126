# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['some_models', 'some_models.models']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy[postgresql]>=1.4.33,<2.0.0',
 'passlib[bcrypt]>=1.7.4,<2.0.0',
 'sqlalchemy-utils>=0.38.2,<0.39.0']

setup_kwargs = {
    'name': 'some-models',
    'version': '0.4.1',
    'description': 'Учебная библиотека. Тут находятся orm модели нужные в нескольких микросервисах, что бы не нарушать DRY.',
    'long_description': 'None',
    'author': 'koevgeny10',
    'author_email': 'koevgeny10@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
