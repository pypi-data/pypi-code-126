from setuptools import setup, find_packages

setup(
name='nonebot_plugin_kawaii_robot',
version='1.0.1',
description='使用Kyomotoi / AnimeThesaurus的nonebot2的回复（文i）插件',
author='karisaya',
author_email='1048827424@qq.com',
license='AGPL License',
packages=find_packages(),
package_data = {'resource':['.json'],},
platforms='all',
url='https://github.com/KarisAya/nonebot_plugin_kawaii_robot',
)