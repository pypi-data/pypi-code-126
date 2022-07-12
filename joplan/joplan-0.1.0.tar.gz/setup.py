# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['joplan']

package_data = \
{'': ['*']}

install_requires = \
['deltaman>=0.0.4,<0.0.5']

extras_require = \
{'testing': ['pytest>=7.1.2,<8.0.0', 'tox>=3.25.0,<4.0.0']}

setup_kwargs = {
    'name': 'joplan',
    'version': '0.1.0',
    'description': 'Python Simple Job Scheduling.',
    'long_description': "JoPlan - Arrange Jobs as Plan\n=============================\n\n## Installation\n\n```shell\n$ pip install joplan\n```\n\n## Usage\n\n### Demo 1\n\n```python\nimport logging\n\nfrom joplan import take, do, every\n\nlogging.basicConfig(level=logging.INFO)\n\ndef f1():\n    print('Making F1')\n\ndef f2():\n    print('Making F2')\n\ntake(\n    every('2s').do(f1),\n    every('3s').do(f2),\n).run()\n```\n\n### Demo 2\n\n```python\nfrom joplan import take, do, every\n\ntake(\n    do('pkg.mod.func1').every('5s'),\n    do('pkg.mod.func2').every('3m'),\n).run()\n```\n",
    'author': 'Wonder',
    'author_email': 'wonderbeyond@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/wonderbeyond/joplan',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
