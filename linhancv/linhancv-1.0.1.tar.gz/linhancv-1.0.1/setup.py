from distutils.core import setup
from setuptools import find_packages


REQUIRES_PYTHON = '>=3.8.0'


with open("requirements.txt", "r") as f:
    REQUIRED = f.read()

with open("README.rst", "r") as f:
    long_description = f.read()

setup(
    name='linhancv',  # 包名
    version='1.0.1',  # 版本号
    description='A small example package',
    long_description=long_description,
    author='南林笑笑生',
    author_email='gin.linhan@gmail.com',
    url='https://voldemortgin.github.io',
    install_requires=[],
    license='MIT',
    python_requires=REQUIRES_PYTHON,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    platforms=["all"],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries'
    ],
)
