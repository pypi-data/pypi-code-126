# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['secimport']

package_data = \
{'': ['*'],
 'secimport': ['templates/*',
               'templates/actions/*',
               'templates/deprecated/*',
               'templates/filters/*']}

setup_kwargs = {
    'name': 'secimport',
    'version': '0.1.0',
    'description': 'A sandbox/supervisor for python modules.',
    'long_description': '# secimport\n<p align="center">\n <a href="https://github.com/avilum/secimport"><img src="https://user-images.githubusercontent.com/19243302/177835749-6aec7200-718e-431a-9ab5-c83c6f68565e.png" alt="secimport"></a>\n</p>\n\n<p align="center">\nA sandbox/supervisor for python modules.\n</p>\n\n`secimport` can be used to:\n- Confine/Restrict specific python modules inside your production environment.\n  - Open Source, 3rd party from unstrusted sources.\n- Audit the flow of your python application at user-space/os/kernel level.\n- Run an entire python application under unified configuration\n  - Like `seccomp` and `seccomp-bpf`, <b>without changing your code</b>\n  - Not limited to Linux kernels. Cross platform.\n\n### Requirements\n- A python interpreter that was built with `--with-dtrace`.\n  - See <a href="docs/INSTALL.md">INSTALL.md</a>.\n\n<br>\n\n# Quick Start\nFor the full list of examples, see <a href="docs/EXAMPLES.md">EXAMPLES.md</a>.\n\n### Shell blocking\n```python\n# example.py - Executes code upon import;\n  import os;\n\n  os.system(\'Hello World!\');\n```\n```python\n# production.py - Your production code\n  from secimport import secure_import \n\n  example = secure_import(\'example\', allow_shells=False)\n```\n```\n(root) sh-3.2#  export PYTHONPATH=$(pwd)/src:$(pwd)/examples:$(pwd):$PYTHONPATH\n(root) sh-3.2#  python examples/production.py \n  Successfully compiled dtrace profile:  /tmp/.secimport/sandbox_example.d\nKilled: 9\n```\n- We imported `example` with limited capabilities.\n- If a syscall like `spawn/exec/fork/forkexec` will be executed\n  - The process will be `kill`ed with `-9` signal.\n\n### Network blocking\n```\n>>> import requests\n>>> requests.get(\'https://google.com\')\n<Response [200]>\n  \n\n>>> from secimport import secure_import\n>>> requests = secure_import(\'requests\', allow_networking=False)\n\n# The next call should kill the process, since networking is not allowed\n>>> requests.get(\'https://google.com\')\n[1]    86664 killed\n```\n\n## Python Shell Interactive Example\n```python\nPython 3.10.0 (default, May  2 2022, 21:43:20) [Clang 13.0.0 (clang-1300.0.27.3)] on darwin\nType "help", "copyright", "credits" or "license" for more information.\n\n# Let\'s import subprocess module, limiting it\'s syscall access.\n>>> import secimport\n>>> subprocess = secimport.secure_import("subprocess")\n\n# Let\'s import os \n>>> import os\n>>> os.system("ps")\n  PID TTY           TIME CMD\n 2022 ttys000    0:00.61 /bin/zsh -l\n50092 ttys001    0:04.66 /bin/zsh -l\n75860 ttys001    0:00.13 python\n0\n# It worked as expected, returning exit code 0.\n\n\n# Now, let\'s try to invoke the same logic using a different module, "subprocess", that was imported using secure_import:\n>>> subprocess.check_call(\'ps\')\n[1]    75860 killed     python\n\n# Damn! That\'s cool.\n```\n\n- The dtrace profile for the module is saved under:\n  -  `/tmp/.secimport/sandbox_subprocess.d`:\n- The log file for this module is under\n  -  `/tmp/.secimport/sandbox_subprocess.log`:\n        ```shell\n        ...\n\n        (OPENING SHELL using posix_spawn): (pid 75860) (thread 344676) (user 501) (python module: <stdin>) (probe mod=, name=entry, prov=syscall func=posix_spawn) /bin/sh \n            #posix_spawn,\n\n        (TOUCHING FILESYSTEM): write(140339021606912) from thread 344676\n                    libsystem_kernel.dylib`__fork+0xb\n                    _posixsubprocess.cpython-310-darwin.so`do_fork_exec+0x29\n                    _posixsubprocess.cpython-310-darwin.so`subprocess_fork_exec+0x71f\n                    python.exe`cfunction_call+0x86\n        killing...\n        killed.\n        ```\n\n## Useful References\n- <a href="docs/EXAMPLES.md">Examples</a>\n- <a href="docs/FAQ.md">F.A.Q</a>\n- <a href="docs/INSTALL.md">Installation</a>\n- <a href="docs/MAC_OS_USERS.md">Mac OS Users</a> - Disabling SIP for dtrace\n- Tracing processes\n  - Using `dtrace`\n    - Tracing the syscalls of a process with pid `12345`\n      - `dtrace -n \'syscall::: /pid == ($1)/ {@[pid,execname,probefunc]=count()}\' 12345`\n    - Tracing the syscalls of a docker container with pid `12345`\n      - `dtrace -n \'syscall::: /progenyof($1)/ {@[pid,execname,probefunc]=count()}\' 12345`\n  - Using `strace`\n    -  A script to list all your application\'s syscalls using `strace`.<br> I contributed it to `firejail` a few years ago:\n      - https://github.com/netblue30/firejail/blob/master/contrib/syscalls.sh\n      - ```\n        wget "https://raw.githubusercontent.com/netblue30/firejail/c5d426b245b24d5bd432893f74baec04cb8b59ed/contrib/syscalls.sh" -O syscalls.sh\n\n        chmod +x syscalls.sh\n\n        ./syscalls.sh examples/http_request.py\n        ```\n- https://www.brendangregg.com/DTrace/DTrace-cheatsheet.pdf\n<br><br>\n\n## TODO:\n- Node support (dtrace hooks)\n- Go support (dtrace hooks)\n- Allow/Block list configuration\n- Create a .yaml configuration per module in the code\n  - Use secimport to compile that yml\n  - Create a single dcript policy\n  - Run an application with that policy using dtrace, without using `secure_import`\n',
    'author': 'Avi Lumelsky',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/avilum/secimport',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
