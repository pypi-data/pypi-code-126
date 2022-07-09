# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['goobook']

package_data = \
{'': ['*']}

install_requires = \
['google-api-python-client>=1.7.12,<2.0.0',
 'oauth2client>=1.5.0,<5.0.0dev',
 'pyxdg>=0.28,<0.29',
 'setuptools>=62.6.0,<63.0.0',
 'simplejson>=3.16.0,<4.0.0']

entry_points = \
{'console_scripts': ['goobook = goobook.application:main']}

setup_kwargs = {
    'name': 'goobook',
    'version': '3.5.2',
    'description': 'Search your google contacts from the command-line or mutt.',
    'long_description': ':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\nGooBook -- Access your Google contacts from the command line.\n:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n\n.. contents:: **Table of Contents**\n   :depth: 1\n\nAbout\n=====\n\nThe purpose of GooBook is to make it possible to use your Google Contacts from\nthe command-line and from MUAs such as Mutt.\nIt can be used from Mutt the same way as abook.\n\n.. NOTE:: GooBook is looking for a new maintainer see https://gitlab.com/goobook/goobook/-/issues/90\n\nInstallation Instructions\n=========================\n\nThere is a number of ways to install Python software.\n\n- Using pip\n- Using a source tarball\n- Using source directly from gitorius\n- From a distribution specific repository\n\nWhich version to use\n--------------------\n\nIf you only have Python 2.7 you need to use GooBook 1.x.\nIf you have Python 3.7+ you need to use GooBook 3.x.\n\nThere will be no further feature releases in the 1.x series.\n\npip\n---\n\nThis is the recommended way to install goobook for most users that\ndon\'t have it available in their distribution.\nWhen installing this way you will not need to download anything manually.\n\nInstall like this::\n\n    $ pip install --user goobook\n\nThis will install goobook as ~/.local/bin/goobook (In a UNIX environment).\n\n\nPoetry\n------\n\nThis is the recommended way if you want to run from a git checkout.\nInstall poetry if you don\'t have it, https://python-poetry.org.\n\nclone the git repos, cd into in, and run::\n\n    $ poetry install\n\nGoobook is now installed in a virtualenv created by poetry.\nYou can test goobook by running::\n\n    $ poetry run goobook\n\nTo locate the virtualenv where goobook is installed::\n\n    $ poetry env list --full-path\n\nSource installation from tarball\n--------------------------------\n\nDownload the source tarball, uncompress it, then run the install command::\n\n    $ tar -xzvf goobook-*.tar.gz\n    $ cd goobook-*\n    $ sudo python ./setup.py install\n\n\nConfiguration\n=============\n\nFirst you need to authenticate yourself:\n\n- Go to https://developers.google.com/people/quickstart/python\n- and click "Enable the People API"\n- select a name (ex. GooBook)\n- select desktop app and create\n- save the client_id and client_secret to be used below\n\nrun::\n\n    $ goobook authenticate -- CLIENT_ID CLIENT_SECRET\n\nand follow the instructions, this part is web based.\n\n\nIf the procedure above to get client_id and secret stops working this is an alternative way to do it:\n\n- Go to the Google developer console  https://console.developers.google.com/\n- Create a new project (drop down at the top of the screen) (you are free to use an existing one if you so prefer)\n- Select the newly created project\n- Go to OAuth consent screen from sidebar\n- Select the interal user type if you can but most will only be able to select external.\n- On next screen give it a name (ex. GooBook)\n- select Add scope, click manually paste and write "https://www.googleapis.com/auth/contacts" inte the lower text box.\n- and hit hit add and then save\n- Go to Credentials from sidebar\n- Click Create Credentials from top, then OAuth Client ID in the dropdown\n- Choose Desktop app, enter any name you want, and hit create\n- save the client_id and client_secret to be used with goobook authenticate\n\n\nTo get access too more settings you can create a configuration file::\n\n    goobook config-template > ~/.config/goobookrc\n\nIt will look like this::\n\n    # Use this template to create your ~/.goobookrc\n\n    # "#" or ";" at the start of a line makes it a comment.\n\n    [DEFAULT]\n    # The following are optional, defaults are shown when not other specified.\n\n    # This file is written by the oauth library, and should be kept secure,\n    # it\'s like a password to your google contacts.\n    # default is to place it in the XDG_DATA_HOME\n    ;oauth_db_filename: ~/.goobook_auth.json\n\n    ;cache_filename: ~/.goobook_cache   # default is in the XDG_CACHE_HOME\n    ;cache_expiry_hours: 24\n    ;filter_groupless_contacts: yes\n\n    # New contacts will be added to this group in addition to "My Contacts"\n    # Note that the group has to already exist on google or an error will occur.\n    # One use for this is to add new contacts to an "Unsorted" group, which can\n    # be sorted easier than all of "My Contacts".\n    ;default_group:\n\n\nFiles\n-----\n\nGooBook is using three files, the optional config file that can be placed in\nthe ``XDG_CONFIG_HOME`` (``~/.config/goobookrc``) or in the home directory\n(``~/.goobookrc``).\n\nThe authentication file that is created by running goobook authenticate in\n``XDG_DATA_HOME`` (``~/.local/share/goobook_auth.json``) but can also be placed\nin the home directory (``~/.goobook_auth.json``).\n\nThe contacts cache file that is created in ``XDG_CACHE_HOME``\n(``~/.cache/goobook_cache``) but can also be placed in the home directory\n(``~/.goobook_cache``).\n\nProxy settings\n--------------\n\nIf you use a proxy you need to set the ``https_proxy`` environment variable.\n\nMutt\n----\n\nIf you want to use goobook from mutt.\n\nSet in your .muttrc file::\n\n    set query_command="goobook query %s"\n\nto query address book. (Normally bound to "Q" key.)\n\nIf you want to be able to use <tab> to complete email addresses instead of Ctrl-t add this::\n\n    bind editor <Tab> complete-query\n\nTo add email addresses (with "a" key normally bound to create-alias command)::\n\n    macro index,pager a "<pipe-message>goobook add<return>" "add the sender address to Google contacts"\n\nIf you want to add an email\'s sender to Contacts, press a while it\'s selected in the index or pager.\n\nUsage\n=====\n\nTo query your contacts::\n\n    $ goobook query QUERY\n\nThe add command reads a email from STDIN and adds the From address to your Google contacts::\n\n    $ goobook add\n\nThe cache is updated automatically according to the configuration but you can also force an update::\n\n    $ goobook reload\n\nFor more commands see::\n\n    $ goobook -h\n\nand::\n\n    $ goobook COMMAND -h\n\nLinks, Feedback and getting involved\n====================================\n\n- PyPI home: https://pypi.org/project/goobook/\n- Code Repository: http://gitlab.com/goobook/goobook\n- Issue tracker: https://gitlab.com/goobook/goobook/issues\n- Mailing list: http://groups.google.com/group/goobook\n',
    'author': 'Christer Sjöholm',
    'author_email': 'goobook@furuvik.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'http://gitlab.com/goobook/goobook',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
