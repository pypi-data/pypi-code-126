# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['word_text_counter']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'word-text-counter',
    'version': '0.1.0',
    'description': 'Calculate word counts in a text file!',
    'long_description': '# word_text_counter\n\nCalculate word counts in a text file!\n\n## Installation\n\n```bash\n$ pip install word_text_counter\n```\n\n## Usage\n\n```python\nfrom word_text_counter import count_words\n\nfile_path = "data/test.txt" #a path to your text file\ncounts = count_words(file_path)\n```\n\n## Contributing\n\nInterested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.\n\n## License\n\n`word_text_counter` was created by Sumbono. It is licensed under the terms of the MIT license.\n\n## Credits\n\n`word_text_counter` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).\n',
    'author': 'Sumbono',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
