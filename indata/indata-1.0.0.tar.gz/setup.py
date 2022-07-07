# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['indata',
 'indata.dataio',
 'indata.exception',
 'indata.plot',
 'indata.table',
 'indata.utils']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.22.3,<2.0.0',
 'pandas>=1.4.2,<2.0.0',
 'plotly>=5.7.0,<6.0.0',
 'tabulate>=0.8.9,<0.9.0']

setup_kwargs = {
    'name': 'indata',
    'version': '1.0.0',
    'description': 'A tool in order to easily generate data quality reports from ABTs, visualize data and manipulate the ABT (analytics base table)',
    'long_description': '[![Author][contributors-shield]][contributors-url]\n[![Apache 2.0 License][license-shield]][license-url]\n![Version][version-shield]\n\n# indata\nInData is a concise project which enables the user to generate data quality reports with ease and also other data exploration and data visualization tools are available\n\n### Goal\nInData should primarily enable the fast generation of data quality reports for continuous and categorical features. Additionally, data visualisation tools are integrated which can help to identify patterns in data.\n\n### How to use it\nFor more information on how the InData package works, visit: https://github.com/RaphSku/indata\n  \n[contributors-url]: https://github.com/RaphSku\n[license-url]: https://github.com/RaphSku/indata/blob/main/LICENSE\n\n[contributors-shield]: https://img.shields.io/badge/Author-RaphSku-orange?style=plastic&labelColor=black\n[license-shield]: https://img.shields.io/badge/License-Apache%202.0-informational?style=plastic&labelColor=black\n[version-shield]: https://img.shields.io/badge/Version-1.0.0-red?style=plastic&labelColor=black\n',
    'author': 'RapSku',
    'author_email': 'rapsku.dev@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/RaphSku/indata',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
