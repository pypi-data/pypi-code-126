# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['shaarpec']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.0,<0.24.0', 'oidcish==0.1.2']

setup_kwargs = {
    'name': 'shaarpec',
    'version': '0.1.0',
    'description': 'Client for SHAARPEC Analytics API.',
    'long_description': '# shaarpec-python-client\nPython client for SHAARPEC Analytics API\n',
    'author': 'Erik G. Brandt',
    'author_email': 'erik.brandt@shaarpec.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
