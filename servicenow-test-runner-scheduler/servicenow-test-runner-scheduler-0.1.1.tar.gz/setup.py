# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['servicenow_test_runner_scheduler']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.9.1,<2.0.0',
 'python-dotenv>=0.20.0,<0.21.0',
 'selenium>=4.3.0,<5.0.0']

entry_points = \
{'console_scripts': ['servicenow-test-runner-scheduler = '
                     'servicenow_test_runner_scheduler.cli:main',
                     'snowtrs = servicenow_test_runner_scheduler.cli:main']}

setup_kwargs = {
    'name': 'servicenow-test-runner-scheduler',
    'version': '0.1.1',
    'description': '',
    'long_description': "# Trigger ATF Test / Suite from another instance\n\n- [Trigger ATF Test / Suite from another instance](#trigger-atf-test--suite-from-another-instance)\n  - [What does `servicenow-test-runner-scheduler` do?](#what-does-servicenow-test-runner-scheduler-do)\n  - [Installation](#installation)\n    - [pipx](#pipx)\n    - [pip](#pip)\n  - [Configure](#configure)\n  - [Usage](#usage)\n  - [Demo](#demo)\n\n\n## What does `servicenow-test-runner-scheduler` do?\n- Start `NUM_INSTANCE` (default: 6) instances of the client test runner concurrently\n- After `RESTART_INTERVAL // NUM_INSTANCE` (default: `7200 // 6 = 1200`) seconds, the first runner will be restarted, and after another 1200 seconds, the seconds runner will be restarted, and so on.\n- After all the runner have been restarted once, all the 6 runners will be scheduled to restarted every `RESTART_INTERVAL` (default: `7200`) seconds.\n\n\n## Installation\n\nInstall `python3` and [`chromedriver`](https://sites.google.com/chromium.org/driver/) first.  \n\n### pipx\n\nThis is the recommended installation method.\n\n```\n$ pipx install servicenow-test-runner-scheduler\n```\n\n### [pip](https://pypi.org/project/servicenow-test-runner-scheduler/)\n\n```\n$ pip install servicenow-test-runner-scheduler\n```\n\n\n## Configure\n\n- Create a `.env` file and put it in the same directory as the `trigger_test_zipapp.pyz` file.\n- Edit the `.env` files, so it looks like this:\n\n    ```ini\n    # required fields\n    instance=https://dev105825.service-now.com\n    userid=admin\n    password=admin_pw\n\n    # optional fields, the value shown here are the default values\n    RESTART_INTERVAL=7200\n    TOLERANCE=300\n    NUM_INSTANCE=6\n    CHECKING_INTERVAL=300\n    ```\n\n## Usage\n\n```\n$ snowtrs --help # or servicenow-test-runner-scheduler --help\n\nLoading settings for: \nusage: servicenow-test-runner-scheduler [-h] [-V] [-n] [-s]\n\nServiceNow - Start ATF test runner in browser\n\noptions:\n  -h, --help            show this help message and exit\n  -V, --version         show program's version number and exit\n  -n, --dry-run         Dry run (default: False)\n  -s, --scheduled-runner\n                        Start a scheduled runner (default: Client test runner) (default: False)\n```\n\n\n## Demo\n\n\nConfiguration of this demo:\n\n```ini\n# .env\nRESTART_INTERVAL=6\nTOLERANCE=1\nNUM_INSTANCE=6\nCHECKING_INTERVAL=1\n```\n\nRun `servicenow-test-runner-scheduler --dryrun`.\n\n![](images/demo.png)\n",
    'author': 'Teddy Xinyuan Chen',
    'author_email': '45612704+tddschn@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/tddschn/servicenow-test-runner-scheduler',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
