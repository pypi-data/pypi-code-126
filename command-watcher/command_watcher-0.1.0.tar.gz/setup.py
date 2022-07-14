# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['command_watcher']

package_data = \
{'': ['*']}

install_requires = \
['conf2levels>=0.4.0,<0.5.0',
 'jflib>=1.0.0,<2.0.0',
 'requests>=2.28.1,<3.0.0',
 'termcolor>=1.1.0,<2.0.0',
 'types-requests>=2.28.1,<3.0.0',
 'types-termcolor>=1.1.5,<2.0.0']

setup_kwargs = {
    'name': 'command-watcher',
    'version': '0.1.0',
    'description': 'Module to watch the execution of shell scripts. Both streams (`stdout` and `stderr`) are captured.',
    'long_description': "command_watcher\n===============\n\nModule to watch the execution of shell scripts. Both streams (`stdout`\nand `stderr`) are captured.\n\n.. code:: python\n\n    watch = Watch()\n    watch.log.critical('msg')\n    watch.log.error('msg')\n    watch.log.warning('msg')\n    watch.log.info('msg')\n    watch.log.debug('msg')\n    watch.run(['rsync', '-av', '/home', '/backup'])\n\n.. code-block:: python\n\n    from command_watcher import Watch\n    watch = Watch(\n        config_file='/etc/command-watcher.ini',\n        service_name='texlive_update'\n    )\n\n    tlmgr = '/usr/local/texlive/bin/x86_64-linux/tlmgr'\n\n    watch.run('{} update --self'.format(tlmgr))\n    watch.run('{} update --all'.format(tlmgr))\n    installed_packages = watch.run(\n        '{} info --only-installed'.format(tlmgr), log=False\n    )\n    all_packages = watch.run('{} info'.format(tlmgr), log=False)\n\n    watch.final_report(\n        status=0,\n        performance_data={\n            'installed_packages': installed_packages.line_count_stdout,\n            'all_packages': all_packages.line_count_stdout,\n        },\n    )\n\n.. code-block:: ini\n\n    [email]\n    subject_prefix = [cwatcher]\n    from_addr =\n    to_addr = logs@example.com\n    to_addr_critical = critical@example.com\n    smtp_login = mailer\n    smtp_password = 1234\n    smtp_server = mail.example.com:587\n\n    [nsca]\n    remote_host = 1.2.3.4\n    password = asdf1234\n    encryption_method = 8\n    ; port = 5667\n\n    [icinga]\n    url = https://icinga.example.com:5665\n    user = user\n    password = 1234\n\n    [beep]\n    activated = True\n",
    'author': 'Josef Friedrich',
    'author_email': 'josef@friedrich.rocks',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Josef-Friedrich/command-watcher',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
