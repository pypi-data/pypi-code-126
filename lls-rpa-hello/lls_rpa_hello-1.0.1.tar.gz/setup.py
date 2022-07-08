# coding=utf-8
"""
============================
Desc:         功能描述
Author:       xiandongliang
Create Date:  2022/07/07
Pip list:     特殊依赖的第三方库说明
============================
"""
from setuptools import find_packages, setup

setup(
    name='lls_rpa_hello',  # 包名
    version='1.0.1',  # 版本
    description='lls_rpa_hello',  # 包简介
    # long_description=open('README.md').read(),  # 读取文件中介绍包的详细内容
    include_package_data=True,  # 是否允许上传资源文件
    author='xianddd',  # 作者
    author_email='xianddd@126.com',  # 作者邮件
    # maintainer='',  # 维护者
    # maintainer_email='',  # 维护者邮件
    license='MIT License',  # 协议
    url='https://pypi.org/user/xianddd/',  # github或者自己的网站地址
    packages=find_packages(),  # 包的目录
    # classifiers=[
    #     'Development Status :: 3 - Alpha',
    #     'Intended Audience :: Developers',
    #     'Topic :: Software Development :: Build Tools',
    #     'License :: OSI Approved :: MIT License',
    #     'Programming Language :: Python :: 3',  # 设置编写时的python版本
    # ],
    python_requires='>=3.6',  # 设置python版本要求
    install_requires=['requests'],  # 安装所需要的库
    entry_points={
        'console_scripts': [
            ''],
    },  # 设置命令行工具(可不使用就可以注释掉)

)

if __name__ == '__main__':
    pass
