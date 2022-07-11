# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['openldap_schema_parser']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.2,<9.0.0', 'rich>=12.2.0,<13.0.0']

entry_points = \
{'console_scripts': ['schema-parser = openldap_schema_parser.command:cli']}

setup_kwargs = {
    'name': 'openldap-schema-parser',
    'version': '1.1.4',
    'description': 'OpenLDAP schema file parser',
    'long_description': '.. image:: https://img.shields.io/pypi/pyversions/openldap-schema-parser\n   :target: https://pypi.org/project/openldap-schema-parser/\n   :alt: PyPI - Python Version\n.. image:: https://badge.fury.io/py/openldap-schema-parser.svg\n   :target: https://pypi.org/project/openldap-schema-parser/\n.. image:: https://github.com/mypaceshun/openldap-schema-parser/workflows/Test/badge.svg?branch=main&event=push\n   :target: https://github.com/mypaceshun/openldap-schema-parser/actions/workflows/main.yml\n.. image:: https://codecov.io/gh/mypaceshun/openldap-schema-parser/branch/main/graph/badge.svg?token=1H6ZVS122O\n   :target: https://codecov.io/gh/mypaceshun/openldap-schema-parser\n.. image:: https://pepy.tech/badge/openldap-schema-parser\n   :target: https://pypi.org/project/openldap-schema-parser/\n.. image:: https://readthedocs.org/projects/openldap-schema-parser/badge/?version=latest\n   :target: https://openldap-schema-parser.readthedocs.io/ja/latest/?badge=latest\n   :alt: Documentation Status\n\n\nopenldap-schema-parser\n######################\n\nOpenLDAP の schema ファイルをパースします。\n\nRepository\n----------\n\nhttps://github.com/mypaceshun/openldap-schema-parser\n\nDocument\n--------\n\nhttps://openldap-schema-parser.readthedocs.io/ja/latest/\n\nInstall\n-------\n\n::\n\n  $ pip install openldap-schema-parser\n\nCommand Usage\n-------------\n\n::\n\n  Usage: schema-parser [OPTIONS] TARGET\n\n  Options:\n    --version     Show the version and exit.\n    -h, --help    Show this message and exit.\n    --expand-oid  Expand ObjectIdentifier\n\nLibrary Usage\n-------------\n\n::\n\n  from openldap_schema_parser.parser import parse\n\n  result = parse("test.schema")\n  print(result)\n',
    'author': 'KAWAI Shun',
    'author_email': 'shun@osstech.co.jp',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mypaceshun/openldap-schema-parser',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
