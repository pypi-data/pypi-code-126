# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mailmap_generator']

package_data = \
{'': ['*']}

install_requires = \
['docopt>=0.6.2,<0.7.0', 'pandas>=1.4.3,<2.0.0']

entry_points = \
{'console_scripts': ['mailmap = mailmap_generator.cli:main']}

setup_kwargs = {
    'name': 'mailmap-generator',
    'version': '0.1.1',
    'description': 'A small command line tool to create git .mailmap files from a commit history.',
    'long_description': '# What is this?\n\nThis tool, `mailmap-generator` suggests a Git `.mailmap` file based on the commit history.\nIt is intended to support you when you have a repository for which you do not have a `.mailmap` file yet but want to create one.\n\n\n## Installation\n\n```\npip install mailmap-generator\n```\n\n### Requirements\n\nThe tool requires that `git` is installed and accessible on `PATH`.\n\n\n## How to use it?\n\nYou have to either point the tool to a directory containing a Git repository.\nFrom the terminal, the tool can be run as in the following:\n\n```\nUsage:\n  mailmap <repository>\n  mailmap -h | --help\n  mailmap --version\n\nOptions:\n  -h --help             Show this screen.\n  --version             Show version.\n```\n\nFor example, if you wanted to create a `.mailmap` file for the `psf/requests` repository, it could be done as in the following:\n\n\n```bash\n$ git clone https://github.com/psf/requests\n$ mailmap requests > requests/.mailmap\n$ nano requests/.mailmap\n```\n\nThe above shows, that the tool just prints a suggested `.mailmap` file to stdout. Be aware of that the tool only _suggests_ a `.mailmap` file.\nIt might be wrong. Since the tool maps same author names, you have to inspect and double check if the suggested file is correct.\n\n\nCalling it from code:\n\n```python\nfrom mailmap_generator.mailmap import create_mailmap\n\nmailmap_str = create_mailmap("<path_to_repo>")\n```\n\n\n## How does the tool create the `.mailmap` file?\n\nCurrently, the tool works in two stages. In the first stage, authors with the same email address are mapped to one author name. Secondly, all authors with the exact same name -- and potentially different email addresses -- are mapped to another. That second step might be wrong in case of authors with same names but different email addresses are actually two different persons.\n\n## Alternative tools\n\nVia [StackOverflow](https://stackoverflow.com/questions/6502018/tool-to-automate-building-a-mailmap-file) one finds [`genmailmap.sh`](https://github.com/greenrd/genmailmap/blob/master/genmailmap.sh) and [`mailmap_update.py`](https://github.com/sympy/sympy/blob/181d1e630e248c46917a18e9e9fc1cf0990dff6f/bin/mailmap_update.py). The latter is removed from the project, i.e., not maintained anymore and inner workings of the former is not entirely clear to me :) Therefore, I created this tool.',
    'author': 'HelgeCPH',
    'author_email': 'ropf@itu.dk',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/HelgeCPH/mailmap-generator.git',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
