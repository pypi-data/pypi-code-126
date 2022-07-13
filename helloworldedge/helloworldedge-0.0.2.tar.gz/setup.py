# colab Python 3.7.13
# python -m venv env && source ./env/bin/activate
# python -m pip install -U pip wheel setuptools
# python setup.py sdist
# pip install twine
# twine upload dist/*

from setuptools import setup, find_packages

install_requires = []

setup(
    name='helloworldedge',
    version='0.0.2',
    description='helloworldedge',
    author='Happy Puppy',
    packages=find_packages(),
    install_requires=install_requires,
)

