# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pippy_ls']

package_data = \
{'': ['*']}

install_requires = \
['feedparser>=5.2.0', 'html2text', 'tomli>=2.0.1']

entry_points = \
{'console_scripts': ['pippy_ls = pippy_ls.__main__:main']}

setup_kwargs = {
    'name': 'pippy-ls',
    'version': '1.1.0',
    'description': 'An open-source python package',
    'long_description': '## pippy long stockings\nA Python library\n\n',
    'author': 'Pippy Long Stockings',
    'author_email': 'zpprado@email.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pradoz/pippy-ls',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
