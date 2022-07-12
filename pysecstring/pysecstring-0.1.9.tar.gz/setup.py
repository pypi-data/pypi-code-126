# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pysecstring']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pysecstring',
    'version': '0.1.9',
    'description': "Python implementation of Window's Securestring forked from aznashwan/py-securestring",
    'long_description': "This package serves as a mean to save passwords securely in Windows 10 machines.\nIt uses PowerShell's `SecureString` function and objects.\n\n# Installation\n\nYou install this package simply from PyPI.org by:\n\n```\npip install pysecstring\n```\n\nYou could pip install directly from this github repository - which is the development repository.\n\nAlso, you could install it by git cloning this repository and `poetry install` it.\n\n```\ngit clone https://github.com/gwangjinkim/pysecstring.git\n\ncd pysecstring\npoetry install\n```\n\n# Usage\n\nThe functions `encrypt()` and `decrypt()` serve as pure Python equivalents of the `ConvertTo-SecureString` (or `Read-Host -AsSecureString`) and the `ConvertFrom-SecureString` functions in PowerShell.\n\n`set_credentials()` asks you for entering your username and password (starred input), which will store your credentials in two separate files in form of `SecureStrings`\n(hexed binary - with a seed generated inside your computer).\n\n`get_credentials()` reads these stored files and packs the credentials into a `CredentialObject` also known from PowerShell (but a Python equivalent version of it).\nWhen probing for `.password` and `.username` properties from this credential, property-methods decrypt them immediately into plain text (but they are nowhere stored in plain text form - to enhance safety).\n\nAt any time point and place in your script, username and password are stored only in their encrypted form.\n\n`set_credentials()` and `get_credentials()` work only when run on the same machine. Because different machines use different salts for encryption and decryption.\n\n```\n# save your credentials in the files `.\\.user` and `.\\.pass` in your machine:\nusername_file = '.\\.user'\npass_file = '.\\.pass'\nset_credentials(username_file, pass_file)\n# then PowerShell asks you for input of username and pass\n# and these are stored in the username and pass files in an encrypted form - SecureString\n\n# reads-in the SecureStrings and return them as one credential object\nco = get_credentials(username_file, pass_file) \n\n\n# these credential object you can probe using property methods to get the decrypted plain text forms on the fly\nco.username # returns decrypted username\nco.password # returns decrypted password\n# the decryption happens when the properties are called (property objects)\n```\n\nThis repository started as a fork of `aznashwan/py-securestring`.\n",
    'author': 'Gwang-Jin Kim',
    'author_email': 'gwang.jin.kim.phd@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
