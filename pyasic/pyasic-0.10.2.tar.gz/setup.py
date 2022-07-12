# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyasic',
 'pyasic.API',
 'pyasic.config',
 'pyasic.data',
 'pyasic.data.error_codes',
 'pyasic.logger',
 'pyasic.miners',
 'pyasic.miners._backends',
 'pyasic.miners._types',
 'pyasic.miners._types.antminer',
 'pyasic.miners._types.antminer.X17',
 'pyasic.miners._types.antminer.X19',
 'pyasic.miners._types.antminer.X9',
 'pyasic.miners._types.avalonminer',
 'pyasic.miners._types.avalonminer.A10X',
 'pyasic.miners._types.avalonminer.A7X',
 'pyasic.miners._types.avalonminer.A8X',
 'pyasic.miners._types.avalonminer.A9X',
 'pyasic.miners._types.whatsminer',
 'pyasic.miners._types.whatsminer.M2X',
 'pyasic.miners._types.whatsminer.M3X',
 'pyasic.miners.antminer',
 'pyasic.miners.antminer.bmminer',
 'pyasic.miners.antminer.bmminer.X17',
 'pyasic.miners.antminer.bmminer.X19',
 'pyasic.miners.antminer.bmminer.X9',
 'pyasic.miners.antminer.bosminer',
 'pyasic.miners.antminer.bosminer.X17',
 'pyasic.miners.antminer.bosminer.X19',
 'pyasic.miners.antminer.bosminer.X9',
 'pyasic.miners.antminer.cgminer',
 'pyasic.miners.antminer.cgminer.X17',
 'pyasic.miners.antminer.cgminer.X19',
 'pyasic.miners.antminer.cgminer.X9',
 'pyasic.miners.antminer.hiveon',
 'pyasic.miners.antminer.hiveon.X9',
 'pyasic.miners.avalonminer',
 'pyasic.miners.avalonminer.cgminer',
 'pyasic.miners.avalonminer.cgminer.A10X',
 'pyasic.miners.avalonminer.cgminer.A7X',
 'pyasic.miners.avalonminer.cgminer.A8X',
 'pyasic.miners.avalonminer.cgminer.A9X',
 'pyasic.miners.whatsminer',
 'pyasic.miners.whatsminer.btminer',
 'pyasic.miners.whatsminer.btminer.M2X',
 'pyasic.miners.whatsminer.btminer.M3X',
 'pyasic.misc',
 'pyasic.network',
 'pyasic.settings',
 'pyasic.tests',
 'pyasic.tests.network_tests']

package_data = \
{'': ['*']}

install_requires = \
['asyncssh>=2.11.0,<3.0.0',
 'httpx>=0.23.0,<0.24.0',
 'passlib>=1.7.4,<2.0.0',
 'pyaml>=21.10.1,<22.0.0',
 'toml>=0.10.2,<0.11.0']

setup_kwargs = {
    'name': 'pyasic',
    'version': '0.10.2',
    'description': 'A set of modules for interfacing with many common types of ASIC bitcoin miners, using both their API and SSH.',
    'long_description': None,
    'author': 'UpstreamData',
    'author_email': 'brett@upstreamdata.ca',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
