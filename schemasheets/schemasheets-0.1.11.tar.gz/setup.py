# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['schemasheets', 'schemasheets.conf', 'schemasheets.utils']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.0.3,<4.0.0',
 'bioregistry>=0.4.30,<0.5.0',
 'linkml>=1.2.16,<2.0.0',
 'ontodev-cogs>=0.3.3,<0.4.0']

entry_points = \
{'console_scripts': ['linkml2sheets = '
                     'schemasheets.schema_exporter:export_schema',
                     'sheets2linkml = schemasheets.schemamaker:convert',
                     'sheets2project = '
                     'schemasheets.sheets_to_project:multigen']}

setup_kwargs = {
    'name': 'schemasheets',
    'version': '0.1.11',
    'description': 'Package to author schemas using spreadsheets',
    'long_description': '# Schemasheets - make datamodels using spreadsheets\n\n<p align="center">\n    <a href="https://github.com/linkml/schemasheets/actions/workflows/main.yml">\n        <img alt="Tests" src="https://github.com/linkml/schemasheets/actions/workflows/main.yaml/badge.svg" />\n    </a>\n    <a href="https://pypi.org/project/linkml">\n        <img alt="PyPI" src="https://img.shields.io/pypi/v/linkml" />\n    </a>\n    <a href="https://pypi.org/project/sssom">\n        <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/sssom" />\n    </a>\n    <a href="https://github.com/linkml/schemasheets/blob/main/LICENSE">\n        <img alt="PyPI - License" src="https://img.shields.io/pypi/l/sssom" />\n    </a>\n    <a href="https://github.com/psf/black">\n        <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black">\n    </a>\n</p>\n\n![linkml logo](https://avatars.githubusercontent.com/u/79337873?s=200&v=4)\n![google sheets logo](https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Google_Sheets_logo_%282014-2020%29.svg/175px-Google_Sheets_logo_%282014-2020%29.svg.png)\n\nCreate a [data dictionary]*https://linkml.io/schemasheets/howto/data-dictionaries/) / schema for your data using simple spreadsheets - *no coding required*.\n\n## About\n\nSchemasheets is a framework for managing your schema using\nspreadsheets ([Google Sheets](https://linkml.io/schemasheets/howto/google-sheets/), [Excel](https://linkml.io/schemasheets/howto/excel/)). It works by compiling down to\n[LinkML](https://linkml.io), which can itself be compiled to a variety\nof formalisms, or used for different purposes like data validation\n\n- [installation](https://linkml.io/schemasheets/install/)\n- [basics](https://linkml.io/schemasheets/intro/basics/)\n\n## Documentation\n\nSee the [Schema Sheets Manual](https://linkml.io/schemasheets)\n\n## Quick Start\n\n```bash\npip install schemasheets\n```\n\nYou should then be able to run the following commands:\n\n- sheets2linkml - Convert schemasheets to a LinkML schema\n- linkml2sheets - Convert a LinkML schema to schemasheets\n- sheets2project - Generate an entire set of schema files (JSON-Schema, SHACL, SQL, ...) from Schemasheets\n\n## Companion tools\n\nWe recommend using [COGS](https://linkml.io/schemasheets/howto/google-sheets/) to synchronize your google sheets with local files using a git-like mechanism\n\n## Details\n\n1. Author your schema as a google sheet or excel spreadsheet\n2. [Generate schemas](https://linkml.io/linkml/generators/index.html):\n    - LinkML\n    - SHACL and ShEx\n    - JSON-Schema\n    - SQL DDL\n    - OWL\n3. Get tooling for free:\n    - Data validators\n    - Python bindings\n    - Create a website for your schema\n\n',
    'author': 'cmungall',
    'author_email': 'cjm@berkeleybop.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/linkml/schemasheets',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
