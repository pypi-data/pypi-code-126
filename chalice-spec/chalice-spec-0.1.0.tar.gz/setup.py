# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['chalice_spec']

package_data = \
{'': ['*']}

install_requires = \
['apispec>=5.2.2,<6.0.0']

setup_kwargs = {
    'name': 'chalice-spec',
    'version': '0.1.0',
    'description': 'Chalice x APISpec x Pydantic plug-ins',
    'long_description': None,
    'author': 'Jake Wood',
    'author_email': 'jake@testbox.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
