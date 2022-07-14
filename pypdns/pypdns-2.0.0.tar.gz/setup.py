# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pypdns']

package_data = \
{'': ['*']}

install_requires = \
['dnspython>=2.2.1,<3.0.0', 'requests-cache>=0.9.5,<0.10.0']

setup_kwargs = {
    'name': 'pypdns',
    'version': '2.0.0',
    'description': 'Python API for PDNS.',
    'long_description': "Client API for PDNS\n===================\n\nClient API to query any Passive DNS implementation following the Passive DNS - Common Output Format.\n\n* https://datatracker.ietf.org/doc/draft-dulaunoy-dnsop-passive-dns-cof/\n\nExample\n=======\n\n~~~~\nimport pypdns\nx = pypdns.PyPDNS(basic_auth=('username','yourpassword'))\nprint (x.query('www.microsoft.com')[0]['rdata'])\n~~~~\n\nPassive DNS Services\n====================\n\n* (default) [CIRCL Passive DNS](http://www.circl.lu/services/passive-dns/)\n\n\n",
    'author': 'Raphaël Vinot',
    'author_email': 'raphael.vinot@circl.lu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/CIRCL/PyPDNS',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
