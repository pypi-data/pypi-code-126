# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pypkg_winstonyym', 'pypkg_winstonyym.data']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.5.2']

setup_kwargs = {
    'name': 'pypkg-winstonyym',
    'version': '0.4.0',
    'description': 'testing package build',
    'long_description': '# pypkg_winstonyym\n\ntesting package build\n\n## Installation\n\n```bash\n$ pip install pypkg_winstonyym\n```\n\n## Usage\n\n- TODO\n\n## Contributing\n\nInterested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.\n\n## License\n\n`pypkg_winstonyym` was created by winstonyym. It is licensed under the terms of the MIT license.\n\n## Credits\n\n`pypkg_winstonyym` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).\n',
    'author': 'winstonyym',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
