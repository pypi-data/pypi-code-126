# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kuromon']

package_data = \
{'': ['*']}

install_requires = \
['tabulate>=0.8.10,<0.9.0']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=4.12.0,<5.0.0'],
 'pydantic': ['pydantic>=1.6.2,!=1.7,!=1.7.1,!=1.7.2,!=1.7.3,!=1.8,!=1.8.1,<2.0.0']}

setup_kwargs = {
    'name': 'kuromon',
    'version': '0.2.0',
    'description': 'Convert a list of dict, dataclass, Pydantic or POPO objects into a string represented table',
    'long_description': '# kuromon\n\n[![PyPI version](https://badge.fury.io/py/kuromon.svg)](https://badge.fury.io/py/kuromon)\n[![Python CI](https://github.com/ninoseki/kuromon/actions/workflows/test.yml/badge.svg)](https://github.com/ninoseki/kuromon/actions/workflows/test.yml)\n\nConvert a list of dict, dataclass, Pydantic or POPO objects into a string represented table.\n\n## Requirements\n\n- Python 3.7+\n\n## Installation\n\n```bash\npip install kuromon\n# or if you want to use Pydantic along with kuromon\npip install kuromon[pydantic]\n```\n\n## Usage\n\n```py\nfrom kuromon import to_table\n\ndict_data = [\n    {"id": 1, "name": "foo", "tags": None},\n    {"id": 2, "name": "bar", "tags": ["a"]},\n]\nprint(to_table(dict_data))\n# |    |   id | name   | tags   |\n# |----|------|--------|--------|\n# |  0 |    1 | foo    |        |\n# |  1 |    2 | bar    | [\'a\']  |\n\n# Disable indexing by setting index=False\nprint(to_table(dict_data, index=False))\n# |   id | name   | tags   |\n# |------|--------|--------|\n# |    1 | foo    |        |\n# |    2 | bar    | [\'a\']  |\n\n# Change the table format via tablefmt\n# NOTE: You can use the following tabulate formats\n#       https://github.com/astanin/python-tabulate#table-format\nprint(to_table(dict_data, tablefmt="plain"))\n# 0     1  foo\n# 1     2  bar     [\'a\']\n```\n\nThe above example uses a list of dict objects. You can also use a list of dataclass or Pydantic objects.\n\n```py\nfrom dataclasses import dataclass\nfrom typing import List, Optional\n\nfrom dacite import from_dict\nfrom pydantic import BaseModel\n\nfrom kuromon import to_table\n\n\nclass TestModel(BaseModel):\n    id: int\n    name: str\n    tags: Optional[List[str]]\n\n\n@dataclass\nclass TestDataClass:\n    id: int\n    name: str\n    tags: Optional[List[str]]\n\n\ndict_data = [\n    {"id": 1, "name": "foo", "tags": None},\n    {"id": 2, "name": "bar", "tags": ["a"]},\n]\npydantic_data = [TestModel.parse_obj(obj) for obj in dict_data]\ndataclass_data = [from_dict(data_class=TestDataClass, data=obj) for obj in dict_data]\n\nprint(to_table(pydantic_data))\nprint(to_table(dataclass_data))\n```\n',
    'author': 'Manabu Niseki',
    'author_email': 'manabu.niseki@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ninoseki/kuromon',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
