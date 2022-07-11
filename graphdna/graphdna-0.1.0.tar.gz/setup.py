# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['graphdna',
 'graphdna.detectors',
 'graphdna.entities',
 'graphdna.entities.interfaces',
 'graphdna.heuristics',
 'graphdna.heuristics.gql_queries',
 'graphdna.heuristics.web_properties']

package_data = \
{'': ['*']}

install_requires = \
['JSON-log-formatter>=0.5.1,<0.6.0', 'aiohttp[speedups]>=3.8.1,<4.0.0']

entry_points = \
{'console_scripts': ['graphdna = graphdna:cli']}

setup_kwargs = {
    'name': 'graphdna',
    'version': '0.1.0',
    'description': 'Fast and powerful GraphQL engine fingerprinting tool',
    'long_description': '# GraphDNA ![PyPI](https://img.shields.io/pypi/v/GraphDNA)\n\n[![CI](https://github.com/Escape-Technologies/GraphDNA/actions/workflows/ci.yaml/badge.svg)](https://github.com/Escape-Technologies/GraphDNA/actions/workflows/ci.yaml) [![CD](https://github.com/Escape-Technologies/GraphDNA/actions/workflows/cd.yaml/badge.svg)](https://github.com/Escape-Technologies/GraphDNA/actions/workflows/cd.yaml)\n\n![PyPI - License](https://img.shields.io/pypi/l/GraphDNA) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/GraphDNA)\n![PyPI - Downloads](https://img.shields.io/pypi/dm/GraphDNA)\n\n[View on pypi!](https://pypi.org/project/GraphDNA/)\n\n## Getting Started\n\nI takes only two simple step to fingerprint an endpoint using GraphDNA.\n\n```bash\npip install graphdna\ngraphdna -u https://example.com/graphql\n```\n\nThe full list of supported engines is [here](https://github.com/Escape-Technologies/GraphDNA/blob/main/graphdna/entities/engines.py).\n\n## Documentation\n\n```python\nfrom graphdna import detect_engine, detect_engine_async\nfrom graphdna.entities import GraphQLEngine\n\ndef detect_engine(\n    url: str,\n    headers: dict[str, str] | None = None,\n    logger: logging.Logger | None = None,\n) -> GraphQLEngine | None:\n    ...\n\n\nasync def detect_engine_async(\n    url: str,\n    headers: dict[str, str] | None = None,\n    logger: logging.Logger | None = None,\n) -> GraphQLEngine | None:\n    ...\n```\n\n## Contributing\n\nPull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.\n\nPlease make sure to update tests as appropriate.\n\n## License\n\n[MIT](https://choosealicense.com/licenses/mit/)\n',
    'author': 'Escape Technologies SAS',
    'author_email': 'ping@escape.tech',
    'maintainer': 'Swan',
    'maintainer_email': 'swan@escape.tech',
    'url': 'https://escape.tech/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<=3.11',
}


setup(**setup_kwargs)
