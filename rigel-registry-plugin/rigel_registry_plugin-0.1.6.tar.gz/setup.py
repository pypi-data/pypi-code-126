# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rigel_registry_plugin', 'rigel_registry_plugin.registries']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.20.52,<2.0.0',
 'docker>=5.0.3,<6.0.0',
 'pydantic>=1.9.0,<2.0.0',
 'rigelcore>=0.1.16,<0.2.0']

setup_kwargs = {
    'name': 'rigel-registry-plugin',
    'version': '0.1.6',
    'description': 'A plugin for Rigel to deploy Docker images to Docker image registries.',
    'long_description': '**ECR Rigel Plugin**',
    'author': 'Pedro Miguel Melo',
    'author_email': 'pedro.m.melo@inesctec.pt',
    'maintainer': 'Pedro Miguel Melo',
    'maintainer_email': 'pedro.m.melo@inesctec.pt',
    'url': 'https://github.com/rigel-ros/rigel_registry_plugin',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
