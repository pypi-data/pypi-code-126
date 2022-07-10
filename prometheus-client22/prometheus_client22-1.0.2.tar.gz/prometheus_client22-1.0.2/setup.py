from distutils.core import setup

"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='prometheus_client22',
    version='1.0.2',
    py_modules=['prometheus_client22'],
    author='hole',
    author_email='617240374@qq.com',
    description='模块描述',
    long_description='',  # 这里是文档内容, 读取readme文件
    packages=find_packages(),
    python_requires='>=3.6',  # 这里指定python版本号必须大于3.6才可以安装
    install_requires=[]  # 我们的模块所用到的依赖, 这里指定的话, 用户安装你的模块时, 会自动安装这些依赖
)