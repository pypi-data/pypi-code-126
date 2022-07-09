# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['snyk_tags']

package_data = \
{'': ['*']}

install_requires = \
['colorama>=0.4.5,<0.5.0',
 'httpx>=0.20.0,<0.21.0',
 'shellingham>=1.4.0,<2.0.0',
 'typer>=0.5.0']

entry_points = \
{'console_scripts': ['snyk-tags = snyk_tags.tags:app']}

setup_kwargs = {
    'name': 'snyk-tags',
    'version': '0.3.0',
    'description': 'Tool designed to add tags in bulk to Snyk projects',
    'long_description': "# Snyk Tags Tool\n\nSnyk Tags is a CLI tool with two purposes:\n\n- Help filter Snyk projects by product type by adding product tags across a Snyk Group or Organization - using ```snyk-tags tag```\n- Help filter Snyk projects by applying tags to a collection of projects (for example a git repo like **snyk-labs/nodejs-goof**) - using ```snyk-tags collection```\n\n### snyk-tags tag\n\n```snyk-tags tag``` is a CLI tool that uses the Snyk Project API to assign tags in bulk to Snyk projects based on the product type.\n\n```snyk-tags tag``` will update all projects of the specified product type within a Snyk Group or Organization with the product's tag.\n\nYou can also specify a custom tag for the products.\n\n### snyk-tags collection\n\n```snyk-tags collection``` uses the Snyk Project API to assign tags to all projects within a collection. A collection encompasses one or more projects in Snyk, for example:\n\n- **snyk-labs/nodejs-goof** is a collection from a git import\n- **library/httpd** is a collection from a container import\n- **/snyk-labs/nodejs-goof** is a collection from a CLI import\n\nOnce you run ```snyk-tags```, go into the UI, naviagate to the projects page and find the tags filter options on the left-hand menu. Select the tag you have applied and you will visualize all projects associated.\n\n## Installation and requirements\n\n### Requirements\n\nRequires Python version above 3.6\n\n### Installation\n\nTo install the simplest way is to use pip:\n\n```bash\npip install snyk-tags\n```\n\nAlternatively you can clone the repo and then run the following commands:\n\n```python\npoetry install # To install dependencies\npython -m snyk-tags # To run snyk-tags\n```\n\n## Examples\n\nI want to filter all my Snyk Code projects to the whole Snyk Group:\n\n``` bash\nsnyk-tags tag sast --group-id=abc --token=abc\n```\n\nI want to filter all my ```npm``` Snyk Open Source projects within a specific Snyk Organization:\n\n``` bash\nsnyk-tags tag sca --scatype=npm --org-id=abc --token=abc\n```\n\nI want to filter all projects within my ```snyk-labs/nodejs-goof``` repo as ```project:snyk```\n\n``` bash\nsnyk-tags collection apply --collectionname=snyk-labs/nodejs-goof --org-id=abc --token=abc --tagkey=project --tagvalue=snyk\n```\n",
    'author': 'EricFernandezSnyk',
    'author_email': 'eric.fernandez@snyk.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/EricFernandezSnyk/snyk-tags-tool',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
