# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['abortion_policies']

package_data = \
{'': ['*'],
 'abortion_policies': ['Gestational Limits/HTML/*',
                       'Gestational Limits/JSON/*',
                       'Gestational Limits/MP3/*',
                       'Gestational Limits/Markdown/*',
                       'Gestational Limits/Mindmap/*',
                       'Gestational Limits/PNG/*',
                       'Gestational Limits/SVG/*',
                       'Gestational Limits/Spreadsheet/*',
                       'Gestational Limits/Text/*',
                       'Gestational Limits/YAML/*',
                       'Insurance Coverage/HTML/*',
                       'Insurance Coverage/JSON/*',
                       'Insurance Coverage/MP3/*',
                       'Insurance Coverage/Markdown/*',
                       'Insurance Coverage/Mindmap/*',
                       'Insurance Coverage/PNG/*',
                       'Insurance Coverage/SVG/*',
                       'Insurance Coverage/Spreadsheet/*',
                       'Insurance Coverage/Text/*',
                       'Insurance Coverage/YAML/*',
                       'Minors/HTML/*',
                       'Minors/JSON/*',
                       'Minors/MP3/*',
                       'Minors/Markdown/*',
                       'Minors/Mindmap/*',
                       'Minors/PNG/*',
                       'Minors/SVG/*',
                       'Minors/Spreadsheet/*',
                       'Minors/Text/*',
                       'Minors/YAML/*',
                       'Waiting Period/HTML/*',
                       'Waiting Period/JSON/*',
                       'Waiting Period/MP3/*',
                       'Waiting Period/Markdown/*',
                       'Waiting Period/Mindmap/*',
                       'Waiting Period/PNG/*',
                       'Waiting Period/SVG/*',
                       'Waiting Period/Spreadsheet/*',
                       'Waiting Period/Text/*',
                       'Waiting Period/YAML/*']}

install_requires = \
['CairoSVG>=2.5.2,<3.0.0',
 'Jinja2>=3.1.2,<4.0.0',
 'PyYAML>=6.0,<7.0',
 'gTTS>=2.2.4,<3.0.0',
 'requests>=2.28.1,<3.0.0',
 'rich-click>=1.5.1,<2.0.0']

entry_points = \
{'console_scripts': ['abortion_policies = abortion_policies.script:run']}

setup_kwargs = {
    'name': 'abortion-policies',
    'version': '1.0.0',
    'description': 'Easy to read abortion policies by state from the Abortion Policy API',
    'long_description': '# abortion_policies\nEasy to read abortion policies from the abortion policy API\n\nThis code is built using the [AbortionPolicyAPI](https://www.abortionpolicyapi.com/)\n\n## Installation\nIf you want to install and run the code yourself you will first need an API key. You can apply for an API key here:\n\n[AbortionPolicyAPI](https://www.abortionpolicyapi.com/request-access)\n\nOnce you have an API token you can pip install this application\n\n```console\npip install abortion_policies\n```\n\n## Running the code\nThen you can run the software and supply your API token\n\n```console\nabortion_policies \n\nAbortion API Token: <supply token>\n```\n\nThen you can review the output\n\n## Consuming the Code\nIf you simply want to consume the output from the API you can Git clone the repository locally which will include all of the generated documents\n\n```console\ngit clone https://github.com/automateyournetwork/abortion_policies\n```\n### VS Code Extensions\nYou can use VS Code to browse and view all of the various file types using the following extensions \n#### Excel Preview\nUsed to preview the CSV files \n#### Markdown Preview\nUsed to preview the markdown files\n#### Markmap\nUsed to preview and generate the mind maps\n#### Open in Default Browser\nUsed to view the HTML data tables and SVG files \n(Right click on the file, select Open in Default Browser)\n\n#### Audio-preview\nUsed to listen to the MP3 files',
    'author': 'John Capobianco',
    'author_email': 'ptcapo@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
