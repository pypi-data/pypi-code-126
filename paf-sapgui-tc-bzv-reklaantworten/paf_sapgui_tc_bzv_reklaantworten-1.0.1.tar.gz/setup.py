# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['paf_sapgui_tc_bzv_reklaantworten',
 'paf_sapgui_tc_bzv_reklaantworten.elements']

package_data = \
{'': ['*']}

install_requires = \
['paf_sapgui>=1.0.51,<2.0.0',
 'paf_sapgui_cic>=1.0.16,<2.0.0',
 'paf_tools>=1.0.0,<2.0.0',
 'pendulum>=2.1,<3.0']

setup_kwargs = {
    'name': 'paf-sapgui-tc-bzv-reklaantworten',
    'version': '1.0.1',
    'description': '',
    'long_description': None,
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
