# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cjk_textwrap']

package_data = \
{'': ['*']}

install_requires = \
['jieba>=0.42.1,<0.43.0']

setup_kwargs = {
    'name': 'cjk-textwrap',
    'version': '0.1.0',
    'description': 'A flexible textwrapper for CJK string',
    'long_description': "## CJK Textwrap\n\n`cjk-textwrap`是Python 3.6`textwrap`模块的[中日韩字符](https://en.wikipedia.org/wiki/CJK_characters)兼容版本。此外，它提供了灵活的接口以便用户自定义分词器（如[结巴分词](https://github.com/fxsjy/jieba)）。\n\n`cjk-textwrap` is a [CJK characters](https://en.wikipedia.org/wiki/CJK_characters) compatible version of Python 3.6's `textwrap` module. Moreover, it provides flexible interfaces which allows users to define their own text segmentation for text wrapping like [jieba](https://github.com/fxsjy/jieba).\n\n### Installation 安装\n\npip:\n\n```bash\npip install cjk-textwrap\n```\n\npoetry:\n\n```bash\npoetry add cjk-textwrap\n```\n\n### Feature 功能特性\n\nAlthough user can get various language support by adding their custom splitter, `cjk-textwrap` provides built-in `English-Chinese` mixed text phrase wrapping support.\n\n虽然可以通过自定义分词器添加各种语言的支持，但是`cjk-textwrap`提供了原生的*中-英文*混合句支持。\n\n- [x] Chinese Support 中文支持\n- [ ] Japanese Support 日文支持\n- [ ] Korean Support 韩文支持\n\n### LICENSE 协议许可\n\nThis project is licensed under MIT.\n",
    'author': 'Carbene',
    'author_email': 'hyikerhu0212@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Hyiker/cjk-textwrap',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
