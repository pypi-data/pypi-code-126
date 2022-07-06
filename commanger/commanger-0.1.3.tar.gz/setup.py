# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['commanger']

package_data = \
{'': ['*']}

install_requires = \
['colorama>=0.4.5,<0.5.0', 'pyparsing>=3.0.9,<4.0.0']

setup_kwargs = {
    'name': 'commanger',
    'version': '0.1.3',
    'description': 'A easy to use, extremely configurable shell/terminal command manager for python.',
    'long_description': '# Commanger for python\nA easy to use, extremely configurable shell/terminal command manager for python.\n\nAt first it may just look like any other command line parser but it has so much more!\nYou don\'t have to ever configure the parsing yourself, you can just tell it what you wan\'t.\nIt also deals with stray non specfied arguments and I am always adding more!\n## Basic example:\n>#### Importation and initialization\n```py\nfrom commanger import commanger\ncmd = commanger("cmd")\n```\n>#### The main Function and config\n```py\ncmd.basicConfig([1,2,"b"]) #set a basic config\n\n@cmd.command #Attach the main func\ndef main(args): #Take in the args\n    print(args)\n```\n### Places:\n* #### [Docs](https://python-commanger-docs.readthedocs.io/en/latest/)\n* #### [Github](https://github.com/thatrandomperson5/commanger-docs)',
    'author': 'ThatRandomPerson',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
