# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cqase', 'cqase.api', 'cqase.common']

package_data = \
{'': ['*']}

install_requires = \
['install>=1.3.5,<2.0.0', 'pip>=22.1.2,<23.0.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'cqase-client',
    'version': '0.1.3',
    'description': 'Custom qase client',
    'long_description': '[![Python tests](https://github.com/berpress/custom-qase-client/actions/workflows/python-app.yml/badge.svg)](https://github.com/berpress/custom-qase-client/actions/workflows/python-app.yml)\n![versions](https://img.shields.io/pypi/pyversions/pybadges.svg)\n[![Downloads](https://static.pepy.tech/personalized-badge/cqase-client?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads)](https://pepy.tech/project/cqase-client)\n# custom-qase-client\n\nThis is an unofficial client [QASE](https://qase.io)\n\nOfficial client: https://github.com/qase-tms/qase-python\n\nAPI QASE: https://developers.qase.io/reference/\n\nGuide: https://developers.qase.io/docs\n\n### Installation\n\n------------\n\nYou can install via pip\n```\n$ pip install cqase-client\n```\nor with poetry\n```\n$ poetry add -D cqase-client\n```\n\n### How to work\n\n------------\n\nFirst, get api token from page https://app.qase.io/user/api/token (See guide)\n\nFor body and params use dict type, like in [requests](https://requests.readthedocs.io/en/latest/user/quickstart/#more-complicated-post-requests) library\n\n```python\nfrom cqase.client import QaseClient\n\nclient = QaseClient(api_token=\'YOUR_API_TOKEN\')\n\ncode = \'CODE\'  # project code\n# create project\nbody = {\'title\': f\'Title test project\', \'code\': code, \'access\': \'all\'}\nclient.projects.create(body=body)\n\n# create suite\nbody = {"title": "test suit"}\nclient.suites.create(code=code, body=body)\n\n# create case\nbody = {"title": "test case"}\nclient.cases.create(code=code, body=body)\n\n# create test run\nbody = {"title": "test run"}\nclient.runs.create(code=code, body=body)\n\n# upload attachment\nclient.attachments.upload(code, "./cat.jpeg")\n\n# finish test run\nclient.runs.complete(code=code, uuid=1)\n\n```\n',
    'author': 'alexanderlozovoy',
    'author_email': 'berpress@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/berpress/custom-qase-client',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
