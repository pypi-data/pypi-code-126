# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_acc_calculate']

package_data = \
{'': ['*']}

install_requires = \
['nonebot-adapter-onebot>=2.0.0-beta.1,<3.0.0', 'nonebot2>=2.0.0-beta.4,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-acc-calculate',
    'version': '0.1.0',
    'description': 'Nonebot2 段位单曲acc计算',
    'long_description': '# nonebot-plugin-acc-calculate\nmalodyv3段位计算单曲acc\n## 使用方式\n聊天框输入  \n`acc`  \n\n`malody`  \n\n`acc计算`  \n\n`单曲acc计算`  \n\n然后按步骤提供信息\n## 关于\n目前支持v3regular、ex和reform\n',
    'author': '10-24',
    'author_email': '1750011571@qq.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/10-24/nonebot-plugin-acc-calculate',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.3,<4.0.0',
}


setup(**setup_kwargs)
