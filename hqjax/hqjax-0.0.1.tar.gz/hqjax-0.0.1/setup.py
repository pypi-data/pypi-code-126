from __future__ import print_function
from setuptools import setup, find_packages
import sys
filepath = 'README.md'

setup(
    name="hqjax",
    version="0.0.1",
    author="J2hu",  #作者名字
    author_email="",
    description="hybrid quantum NNs packages for jax.",
    long_description=open(filepath, encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    license="MIT",
    url="",  #github地址或其他地址
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Environment :: Web Environment",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft',
        'Operating System :: Unix',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=[
            'numpy>=1.14.0',   #所需要包的版本号
    ],
    python_requires=">=3.6",
)
