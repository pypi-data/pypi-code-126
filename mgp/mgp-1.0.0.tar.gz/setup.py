# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['mgp']
setup_kwargs = {
    'name': 'mgp',
    'version': '1.0.0',
    'description': "Memgraph's module for developing MAGE modules. Used only for type hinting!",
    'long_description': '# mgp\n\nPyPi package used for type hinting when creating MAGE modules. The get started\nusing MAGE repository checkout the repository here: https://github.com/memgraph/mage.\n',
    'author': 'MasterMedo',
    'author_email': 'mislav.vuletic@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
