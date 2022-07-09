# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['timezonefinder']

package_data = \
{'': ['*']}

install_requires = \
['h3>=3.7.3,<4.0.0', 'numpy>=1.22,<2.0']

extras_require = \
{'numba': ['numba>=0.55.2,<0.56.0']}

entry_points = \
{'console_scripts': ['timezonefinder = timezonefinder.command_line:main']}

setup_kwargs = {
    'name': 'timezonefinder',
    'version': '6.0.2',
    'description': 'fast python package for finding the timezone of any point on earth (coordinates) offline',
    'long_description': "==============\ntimezonefinder\n==============\n\n\n..\n    Note: can't include the badges file from the docs here, as it won't render on PyPI -> sync manually\n\n.. image:: https://github.com/jannikmi/timezonefinder/actions/workflows/build.yml/badge.svg?branch=master\n    :target: https://github.com/jannikmi/timezonefinder/actions?query=branch%3Amaster\n\n.. image:: https://readthedocs.org/projects/timezonefinder/badge/?version=latest\n    :alt: documentation status\n    :target: https://timezonefinder.readthedocs.io/en/latest/?badge=latest\n\n.. image:: https://img.shields.io/pypi/wheel/timezonefinder.svg\n    :target: https://pypi.python.org/pypi/timezonefinder\n\n.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white\n   :target: https://github.com/pre-commit/pre-commit\n   :alt: pre-commit\n\n.. image:: https://pepy.tech/badge/timezonefinder\n    :alt: total PyPI downloads\n    :target: https://pepy.tech/project/timezonefinder\n\n.. image:: https://img.shields.io/pypi/v/timezonefinder.svg\n    :alt: latest version on PyPI\n    :target: https://pypi.python.org/pypi/timezonefinder\n\n.. image:: https://img.shields.io/conda/vn/conda-forge/timezonefinder.svg\n   :target: https://anaconda.org/conda-forge/timezonefinder\n   :alt: latest version on conda-forge\n\n.. image:: https://img.shields.io/badge/code%20style-black-000000.svg\n    :target: https://github.com/psf/black\n\n\n\nThis is a fast and lightweight python package for looking up the corresponding\ntimezone for given coordinates on earth entirely offline.\n\n\nQuick Guide:\n\n::\n\n    pip install timezonefinder[numba] # also installs optional dependencies for increased performance\n\n\n.. code-block:: python\n\n    from timezonefinder import TimezoneFinder\n\n    tf = TimezoneFinder()\n    tz = tf.timezone_at(lng=13.358, lat=52.5061)  # 'Europe/Berlin'\n\n\nFor more refer to the `Documentation <https://timezonefinder.readthedocs.io/en/latest/>`__.\n\nAlso check:\n\n`PyPI <https://pypi.python.org/pypi/timezonefinder/>`__\n\n`online GUI and API <https://timezonefinder.michelfe.it>`__\n\n`conda-forge feedstock <https://github.com/conda-forge/timezonefinder-feedstock>`__\n\nruby port: `timezone_finder <https://github.com/gunyarakun/timezone_finder>`__\n\n`download stats <https://pepy.tech/project/timezonefinder>`__\n",
    'author': 'jannikmi',
    'author_email': 'github@michelfe.it',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://timezonefinder.michelfe.it/gui',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
