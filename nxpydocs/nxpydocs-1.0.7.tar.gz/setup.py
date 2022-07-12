# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['nxpydocs']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2==2.11.3',
 'PyYAML>=5.4,<6.0',
 'click==7.1.2',
 'furl>=2.1.3,<3.0.0',
 'pathlib>=1.0.1,<2.0.0']

entry_points = \
{'console_scripts': ['nxpydocs = nxpydocs.script:run']}

setup_kwargs = {
    'name': 'nxpydocs',
    'version': '1.0.7',
    'description': 'Automated Business Ready Documents from the NX-OS Guestshell',
    'long_description': '# nxpydocs\nAutomated NXOS Business Ready Documents from th guestshell Python\n\n## Setting up guestshell\n### Enable guestshell\n```console\nswitch# guestshell enable\n```\nWait until the guestshell becomes active\n\n### Resize guestshell diskspace\n```console\nguestshell resize rootfs 2000\nguestshell resize memory 2688\nguesthshell reboot\n```\n\n### Update DNS\n```console\n[cisco@guestshell ~]sudo vi /etc/resolv.conf\nnameserver <dns server IP address>\ndomain <domain that matches NX-OS configured domain>\n```\n\n### Install Git\n```console\n[cisco@guestshell ~]sudo yum install git\n```\n\n### Conigure Git\n```console\n[cisco@guestshell ~]git config --global user.name "Your Name Here"\n[cisco@guestshell ~]git config --global user.email johndoe@example.com\n[cisco@guestshell ~]git config --global push.default matching\n```\n\n## Install the application\n```console\n[cisco@guestshell ~]pip install nxpydocs\n```\n\n## Run nxpydocs\n### Get Help\nYou can add --help to see the help information\n```console\n[cisco@guestshell ~]nxpydocs --help\n\n```\n\n### Run nxpydocs interactively\nYou can simply run nxpydocs and it will prompt you for the required input values\n```console\n[cisco@guestshell ~]nxpydocs\n\n```',
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
