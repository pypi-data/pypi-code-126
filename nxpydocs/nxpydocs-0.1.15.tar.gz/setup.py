# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['nxpydocs']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2==2.11.3', 'PyYAML>=5.4,<6.0', 'click==7.1.2', 'gTTS>=2.2.3,<3.0.0']

entry_points = \
{'console_scripts': ['nxpydocs = nxpydocs.script:run']}

setup_kwargs = {
    'name': 'nxpydocs',
    'version': '0.1.15',
    'description': 'Automated Business Ready Documents from the NX-OS Guestshell',
    'long_description': '# nxpydocs\nAutomated NXOS Business Ready Documents from th guestshell Python\n\n## Setting up guestshell and Python3.8\n### Enable guestshell\n```console\nswitch# guestshell enable\n```\nWait until the guestshell becomes active\n\n### Resize guestshell diskspace\n```console\nguestshell resize rootfs 2000\nguestshell resize memory 2688\nguesthshell reboot\n```\n\n### Update DNS\n```console\n[cisco@guestshell ~]sudo vi /etc/resolv.conf\nnameserver <dns server IP address>\ndomain <domain that matches NX-OS configured domain>\n```',
    'author': 'John Capobianco',
    'author_email': 'ptcapo@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=2.7,<3.0',
}


setup(**setup_kwargs)
