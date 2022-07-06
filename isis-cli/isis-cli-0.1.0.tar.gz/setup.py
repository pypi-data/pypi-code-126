# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['isi-cli']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0']

setup_kwargs = {
    'name': 'isis-cli',
    'version': '0.1.0',
    'description': 'General purpose CLI',
    'long_description': '# icli\n\n## Development set up\n### Without Docker\n- You need to install [poetry](https://python-poetry.org/docs/#installation)\n- Run `poetry install`\n- Run `poetry run python src/main.py`\n- Run `poetry run python src/main.py --name=Batman --count=2`\n- Run `poetry run python src/main.py --help`\n\n## With Docker\n- Prerequisite: being able to run `make`\n- Running `make` will show you all the possible actions\n\n## Decisions taken and personal notes\n- Origin of the name: \n    - i(si) + cli\n    - or the typical iAnything :-)\n- Library used: **Click**\n    - The examples of code seen look simpler\n    - Good opinions in several posts with comparisons with Docopts or Argparse\n    - Looks like a "modern" way of creating a CLI in 2022\n    - Used by AWS\n- Dependencies with [**poetry**](https://python-poetry.org/)\n    - `poetry show -v`\n    - `poetry env list`\n- The [ENTRYPOINT](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#entrypoint) is the execution of the main file.\n\n## Resources\n- [Video tutorial: Building Command Line Applications with Click](https://www.youtube.com/watch?v=kNke39OZ2k0) - 18 minutes\n- [Click examples](https://click.palletsprojects.com/en/7.x/quickstart/#screencast-and-examples)\n- https://github.com/CodiumTeam/docker-training\n- https://jackmckew.dev/packaging-python-packages-with-poetry.html\n    - https://github.com/JackMcKew/wordsum\n\n## TO DO\n- Publish it to PyPI\n- Package it to be installed from PyPI, e.g. `pip install icli`\n- Make possible to run it \n- Version it\n- Use mypy\n- Use black formatter\n',
    'author': 'Isidro Lopez',
    'author_email': 'islomar@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
