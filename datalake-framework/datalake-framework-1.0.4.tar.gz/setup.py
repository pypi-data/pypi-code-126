# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['datalake', 'datalake.provider']

package_data = \
{'': ['*']}

install_requires = \
['Babel>=2.10.1,<3.0.0',
 'azure-eventhub>=5.9.0,<6.0.0',
 'azure-identity>=1.10.0,<2.0.0',
 'azure-keyvault-secrets>=4.4.0,<5.0.0',
 'azure-storage-blob>=12.12.0,<13.0.0',
 'boto3>=1.23.3,<2.0.0',
 'google-cloud-monitoring>=2.9.1,<3.0.0',
 'google-cloud-pubsub>=2.12.1,<3.0.0',
 'google-cloud-secret-manager>=2.10.0,<3.0.0',
 'google-cloud-storage>=2.3.0,<3.0.0',
 'influxdb-client>=1.28.0,<2.0.0',
 'pendulum>=2.1.2,<3.0.0',
 'requests>=2.27.1,<3.0.0']

extras_require = \
{'all': ['pandas>=1.4.2,<2.0.0'], 'pandas': ['pandas>=1.4.2,<2.0.0']}

setup_kwargs = {
    'name': 'datalake-framework',
    'version': '1.0.4',
    'description': 'Datalake Framework',
    'long_description': "# Datalake Framework\n\nA Python framework for working with a datalake's cloud assets like **data catalog**, **storage**, **monitoring** or **secrets**\n\nThe framework helps making abstraction of cloud resources when developing use-cases for a datalake. Supported cloud providers are\n\n- [Amazon Web Services](https://aws.amazon.com/)\n- [Google Cloud Plaform](https://cloud.google.com/)\n- [Microsoft Azure](https://azure.microsoft.com/)\n\nAdditionnaly, most cloud features in the framework are available for **local development**. Hence developers can work on use-cases without requiring a full cloud insfrastructure or even work offline. \n\n## Installation\n\nUsing pip\n\n```shell\npip install datalake-framework\n```\n",
    'author': 'Didier SCHMITT',
    'author_email': 'dschmitt@equancy.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/equancy/datalake-framework',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
