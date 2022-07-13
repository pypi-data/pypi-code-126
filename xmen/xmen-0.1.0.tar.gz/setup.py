# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xmen',
 'xmen.datasets',
 'xmen.datasets.bronco',
 'xmen.datasets.distemist',
 'xmen.ext.sapbert.evaluation',
 'xmen.ext.sapbert.inference',
 'xmen.ext.sapbert.src',
 'xmen.ext.sapbert.train',
 'xmen.linkers',
 'xmen.linkers.n_grams',
 'xmen.linkers.sapbert',
 'xmen.reranking']

package_data = \
{'': ['*'],
 'xmen': ['ext/sapbert/*', 'ext/sapbert/misc/*', 'ext/sapbert/training_data/*'],
 'xmen.ext.sapbert.evaluation': ['xl_bel/*',
                                 'xl_bel/xlbel_v0.0/*',
                                 'xl_bel/xlbel_v1.0/*']}

install_requires = \
['bioc>=2.0.post3,<3.0',
 'datasets>=2.0.0,<3.0.0',
 'hydra-core>=1.1.1,<2.0.0',
 'langcodes>=3.3.0,<4.0.0',
 'lxml>=4.8.0,<5.0.0',
 'neleval>=3.1.1,<4.0.0',
 'numpy>=1.21,<2.0',
 'protobuf>=3.20.0,<4.0.0',
 'pytorch-metric-learning==0.9.98.dev1',
 'rich>=12.3.0,<13.0.0',
 'sentencepiece>=0.1.96,<0.2.0',
 'transformers>=4.17.0,<5.0.0']

setup_kwargs = {
    'name': 'xmen',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Florian Borchert',
    'author_email': 'florian.borchert@hpi.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.9',
}


setup(**setup_kwargs)
