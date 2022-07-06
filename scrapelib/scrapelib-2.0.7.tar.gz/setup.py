# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['scrapelib', 'scrapelib.tests']

package_data = \
{'': ['*']}

install_requires = \
['requests[security]>=2.28.1,<3.0.0']

entry_points = \
{'console_scripts': ['scrapeshell = scrapelib.__main__:scrapeshell']}

setup_kwargs = {
    'name': 'scrapelib',
    'version': '2.0.7',
    'description': '',
    'long_description': "**scrapelib** is a library for making requests to less-than-reliable websites.\n\nSource: [https://github.com/jamesturk/scrapelib](https://github.com/jamesturk/scrapelib)\n\nDocumentation: [https://jamesturk.github.io/scrapelib/](https://jamesturk.github.io/scrapelib/)\n\nIssues: [https://github.com/jamesturk/scrapelib/issues](https://github.com/jamesturk/scrapelib/issues)\n\n[![PyPI badge](https://badge.fury.io/py/scrapelib.svg)](https://badge.fury.io/py/scrapelib)\n[![Test badge](https://github.com/jamesturk/scrapelib/workflows/Test/badge.svg)](https://github.com/jamesturk/scrapelib/actions?query=workflow%3A%22Test)\n\n## Features\n\n**scrapelib** originated as part of the [Open States](http://openstates.org/)\nproject to scrape the websites of all 50 state legislatures and as a result\nwas therefore designed with features desirable when dealing with sites that\nhave intermittent errors or require rate-limiting.\n\nAdvantages of using scrapelib over using requests as-is:\n\n- HTTP(S) and FTP requests via an identical API\n- support for simple caching with pluggable cache backends\n- highly-configurable request throtting\n- configurable retries for non-permanent site failures\n- All of the power of the suberb [requests](http://python-requests.org) library.\n\n\n## Installation\n\n*scrapelib* is on [PyPI](https://pypi.org/project/scrapelib/), and can be installed via any standard package management tool:\n\n    poetry add scrapelib\n\nor:\n\n    pip install scrapelib\n\n\n## Example Usage\n\n``` python\n\n  import scrapelib\n  s = scrapelib.Scraper(requests_per_minute=10)\n\n  # Grab Google front page\n  s.get('http://google.com')\n\n  # Will be throttled to 10 HTTP requests per minute\n  while True:\n      s.get('http://example.com')\n```\n",
    'author': 'James Turk',
    'author_email': 'dev@jamesturk.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jamesturk/scrapelib',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
