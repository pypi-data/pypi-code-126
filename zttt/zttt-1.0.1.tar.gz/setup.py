# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zttt', 'zttt._zt_core']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'zttt',
    'version': '1.0.1',
    'description': 'Simple, Standalone Tic Tac Toe Library',
    'long_description': "\n.. _zttt_main:\n\nZTicTacToe\n============\n\nTic Tac Toe is a famous game in which two players take turns placing\na mark on a 3x3 grid. The first player to get three in a row wins.\n\nThe module is a standalone implementation of the game TicTacToe\nproviding functionality to keep track of the game's state and to\nmake moves.\n\n\n.. _zttt_features:\n\nFeatures\n---------\n- Standalone implementation of the game Tic Tac Toe.\n- Provides a way to customise **move triggers** and access state variables.\n- Comes with an engine with near perfect moves.\n- Written in Python from scratch and does not require any external libraries.\n- Can be integrated into a larger project, with very little effort.\n- Throws custom-built errors making it easy to debug and handle errors.\n\n\n\n.. _zttt_links:\n\nLinks\n------\n- `PyPI <https://pypi.python.org/pypi/zttt>`_\n- `GitHub <https://github.com/Sigma1084/ZTicTacToe/tree/v1>`_\n- `Documentation <https://ztictactoe.readthedocs.io/en/v1/>`_\n- `Examples <https://github.com/Sigma1084/ZTicTacToe/tree/v1/examples>`_\n\n.. _zttt_install:\n\nInstallation\n-------------\n.. code-block:: bash\n\n    pip install zttt\n",
    'author': 'Sumanth NR',
    'author_email': 'sumanthnr62@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://ztictactoe.readthedocs.io/en/latest/',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
