# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['radio_mlbee_client']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.0,<0.24.0',
 'icecream>=2.1.1,<3.0.0',
 'install>=1.3.5,<2.0.0',
 'logzero>=1.7.0,<2.0.0',
 'set-loglevel>=0.1.2,<0.2.0',
 'tenacity>=8.0.1,<9.0.0',
 'typer>=0.4.1,<0.5.0']

entry_points = \
{'console_scripts': ['radio-mlbee-client = radio_mlbee_client.__main__:app']}

setup_kwargs = {
    'name': 'radio-mlbee-client',
    'version': '0.1.0a0',
    'description': 'radio_mlbee_client',
    'long_description': '# radio-mlbee-client\n[![pytest](https://github.com/ffreemt/radio-mlbee-client/actions/workflows/routine-tests.yml/badge.svg)](https://github.com/ffreemt/radio-mlbee-client/actions)[![python](https://img.shields.io/static/v1?label=python+&message=3.8%2B&color=blue)](https://www.python.org/downloads/)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/radio_mlbee_client.svg)](https://badge.fury.io/py/radio_mlbee_client)\n\nradio-mlbee client for talking to radio-mlbee\n\n## Install it\n\n```shell\npip install git+https://github.com/ffreemt/radio-mlbee-client\n# poetry add git+https://github.com/ffreemt/radio-mlbee-client\n# git clone https://github.com/ffreemt/radio-mlbee-client && cd radio-mlbee-client\n```\n\n## Use it\n```python\nfrom radio_mlbee_client import radio_mlbee_client\n\n```\n',
    'author': 'ffreemt',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ffreemt/radio-mlbee-client',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.3,<4.0.0',
}


setup(**setup_kwargs)
