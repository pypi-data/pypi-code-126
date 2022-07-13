# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['psi_score']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.23.1,<2.0.0', 'progressbar2>=4.0.0,<5.0.0', 'scipy>=1.8.1,<2.0.0']

setup_kwargs = {
    'name': 'psi-score',
    'version': '0.1.0',
    'description': 'Metric of user influence in Online Social Networks',
    'long_description': '# Psi-score\n\nMetric of user influence in Online Social Networks\n\n## Installation\n\n```bash\n$ pip install psi-score\n```\n\n## Usage\n\n```python\n>>> from psi_score import PsiScore\n>>> adjacency = {0: [1, 3], 1: [0, 2], 2: [0, 1, 3], 3: [0]}\n>>> lambdas = [0.23, 0.50, 0.86, 0.19]\n>>> mus = [0.42, 0.17, 0.10, 0.37]\n>>> psiscore = PsiScore()\n>>> scores = psiscore.fit_transform(adjacency, lambdas, mus)\n>>> scores\narray([0.21158803, 0.35253745, 0.28798439, 0.14789014])\n>>> np.round(scores, 2)\narray([0.21, 0.35, 0.29, 0.15])\n```\n\n## License\n\n`psi-score` was created by Nouamane Arhachoui. It is licensed under the terms of the MIT license.\n',
    'author': 'Nouamane Arhachoui',
    'author_email': 'nouamane.arhachoui@lip6.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/NouamaneA/psi-score',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
