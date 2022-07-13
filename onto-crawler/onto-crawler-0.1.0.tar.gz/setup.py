# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['onto_crawler']

package_data = \
{'': ['*']}

install_requires = \
['PyGithub>=1.55,<2.0', 'oaklib>=0.1.31,<0.2.0']

entry_points = \
{'console_scripts': ['ocrawl = onto_crawler.cli:main']}

setup_kwargs = {
    'name': 'onto-crawler',
    'version': '0.1.0',
    'description': 'Crawl github for ontology related issues.',
    'long_description': None,
    'author': 'Harshad Hegde',
    'author_email': 'hhegde@lbl.gov',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
