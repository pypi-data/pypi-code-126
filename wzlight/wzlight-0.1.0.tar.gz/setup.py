# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wzlight']

package_data = \
{'': ['*']}

install_requires = \
['async-lru>=1.0.3,<2.0.0',
 'backoff>=2.1.2,<3.0.0',
 'httpx>=0.23.0,<0.24.0',
 'jupyterlab>=3.4.3,<4.0.0',
 'python-dotenv>=0.20.0,<0.21.0']

setup_kwargs = {
    'name': 'wzlight',
    'version': '0.1.0',
    'description': 'Light asynchronous wrapper for COD Warzone API',
    'long_description': '\n# wzlight\n\n[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)\n[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)\n\n\n`wzlight` is an asynchronous Python wrapper for the Call of Duty API\nthat focuses on Warzone endpoints.\n\n## Features\n\n- Asynchronous with help of HTTPX, the HTTP client library\n- Light : only centered around the few GET methods to collect Warzone stats\n- Handle SSO auth. the (now) only available way to connect to the API\n\n## Installation\n\n```bash\n  # with pip\n  pip install wzlight\n```\n```bash\n  # with Poetry\n  poetry add wzlight\n```\n\n    \n## Client usage\n<img src="https://github.com/matthieuvion/wzlight/blob/main/demo.svg">\n\n## Acknowledgements\n![Love](https://img.shields.io/badge/Love-pink?style=flat-square&logo=data:image/svg%2bxml;base64,PHN2ZyByb2xlPSJpbWciIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48dGl0bGU+R2l0SHViIFNwb25zb3JzIGljb248L3RpdGxlPjxwYXRoIGQ9Ik0xNy42MjUgMS40OTljLTIuMzIgMC00LjM1NCAxLjIwMy01LjYyNSAzLjAzLTEuMjcxLTEuODI3LTMuMzA1LTMuMDMtNS42MjUtMy4wM0MzLjEyOSAxLjQ5OSAwIDQuMjUzIDAgOC4yNDljMCA0LjI3NSAzLjA2OCA3Ljg0NyA1LjgyOCAxMC4yMjdhMzMuMTQgMzMuMTQgMCAwIDAgNS42MTYgMy44NzZsLjAyOC4wMTcuMDA4LjAwMy0uMDAxLjAwM2MuMTYzLjA4NS4zNDIuMTI2LjUyMS4xMjUuMTc5LjAwMS4zNTgtLjA0MS41MjEtLjEyNWwtLjAwMS0uMDAzLjAwOC0uMDAzLjAyOC0uMDE3YTMzLjE0IDMzLjE0IDAgMCAwIDUuNjE2LTMuODc2QzIwLjkzMiAxNi4wOTYgMjQgMTIuNTI0IDI0IDguMjQ5YzAtMy45OTYtMy4xMjktNi43NS02LjM3NS02Ljc1em0tLjkxOSAxNS4yNzVhMzAuNzY2IDMwLjc2NiAwIDAgMS00LjcwMyAzLjMxNmwtLjAwNC0uMDAyLS4wMDQuMDAyYTMwLjk1NSAzMC45NTUgMCAwIDEtNC43MDMtMy4zMTZjLTIuNjc3LTIuMzA3LTUuMDQ3LTUuMjk4LTUuMDQ3LTguNTIzIDAtMi43NTQgMi4xMjEtNC41IDQuMTI1LTQuNSAyLjA2IDAgMy45MTQgMS40NzkgNC41NDQgMy42ODQuMTQzLjQ5NS41OTYuNzk3IDEuMDg2Ljc5Ni40OS4wMDEuOTQzLS4zMDIgMS4wODUtLjc5Ni42My0yLjIwNSAyLjQ4NC0zLjY4NCA0LjU0NC0zLjY4NCAyLjAwNCAwIDQuMTI1IDEuNzQ2IDQuMTI1IDQuNSAwIDMuMjI1LTIuMzcgNi4yMTYtNS4wNDggOC41MjN6Ii8+PC9zdmc+)  \nInspiration (heavily) came from :  \nAlso check those links if your need documentation on how the API works\n - [EthanC/CallofDuty.py](https://github.com/EthanC/CallofDuty.py) : the most complete but now slightly deprecated (mainly the Auth.), async COD client (lot of exploited endpoints and methods + more than WZ) \n - [Lierrmm/Node-CallOfDuty](https://github.com/Lierrmm/Node-CallOfDuty) : very clean async. wrapper written in NodeJS. Also check their Discord to get a grip on API subtleties and unofficial changes (privacy changes, rate limits etc)\n - [valtov/WarzoneStats](https://github.com/valtov/WarzoneStats) : very clean synch. Python wrapper by the creator of wzstats.gg\n\n## License\n\n[MIT](https://choosealicense.com/licenses/mit/)\n',
    'author': 'Matthieu Vion',
    'author_email': 'viomatthieu@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/matthieuvion/wzlight',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
