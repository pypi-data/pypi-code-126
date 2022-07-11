# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['deeprecsys',
 'deeprecsys.rl',
 'deeprecsys.rl.agents',
 'deeprecsys.rl.experience_replay',
 'deeprecsys.rl.neural_networks',
 'deeprecsys.tests',
 'deeprecsys.tests.unit']

package_data = \
{'': ['*']}

install_requires = \
['absl-py==0.12.0',
 'gym==0.18.0',
 'more-itertools>=8.7.0,<9.0.0',
 'networkx>=2.5.1,<3.0.0',
 'pandas==0.25.3',
 'scikit-learn>=0.24.1,<0.25.0',
 'simplejson>=3.17.2,<4.0.0',
 'tensorflow>=2.4.1,<3.0.0',
 'torch==1.4.0']

setup_kwargs = {
    'name': 'deeprecsys',
    'version': '0.1.0',
    'description': 'Python Recommender System based on Deep Reinforcement Learning',
    'long_description': None,
    'author': 'Lucas Farris',
    'author_email': 'lucas@farris.com.br',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<3.7',
}


setup(**setup_kwargs)
