# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cybernetickit', 'cybernetickit.experimental']

package_data = \
{'': ['*']}

install_requires = \
['elasticsearch-dsl>=7.0.0,<8.0.0']

extras_require = \
{':python_version >= "3.7" and python_version < "3.8"': ['typing-inspect>=0.7.1,<0.8.0']}

setup_kwargs = {
    'name': 'cybernetickit',
    'version': '0.2.0a4',
    'description': 'The Cybernetic Kit is a set of conventions and techniques useful for making software-driven social impact.',
    'long_description': "# Cybernetic Kit\n\nThe Cybernetic Kit is a set of conventions and techniques useful for making software-driven social impact. This repository holds a collection of software components for multiple fields of study, such as:\n\n- Open Data & Civic Engagement\n- Environmental Science\n- Library Science\n- Software Development\n- Sociology\n- Neuroscience\n\n\n## Meet the Cast\n\n### Data Objects\n\nData Objects are Python classes designed to make it easier to interact with data. Using Data Objects to describe something of interest tells computers how to manipulate, archive, inspect, and exchange data.\n\n#### Built-In Data Objects\n\n- civic data\n- research preprints and archives\n- air quality sensor readings\n- geopolitical shapes (e.g., county, state)\n\n\n**How to use built-in Data Objects**\n\nHere's an example of how you'd go about storing air quality sensor readings in Elasticsearch.\n\n```python\nfrom datetime import datetime\n\nfrom elasticsearch_dsl import connections\nfrom cybernetickit.sensor import AirQuality\nfrom cybernetickit import constants\n\nconnections.create_connection(hosts=['localhost'], timeout=20)\n\nobservation = AirQuality(date=datetime.now(),\n                         state='ga',\n                         pollutant=constants.OZONE._asdict(),\n                         units=constants.OZONE.units,\n                         concentration=2.3)\n\nobservation.save()\n```\n\nYou can use the Elasticsearch DSL to search and aggregations against an existing Elasticsearch index:\n\n```python\nfrom elasticsearch_dsl import Q\ns = AirQuality.search(Q('match', state='ny') & Q('match', **{'pollutant.parameter': 'OZONE'}))\nresponse = s.execute()\n\nfor obs in response:\n    ...\n```\n\n#### Custom Data Objects\n\nSimply subclass the `CoreModel` and describe something of interest. Use annotations for runtime validation:\n\n```python\nfrom typing from List, Optional\nfrom cybernetickit from CoreModel, Keyword\n\n\nclass UseOfForce(CoreModel):\n    force_applied: str = Keyword()\n    deadly_force: Optional[str] = Keyword()\n    source_ref: str = Keyword()\n    target_ref: str = Keyword()\n\n```\n\n\n\n## Getting Started\n\n```sh\npip install cybernetickit\n```\n\n```python\nfrom cybernetickit import CoreModel\n```\n\n\n## Licensing\n\n    Cybernetic Kit\n    Copyright (C) 2021  Civic Hacker, LLC\n\n    This program is free software: you can redistribute it and/or modify\n    it under the terms of the Lesser GNU General Public License as published by\n    the Free Software Foundation, either version 3 of the License, or\n    (at your option) any later version.\n\n    This program is distributed in the hope that it will be useful,\n    but WITHOUT ANY WARRANTY; without even the implied warranty of\n    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n    Lesser GNU General Public License for more details.\n\n    You should have received a copy of the Lesser GNU General Public License\n    along with this program.  If not, see <https://www.gnu.org/licenses/>.\n",
    'author': 'Jurnell Cockhren',
    'author_email': 'jurnell@civichacker.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
