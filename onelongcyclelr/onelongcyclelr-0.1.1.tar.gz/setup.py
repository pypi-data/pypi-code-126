# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['onelongcyclelr']

package_data = \
{'': ['*']}

install_requires = \
['torch>=1.0.0,<2.0.0']

setup_kwargs = {
    'name': 'onelongcyclelr',
    'version': '0.1.1',
    'description': "An adaptation of pytorch OneCycleLR that doesn't crash when max steps is reached",
    'long_description': '# OneLongCycleLR\n\nThis is a simple adaptation from the OneCycleLR of pytorch.optim package.\nThe default behaviour is to raise a ValueError when the maximum number of steps is reached. This one instead just keeps on returning the last value.\n\nTo install it, just use:\n\n    pip install onelongcyclelr\n\nAnd to use it you need to import it like\n\n    from onelongcyclelr import OneLongCycleLR\n\nThe arguments and keywords needed are exactly the same as the official implementation.',
    'author': 'Andrea Boscolo Camiletto',
    'author_email': 'abcamiletto@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/abcamiletto/onelongcyclelr',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
