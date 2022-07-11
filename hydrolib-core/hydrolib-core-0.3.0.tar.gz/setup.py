# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hydrolib',
 'hydrolib.core',
 'hydrolib.core.geometry',
 'hydrolib.core.io',
 'hydrolib.core.io.bc',
 'hydrolib.core.io.common',
 'hydrolib.core.io.crosssection',
 'hydrolib.core.io.dimr',
 'hydrolib.core.io.ext',
 'hydrolib.core.io.friction',
 'hydrolib.core.io.ini',
 'hydrolib.core.io.inifield',
 'hydrolib.core.io.mdu',
 'hydrolib.core.io.net',
 'hydrolib.core.io.obs',
 'hydrolib.core.io.onedfield',
 'hydrolib.core.io.polyfile',
 'hydrolib.core.io.rr',
 'hydrolib.core.io.rr.meteo',
 'hydrolib.core.io.rr.topology',
 'hydrolib.core.io.storagenode',
 'hydrolib.core.io.structure',
 'hydrolib.core.io.xyz',
 'hydrolib.core.modeldata']

package_data = \
{'': ['*']}

install_requires = \
['lxml>=4.6,<5.0',
 'meshkernel>=1.0.0,<2.0.0',
 'netCDF4>=1.5,<2.0',
 'numpy>=1.21,<2.0',
 'pydantic[dotenv]>=1.8,<1.9']

setup_kwargs = {
    'name': 'hydrolib-core',
    'version': '0.3.0',
    'description': 'Python wrappers around D-HYDRO Suite.',
    'long_description': '[![Join the chat at https://gitter.im/Deltares/hydrolib](https://badges.gitter.im/Deltares/hydrolib.svg)](https://gitter.im/Deltares/hydrolib?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![ci](https://github.com/Deltares/HYDROLIB-core/actions/workflows/ci.yml/badge.svg)](https://github.com/Deltares/HYDROLIB-core/actions/workflows/ci.yml)\n[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Deltares_HYDROLIB-core&metric=alert_status)](https://sonarcloud.io/dashboard?id=Deltares_HYDROLIB-core)\n\n\n# HYDROLIB-core\nHYDROLIB-core is the core library of Python wrappers around the D-HYDRO model files (input and output) and model engines (kernel libraries).\nIt can serve as the basis for various pre- and postprocessing tools for a modelling workflow of hydrodynamic simulations.\n\n<div align="center">\n<img src="docs/images/HYDROLIB_logo_paths.svg" width="50%">\n</div>\n\n## More information\nMuch more information is available from the dedicated package website.\n\nSome quickstarts:\n* First users: [Installation](https://deltares.github.io/HYDROLIB-core/latest/guides/setup/) and [Tutorials](https://deltares.github.io/HYDROLIB-core/latest/tutorials/steps).\n* Developers: [List of supported functionalities](https://deltares.github.io/HYDROLIB-core/latest/topics/dhydro_support/),\n  [API reference](https://deltares.github.io/HYDROLIB-core/latest/reference/api/), and\n  [How to contribute](https://deltares.github.io/HYDROLIB-core/latest/guides/contributing/).\n* Releases: [hydrolib-core on PyPI](https://pypi.org/project/hydrolib-core/), [ChangeLog](https://deltares.github.io/HYDROLIB-core/latest/changelog/).\n* Known issues and requested features: via [GitHub issues](https://github.com/Deltares/HYDROLIB-core/issues).\n',
    'author': 'Deltares',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://deltares.github.io/HYDROLIB-core',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
