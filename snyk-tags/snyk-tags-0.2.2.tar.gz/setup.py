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
    'version': '0.2.2',
    'description': 'Tool designed to add tags in bulk to Snyk projects',
    'long_description': "# Snyk Tags Tool\n\nSnyk Tags is a CLI tool with one purpose:\n- Help filter Snyk projects by product type by adding product tags across a Snyk Group or Organization\n\nSnyk Tags is a CLI tool that uses the Snyk Project API to assign tags in bulk to Snyk projects based on the product type.\n\nSnyk Tags will update all projects of the specified product type within a Snyk Group or Organization with the product's tag.\n\nYou can also specify a custom tag for the products.\n\nOnce you run snyk-tags, go into the UI, naviagate to the projects page and find the tags filter options on the left-hand menu. Select the Product tag and the product as the key. All your Snyk projects from a specific product will be shown via this filter.\n\n## Installation and requirements\n\n### Requirements\n\nRequires Python version above 3.6\n\n### Installation\n\nTo install the simplest way is to use pip:\n\n```bash\npip install snyk-tags\n```\n\nAlternatively you can clone the repo and then run the following commands:\n\n```python\npoetry install # To install dependencies\npython -m snyk-tags # To run snyk-tags\n```\n\n## Examples\n\nI want to filter all my Snyk Code projects to the whole Snyk Group:\n```\nsnyk-tags apply sast --groupid=abc --token=abc\n```\n\nI want to filter all my npm Snyk Open Source projects within a specific Snyk Organization:\n```\nsnyk-tags apply sast --scatype=npm --orgid=abc --token=abc\n```\n\n\n## Usage\n\n**Usage:** snyk-tags [OPTIONS] COMMAND [ARGS]\n\n**COMMAND**:\n\n- apply: ```snyk-tags apply --help```\n  - container: ```snyk-tags apply container```\n    - Used to tag Snyk Container projects [default: deb]\n  - iac: ```snyk-tags apply iac```\n    - Used to tag Snyk IaC projects [default: iac]\n  - sast: ```snyk-tags apply sast```\n    - Used to tag Snyk Code projects [default: sast]\n  - sca: ```snyk-tags apply sca```\n    - Used to tag Snyk Open Source projects [default: mvn]\n  - custom: ```snyk-tags apply custom```\n    - Used to create a custom tag for the projects\n\n**OPTIONS**:\n\n- **[-v, --version]**: ```snyk tags -v```\n- **[--containertype]**: ```snyk-tags apply container --containertype=deb```\n  - Define the type of Snyk Container projects to tag\n- **[--scatype]**: ```snyk-tags apply sca --scatype=maven```\n  - Define the type of Snyk Open Source projects to tag\n- **[--projecttype]**: ```snyk-tags apply custom --projecttype=maven --tagkey=Type --tagvalue=Value```\n  - Define the type of project to tag, must be accompanied by ```tagkey``` and ```tagvalue```\n- **[--tagkey]**: ```snyk-tags apply custom --projecttype=deb --tagkey=Type --tagvalue=Value```\n  - Define the custom tag\n- **[--tagvalue]**: ```snyk-tags apply custom --projecttype=iac --tagkey=Type --tagvalue=Value```\n  - Define the value of the custom tag\n\n**ARGS**:\n\n- **[--group-id]**: ```snyk tags sast --group-id=abc```\n  - Define the Group ID you want to apply the tags to\n  - Can also be imported as an environment variable\n- **[--org-id]**: ```snyk tags sast --org-id=abc```\n  - Define the Organization ID you want to apply the tags to\n  - Can also be imported as an environment variable\n- **[--token]**: ```snyk-tags apply sast --token=abc```\n  - Define the Snyk API Token you want to use (needs Group access by default)\n  - Can also be imported as an environment variable\n",
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
