# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['envawareconfig']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0', 'python-dotenv>=0.19.2,<0.20.0']

setup_kwargs = {
    'name': 'envawareconfig',
    'version': '0.2.1',
    'description': 'Load configurations from yaml files with automatic environment variable substitution',
    'long_description': '# Envawareconfig\n\nLoad configurations from yaml files with automatic environment variable substitution.\n\n## Installation\n\nwith [pip](https://pip.pypa.io/en/stable/):\n\n`pip install envawareconfig`\n\nwith [poetry](https://python-poetry.org/):\n\n`poetry add envawareconfig`\n\n## QuickStart\n\nSuppose you have a configuration file like this:\n\n```yaml\n# test-config.yaml\ndatabase:\n  name: my-database\n  user: "${DB_USER:admin}"\n  password: "${DB_PASSWORD}"\n```\n\nand that you have set the environment variable `DB_PASSWORD` to `my-secret-password`\nwhile `DB_USER` has been left unset.\n\nthen running the following code:\n\n```python\n# main.py\n\nfrom envawareconfig import load_config\n\nconfig = load_config("tests/test-config.yaml")\n```\n\nwould result in:\n```python\nconfig = {\n    "database": {\n        "name": "my-database",\n        "user": "admin",\n        "password": "my-secret-password"\n    }\n}\n```\n\nNotice that `${DB_PASSWORD}` has been expanded and `${DB_USER:admin}` used the default value.\n',
    'author': 'marcello',
    'author_email': 'marcello.frattini7@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mfrattini7/envawareconfig',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
