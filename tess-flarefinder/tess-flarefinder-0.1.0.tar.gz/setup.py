# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['tess_flarefinder']

package_data = \
{'': ['*'], 'tess_flarefinder': ['data/model.dat']}

install_requires = \
['lightkurve>=2.3,<3.0',
 'numba>=0.55.2,<0.56.0',
 'retrying>=1.3,<2.0',
 'tsfresh>=0.19,<0.20',
 'wotan>=1.10,<2.0']

setup_kwargs = {
    'name': 'tess-flarefinder',
    'version': '0.1.0',
    'description': 'Find flares in TESS',
    'long_description': None,
    'author': 'Keyu Xing',
    'author_email': 'kyxing@mail.bnu.edu.cn',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/keyuxing/tess_flarefinder',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
