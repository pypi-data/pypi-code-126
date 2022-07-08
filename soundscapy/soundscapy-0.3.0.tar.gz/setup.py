# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['soundscapy', 'soundscapy.test']

package_data = \
{'': ['*'],
 'soundscapy.test': ['test_DB/*',
                     'test_DB/OFF_LocationA1_FULL_2020-12-31/OFF_LocationA1_BIN_2020-12-31/LocationA1_SpectrumData/FFT_Average/*',
                     'test_DB/OFF_LocationA1_FULL_2020-12-31/OFF_LocationA1_BIN_2020-12-31/LocationA1_WAV/*',
                     'test_DB/OFF_LocationA2_FULL_2021-01-01/OFF_LocationA2_BIN_2021-01-01/LocationA2_WAV/*',
                     'test_DB/OFF_LocationB1_FULL_2021-01-13/OFF_LocationB1_BIN_2021-01-13/LocationB1_WAV/*']}

install_requires = \
['jupyter>=1.0.0,<2.0.0',
 'matplotlib>=3.5.2,<4.0.0',
 'openpyxl>=3.0.10,<4.0.0',
 'pandas-flavor>=0.3.0,<0.4.0',
 'pandas>=1.4.3,<2.0.0',
 'pyjanitor>=0.23.1,<0.24.0',
 'seaborn>=0.11.2,<0.12.0']

setup_kwargs = {
    'name': 'soundscapy',
    'version': '0.3.0',
    'description': 'A python library for analysing and visualising soundscape assessments.',
    'long_description': None,
    'author': 'Andrew Mitchell',
    'author_email': 'mitchellacoustics15@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
