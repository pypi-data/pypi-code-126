# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['hunt',
 'hunt.attributes',
 'hunt.cli',
 'hunt.cli.arguments',
 'hunt.database',
 'hunt.filesystem',
 'hunt.steam']

package_data = \
{'': ['*']}

install_requires = \
['colorama>=0.4.5,<0.5.0', 'watchdog>=2.1.9,<3.0.0']

entry_points = \
{'console_scripts': ['hunt-match-telemetry-cli = hunt.cli.app:console_main']}

setup_kwargs = {
    'name': 'hunt-match-telemetry',
    'version': '1.4.0',
    'description': 'Automatically extract match data from Hunt: Showdown matches.',
    'long_description': None,
    'author': 'Anthony Printup',
    'author_email': 'anthony@printup.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/anthonyprintup/hunt-match-telemetry',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
