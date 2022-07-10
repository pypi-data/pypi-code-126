# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['sjtuq']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.6.0,<3.0.0']

setup_kwargs = {
    'name': 'sjtu-questionnaire',
    'version': '0.1.0',
    'description': 'A Python binding to SJTU Questionnaire API (https://wj.sjtu.edu.cn/)',
    'long_description': '# SJTU Questionnaire\n\n![requests>=2.6.0](https://img.shields.io/badge/requests-%3E%3D2.6.0-yellowgreen) ![python version support](https://img.shields.io/pypi/pyversions/requests)\n\n[Chinese Simplied / 简体中文](readme_zh-cn.md)\n\nA simple unofficial Python implementation of [SJTU Questionnaire API](https://wj.sjtu.edu.cn/). Supports multi-processing.\n\n## Installation\n\n```bash\npip install sjtu-questionnaire\n```\n\n## Quick Start\n\n```python\nimport sjtuq as Q\n\n# Create form object\nform = Q.SJTUQuestionnaire("https://wj.sjtu.edu.cn/api/v1/public/export/83f581b4cfd3be8897bcabb23b25ef30/json")\n# Get all answers\nanswers = form.get_all_data() # Get all data as a list\n\nprint("# Answers:", len(answers)) # 1. Only Kunologist have answered this questionnaire!\n```\n\n## Documentation\n\nThe documentation is generated using [`pydoctor`](https://github.com/twisted/pydoctor), hosted on [GitHub Pages](https://gennadiyev.github.io/sjtu-questionnaire/index.html) \n\n',
    'author': 'Kunologist',
    'author_email': 'kunologist@foxmail.com',
    'maintainer': 'Kunologist',
    'maintainer_email': 'kunologist@foxmail.com',
    'url': 'https://github.com/Gennadiyev/sjtuq',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
