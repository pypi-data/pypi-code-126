# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['audiocodes_exporter', 'audiocodes_exporter.collectors']

package_data = \
{'': ['*']}

install_requires = \
['prometheus-client>=0.14.1,<0.15.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'audiocodes-exporter',
    'version': '0.1.1',
    'description': 'AudioCodes SBC exporter for the Prometheus monitoring system.',
    'long_description': None,
    'author': 'Matthew Neirynck',
    'author_email': 'matthew.neirynck@telsmart.eu',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
