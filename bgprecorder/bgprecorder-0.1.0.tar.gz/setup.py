# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bgprecorder']

package_data = \
{'': ['*']}

install_requires = \
['logzero>=1.7.0,<2.0.0',
 'pickleDB>=0.9.2,<0.10.0',
 'psycopg2-binary>=2.9.3,<3.0.0']

setup_kwargs = {
    'name': 'bgprecorder',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'yas-nyan',
    'author_email': 'yas-nyan@sfc.wide.ad.jp',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
