# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pi_mcp23017']

package_data = \
{'': ['*']}

install_requires = \
['RPi.GPIO>=0.7.1,<0.8.0', 'smbus>=1.1.post2,<2.0']

setup_kwargs = {
    'name': 'pi-mcp23017',
    'version': '1.0.0',
    'description': 'Library to access the I2C MCP23017 Port expander via an raspberry pi',
    'long_description': None,
    'author': 'Andreas Philipp',
    'author_email': 'dev@anphi.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
