# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dfds_ds_toolbox',
 'dfds_ds_toolbox.analysis',
 'dfds_ds_toolbox.feature_extraction',
 'dfds_ds_toolbox.feature_selection',
 'dfds_ds_toolbox.logging',
 'dfds_ds_toolbox.model_selection',
 'dfds_ds_toolbox.profiling']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.4,<4.0',
 'pandas>=1.0,<2.0',
 'rich>=12.0,<13.0',
 'scikit-learn>=1.0,<2.0',
 'scipy>1.7.2',
 'statsmodels>=0.13,<0.14']

setup_kwargs = {
    'name': 'dfds-ds-toolbox',
    'version': '0.10.1',
    'description': 'A toolbox for data science',
    'long_description': None,
    'author': 'Data Science Chapter at DFDS',
    'author_email': 'urcha@dfds.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://dfds-ds-toolbox.readthedocs.io',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
