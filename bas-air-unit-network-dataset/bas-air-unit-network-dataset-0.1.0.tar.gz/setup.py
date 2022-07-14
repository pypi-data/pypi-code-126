# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['bas_air_unit_network_dataset',
 'bas_air_unit_network_dataset.exporters',
 'bas_air_unit_network_dataset.schemas',
 'bas_air_unit_network_dataset.schemas.garmin']

package_data = \
{'': ['*']}

install_requires = \
['Fiona>=1.8.21,<2.0.0',
 'Shapely>=1.8.2,<2.0.0',
 'click>=8.1.3,<9.0.0',
 'gpxpy>=1.5.0,<2.0.0',
 'lxml>=4.9.1,<5.0.0',
 'ulid-py>=1.1.0,<2.0.0']

entry_points = \
{'console_scripts': ['airnet = bas_air_unit_network_dataset.__main__:cli']}

setup_kwargs = {
    'name': 'bas-air-unit-network-dataset',
    'version': '0.1.0',
    'description': 'Data management for waypoints and routes within the British Antarctic Survey Air Unit',
    'long_description': None,
    'author': 'Felix Fennell',
    'author_email': 'felnne@bas.ac.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9.1,<4.0.0',
}


setup(**setup_kwargs)
