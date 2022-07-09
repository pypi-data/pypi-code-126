# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cvrplib']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.15,<2.0', 'requests>=2.27.1,<3.0.0']

setup_kwargs = {
    'name': 'cvrplib',
    'version': '0.1.0',
    'description': 'Python library for reading and downloading CVRPLIB instances.',
    'long_description': "# CVRPLIB\n[![PyPI version](https://badge.fury.io/py/cvrplib.svg)](https://badge.fury.io/py/cvrplib)\n[![cvrplib](https://github.com/leonlan/cvrplib/actions/workflows/cvrplib.yml/badge.svg)](https://github.com/leonlan/cvrplib/actions/workflows/cvrplib.yml)\n\nThis Python package provides functions to read and download instances from the Capacitated Vehicle Routing Problem Library ([CVRPLIB](http://vrp.atd-lab.inf.puc-rio.br/index.php/en/)). CVRPLIB contains a large collection of CVRP and VRPTW benchmark instances and also keeps track of the currently best known solutions.\n\n\n# Installation\nThis library works with Python 3.7+.\n\n```shell\npip install cvrplib\n```\n\n\n# Usage\nUsing this package is simple. We expose three functions:\n\n-   `read`: Read an instance (and optionally solution) from a local file.\n-   `download`: Download an instance (and optionally solution) directly from the CVRPLIB website.\n-   `list_names`: List all instance names that can be passed to `download`.\n\n\n## Example\n```python\nimport cvrplib\n\n# Read instances\ninstance = cvrplib.read('/path/to/A-n32-k5.vrp')\ninstance, solution = cvrplib.read(instance_path='/path/to/A-n32-k5.vrp',\n                                  solution_path='/path/to/A-n32-k5.sol')\n\n# Download instances\ninstance = cvrplib.download('A-n32-k5')\ninstance, solution = cvrplib.download('A-n32-k5', solution=True)\n\n# List instance names \ncvrplib.list_names()                      # All instance names\ncvrplib.list_names(low=100, high=200)     # Instances with between [100, 200] customers\ncvrplib.list_names(vrp_type='vrptw')      # Only VRPTW instances\n```\n## Dataclasses\nInstance fields depend on the VRP type of the instance. `Instance` defines the base instance, which is extended by the `CVRP` and `VRPTW` classes. `Solution` defines the solution and is the same for CVRP and VRPTW. \n```python\nclass Instance:\n    name: str\n    dimension: int\n    n_customers: int\n    depot: int\n    customers: List[int]\n    capacity: int\n    distances: List[List[float]]\n    demands: List[int]\n    service_times: List[float]\n    coordinates: Optional[List[List[float]]]\n\nclass CVRP(Instance):\n    distance_limit: float\n\nclass VRPTW(Instance):\n    n_vehicles: int\n    earliest: List[int]\n    latest: List[int]\n\nclass Solution:\n    routes: List[int]\n    cost: float\n```\n\n     \n# Conventions\nAll instances are parsed according to the CVRPLIB convention. See Section 3.3 in [Uchoa et al. (2014)](http://www.optimization-online.org/DB_FILE/2014/10/4597.pdf) for more details. In short:\n- The depot has index `0`. Customers are indexed from `1` to `n`.\n- The distances are rounded to the nearest integer. \n    - Note that some benchmark sets were originally proposed without integer rounding. This is the case for the following sets: `CMT`, `Rochat and Taillard (tai)`, `Golden`, `Li`, `Solomon`, `Homberger and Gehring`.\n    \n# Remarks\n- Downloading instances may take a few seconds. \n- The `XML100` benchmark set is not listed in `list_names` and cannot be downloaded using `download`. Please download these instances directly from [CVRPLIB](http://vrp.atd-lab.inf.puc-rio.br/index.php/en/) and use the `read` function instead.\n\n    \n",
    'author': 'Leon Lan',
    'author_email': 'leon.lanyidong@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/leonlan/CVRPLIB',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
