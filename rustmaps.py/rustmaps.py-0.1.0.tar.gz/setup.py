# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['rustmaps']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'rustmaps.py',
    'version': '0.1.0',
    'description': 'Wrapper for the rustmaps.com REST API',
    'long_description': "# rustmaps.py\n\nThis package provides a Python interface for [rustmaps.com's HTTP REST API][1].\n\n**NB:** This is my first API wrapper package so it may have some issues. If you\nfind any I would greatly appreciate it if you opened an issue or pull request!\n\n\n## Roadmap to 1.0.0\n\nThe current features are not implemented:\n\n- [ ] `maps/filter/{filterId}` endpoint (paginated map searching)\n- [ ] v2Beta endpoints (`beta/outposts` and `beta/map/custom`)\n\n\n## Contributing\n\nThis project uses flake8 with default settings. Please make sure your code\npasses `poetry run flake8` and `poetry run pytest` before opening a pull\nrequest.\n\nThis project is designed to work with Python 3.8.0+. Please do not open pull\nrequests with features that break this compatibility.\n\n\n[1]: https://rustmaps.com/docs/index.html\n",
    'author': 'Ralph Drake',
    'author_email': 'pypi@ralphdrake.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/RalphORama/rustmaps.py/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
