# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['spiro',
 'spiro.automl',
 'spiro.automl.tf',
 'spiro.automl.torch',
 'spiro.core',
 'spiro.core.backend_config',
 'spiro.core.tf',
 'spiro.dtdg',
 'spiro.dtdg.models.decoder',
 'spiro.dtdg.models.decoder.tf',
 'spiro.dtdg.models.decoder.tf.sequentialDecoder',
 'spiro.dtdg.models.decoder.torch',
 'spiro.dtdg.models.decoder.torch.sequentialDecoder',
 'spiro.dtdg.models.encoder.implicitTimeEncoder',
 'spiro.dtdg.models.encoder.implicitTimeEncoder.tf',
 'tests',
 'tests.automl',
 'tests.automl.tf',
 'tests.core',
 'tests.core.layers.tf',
 'tests.dtdg',
 'tests.dtdg.models.decoder.tf',
 'tests.dtdg.models.decoder.torch',
 'tests.dtdg.models.encoder.tf']

package_data = \
{'': ['*']}

install_requires = \
['click==8.0.1',
 'findspark>=2.0.1,<3.0.0',
 'ogb>=1.3.2,<2.0.0',
 'pyspark>=3.2.1,<4.0.0']

extras_require = \
{':extra == "test"': ['mypy==0.961'],
 'dev': ['tox>=3.20.1,<4.0.0',
         'virtualenv>=20.2.2,<21.0.0',
         'pip>=20.3.1,<21.0.0',
         'twine>=3.3.0,<4.0.0',
         'pre-commit>=2.12.0,<3.0.0',
         'toml>=0.10.2,<0.11.0',
         'bump2version>=1.0.1,<2.0.0',
         'py7zr>=0.17,<0.18',
         'torch==1.10.2',
         'tensorflow>=2.7.0,<2.9'],
 'doc': ['jinja2==3.0.0',
         'mkdocs==1.2.3',
         'mkdocs-include-markdown-plugin>=1.0.0,<2.0.0',
         'mkdocs-material>=6.1.7,<7.0.0',
         'mkdocstrings>=0.15.2,<0.16.0',
         'mkdocs-autorefs>=0.2.1,<0.3.0'],
 'test': ['black>=21.5b2,<22.0',
          'isort>=5.8.0,<6.0.0',
          'flake8>=3.9.2,<4.0.0',
          'flake8-docstrings>=1.6.0,<2.0.0',
          'pytest>=6.2.4,<7.0.0',
          'pytest-cov>=2.12.0,<3.0.0']}

setup_kwargs = {
    'name': 'spirograph',
    'version': '0.0.0',
    'description': 'A tool to help building ML pipeline easier for non technical users..',
    'long_description': '# spirograph\n\n\n[![pypi](https://img.shields.io/pypi/v/spirograph.svg)](https://pypi.org/project/spirograph/)\n[![python](https://img.shields.io/pypi/pyversions/spirograph.svg)](https://pypi.org/project/spirograph/)\n[![Build Status](https://github.com/mcgill-cpslab/spiral/actions/workflows/dev.yml/badge.svg)](https://github.com/mcgill-cpslab/spiral/actions/workflows/dev.yml)\n[![codecov](https://codecov.io/gh/mcgill-cpslab/spiral/branch/main/graphs/badge.svg)](https://codecov.io/github/mcgill-cpslab/spiral)\n\n\n\nA tool to help building ML pipeline easier for non technical users.\n\n\n* Documentation: <https://mcgill-cpslab.github.io/spiral>\n* GitHub: <https://github.com/mcgill-cpslab/spiral>\n* PyPI: <https://pypi.org/project/spirograph/>\n* Free software: Apache-2.0\n\n## Architecture and road map\n\nThe following image shows the overall architecture design of spirograph:\n![alt text](https://github.com/mcgill-cpslab/spiral/blob/master/imgs/architecture.png?raw=true)\n\nAnd here will be the spirograph application design. Some names are out of dated, need further modification.\n![alt text](https://github.com/mcgill-cpslab/spiral/blob/master/imgs/dygraph_app-app.png?raw=true)\n\n\n## Features\n\n* TODO\n\n## Credits\n\nThis package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [waynerv/cookiecutter-pypackage](https://github.com/waynerv/cookiecutter-pypackage) project template.\n',
    'author': 'Yuecai Zhu',
    'author_email': 'zhuyuecai@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mcgill-cpslab/spiral',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<3.10',
}


setup(**setup_kwargs)
