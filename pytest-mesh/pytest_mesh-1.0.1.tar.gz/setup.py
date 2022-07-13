#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
pytest_mesh 打包文件
@author:zhaojiajun
@file:setup.py
@time:2022/07/13
"""

from setuptools import setup

setup(
    name='pytest_mesh',
    version='1.0.1',
    author="zhaojiajun",
    author_email='zhaojiajun@baicizhan.com',
    description='pytest_mesh插件',
    packages=['pytest_mesh'],
    # 需要安装的依赖
    install_requires=[
        'autodoraemon==1.0.0',
        'pytest==7.1.2',
        'allure-pytest==2.9.45'
    ],
    entry_points={
        'pytest11': [
            'pytest-mesh = pytest_mesh.main',
        ]
    }
)

if __name__ == '__main__':
    pass
