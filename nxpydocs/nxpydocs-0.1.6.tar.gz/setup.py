# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['nxpydocs']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0',
 'PyYAML>=6.0,<7.0',
 'gTTS>=2.2.4,<3.0.0',
 'rich-click>=1.5.1,<2.0.0',
 'rich>=12.4.4,<13.0.0']

entry_points = \
{'console_scripts': ['nxpydocs = nxpydocs.script:run']}

setup_kwargs = {
    'name': 'nxpydocs',
    'version': '0.1.6',
    'description': 'Automated Business Ready Documents from the NX-OS Guestshell',
    'long_description': "# nxpydocs\nAutomated NXOS Business Ready Documents from th guestshell Python\n\n## Setting up guestshell and Python3.8\n### Enable guestshell\n```console\nswitch# guestshell enable\n```\nWait until the guestshell becomes active\n\n### Resize guestshell diskspace\n```console\nguestshell resize rootfs 2000\nguestshell resize memory 2688\nguesthshell reboot\n```\n\n### Update DNS\n```console\n[cisco@guestshell ~]sudo vi /etc/resolv.conf\nnameserver <dns server IP address>\ndomain <domain that matches NX-OS configured domain>\n```\n\n### Update yum\n```console\n[cisco@guestshell ~]sudo yum -y install epel-release\n[cisco@guestshell ~]yum update -y\n[cisco@guestshell ~]sudo reboot\n```\n### Install Python3.8\n```console\n[cisco@guestshell ~]sudo yum -y install openssl-devel bzip2-devel libffi-devel xz-devel\n```\n\nConfirm gcc is installed\n\n```console\n[cisco@guestshell ~]gcc --version\ngcc (GCC) 4.8.5 20150623 (Red Hat 4.8.5-44)\nCopyright (C) 2015 Free Software Foundation, Inc.\nThis is free software; see the source for copying conditions.  There is NO\nwarranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.\n```\n\nDownload Python 3.8\n```console\n[cisco@guestshell ~]sudo yum -y install wget\n[cisco@guestshell ~]wget https://www.python.org/ftp/python/3.8.12/Python-3.8.12.tgz\n```\n\nExtract and compile\n```console\n[cisco@guestshell ~]sudo tar xvf Python-3.8.12.tgz\n[cisco@guestshell ~]cd Python-3.8.12\n[cisco@guestshell ~]sudo ./configure --enable-optimizations\n[cisco@guestshell ~]sudo make altinstall\n```\n\nVerify Python3.8 is installed\n```console\n[cisco@guestshell ~]python3.8 -V\nPython 3.8.12\n```\n\nCleanup\n```console\n[cisco@guestshell ~]sudo rm -rf Python-3.8.12\n[cisco@guestshell ~]sudo rm Python-3.8.12.tgz\n```\n### Set Python3 as default Python version\n```\n[cisco@guestshell ~]sudo alternatives --install /usr/bin/python python /usr/local/bin/python3.8 60\n\n[cisco@guestshell ~]sudo alternatives --config python\n\nThere is 1 program that provides 'python'.\n\n  Selection    Command\n-----------------------------------------------\n*+ 1           /usr/local/bin/python3.8\n\nEnter to keep the current selection[+], or type selection number: 1\n```",
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
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
