# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['py_avataaars_no_png']

package_data = \
{'': ['*'],
 'py_avataaars_no_png': ['templates/*',
                         'templates/clothes/*',
                         'templates/clothes/graphics/*',
                         'templates/face/eyebrow/*',
                         'templates/face/eyes/*',
                         'templates/face/mouth/*',
                         'templates/face/nose/*',
                         'templates/top/*',
                         'templates/top/accessories/*',
                         'templates/top/facial_hair/*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0']

setup_kwargs = {
    'name': 'py-avataaars-no-png',
    'version': '0.1.0',
    'description': 'SVG-Avatar generator library',
    'long_description': None,
    'author': 'Mawoka',
    'author_email': 'mawoka@mawoka.eu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mawoka-myblock/py-avataaars',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
