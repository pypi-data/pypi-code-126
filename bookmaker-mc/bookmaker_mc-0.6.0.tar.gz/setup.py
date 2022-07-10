# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['bookmaker', 'bookmaker.css_resources']

package_data = \
{'': ['*'], 'bookmaker': ['book_resources/*']}

install_requires = \
['PyGObject>=3.40,<4.0',
 'Pygments>=2.9,<3.0',
 'mistune>=2.0.0rc1,<3.0.0',
 'tomli>=2.0.1,<3.0.0']

entry_points = \
{'console_scripts': ['bm = bookmaker:main']}

setup_kwargs = {
    'name': 'bookmaker-mc',
    'version': '0.6.0',
    'description': 'A Book Authoring Application in Python',
    'long_description': "# BookMaker\nA Book Authoring Application in Python - inspired by Gitbook-Legacy\n\nBookMaker is a book authoring application in Python.\n\nIntroduction\n------------\n* BookMaker facilitates authoring using MarkDown, with a live preview.\n* Handles a complete book with a live tree display of chapters, sections and subsections.\n* Exporting to EPUB\n* Exporting to PDF (generating suitable HTML and CSS for Prince)\n\nHow to install it?\n------------\nUsing poetry (https://python-poetry.org/)\n```txt\ngit clone https://github.com/marcris/bookmaker_mc.git\ncd bookmaker_mc\npoetry build\npip3 install dist/*.whl\n```\nRun using the command 'bm'.\n\nLinks\n------------\n* BookMaker GitHub repository including documentation (in preparation) <https://github.com/marcris/BookMaker_mc>\n",
    'author': 'Chris Brown',
    'author_email': 'chris@marcrisoft.co.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/marcris/bookmaker-mc',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
