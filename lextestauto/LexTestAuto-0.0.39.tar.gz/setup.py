# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : setup.py
# Time       ：2022/2/12 15:51
# Author     ：Lex
# email      : 2983997560@qq.com
# Description：项目描述
"""
from setuptools import setup, find_packages


# 第三方依赖
requires = [
    "pywin32>=303",
    "comtypes>=1.1.0",
    "Pillow>=9.0.1"
]

setup(
    name='LexTestAuto',
    version='0.0.39',
    packages=find_packages(),
    license='MIT',
    author='Lex',
    description='Lex软件工作室测试包',
    install_requires=requires,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='==3.8.8',
    package_data={
        '': ['*.dll', "*.pyd"]
    }
)

