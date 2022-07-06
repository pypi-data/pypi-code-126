# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src/repyle'}

packages = \
['repyle']

package_data = \
{'': ['*']}

modules = \
['py']
setup_kwargs = {
    'name': 'repyle',
    'version': '0.0.0',
    'description': 'Python Hot Reloading',
    'long_description': '# repy\nHot Reloading Python Code\n',
    'author': 'Markus Feiks',
    'author_email': 'github@feyx.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
