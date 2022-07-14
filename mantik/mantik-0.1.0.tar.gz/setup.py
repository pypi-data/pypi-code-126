# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['mantik',
 'mantik.compute_backend_service',
 'mantik.mlflow_server',
 'mantik.mlflow_server.flask',
 'mantik.mlflow_server.flask.api',
 'mantik.mlflow_server.flask.api.models',
 'mantik.mlflow_server.gunicorn',
 'mantik.mlflow_server.tokens',
 'mantik.mlflow_server.tokens.cognito',
 'mantik.testing',
 'mantik.tracking',
 'mantik.tracking._server',
 'mantik.unicore',
 'mantik.unicore._config',
 'mantik.utils']

package_data = \
{'': ['*']}

install_requires = \
['Flask>=2.1.2,<3.0.0',
 'boto3>=1.23.6,<2.0.0',
 'fastapi>=0.78.0,<0.79.0',
 'mlflow>=1.24.0,<2.0.0',
 'pydantic>=1.9.0,<2.0.0',
 'python-jose>=3.3.0,<4.0.0',
 'python-multipart>=0.0.5,<0.0.6',
 'pyunicore>=0.9.16,<0.10.0',
 'requests>=2.27.1,<3.0.0',
 'spython>=0.2.1,<0.3.0',
 'uvicorn[standard]>=0.17.6,<0.18.0']

entry_points = \
{'mlflow.project_backend': ['unicore = mantik.unicore.backend:UnicoreBackend']}

setup_kwargs = {
    'name': 'mantik',
    'version': '0.1.0',
    'description': 'mantik for mlflow',
    'long_description': None,
    'author': 'Fabian Emmerich',
    'author_email': 'fabian.emmerich@4-cast.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://mantik.ai/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
