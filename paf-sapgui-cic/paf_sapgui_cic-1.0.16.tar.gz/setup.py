# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['paf_sapgui_cic',
 'paf_sapgui_cic.elements',
 'paf_sapgui_cic.flows',
 'paf_sapgui_cic.flows.msd_orders',
 'paf_sapgui_cic.flows.position_details']

package_data = \
{'': ['*']}

install_requires = \
['paf_sapgui>=1.0.51,<2.0.0']

setup_kwargs = {
    'name': 'paf-sapgui-cic',
    'version': '1.0.16',
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
