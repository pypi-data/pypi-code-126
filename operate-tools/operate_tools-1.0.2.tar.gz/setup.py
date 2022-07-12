#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   setup.py
@Time    :   2022/07/12 10:17:09
@Author  :   Desire
@Version :   1.0
@Desc    :   None
"""

import os
import sys

sys.path.insert(1, os.getcwd())
# here put the import lib

from setuptools import setup, find_packages


filepath = os.path.join(os.getcwd(), 'README.md')
setup(
    name="operate_tools",
    version="1.0.2",
    description="Python操作工具合集",
    long_description=open(filepath, encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/Joker-desire/operate-tools",
    author="Joker-desire",
    author_email="2590205729@qq.com",
    requires=['pytest'],
    packages=find_packages(),
    license="MIT Licence",
    data_files=[filepath],
    platforms="any"
)
