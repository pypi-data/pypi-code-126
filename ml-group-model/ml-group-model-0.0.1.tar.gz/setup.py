from setuptools import setup, find_packages


def requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()


setup(
    name='ml-group-model',
    version='0.0.1',
    author='Mirko',
    description='A model for the ml group',
    install_requires=requirements(),
    packages=find_packages(),
)