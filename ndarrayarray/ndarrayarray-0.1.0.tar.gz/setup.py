import versioneer
from setuptools import setup

setup(
    name='ndarrayarray',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=['ndarrayarray'],
    url='',
    license='',
    author='Gabriel Beckers',
    author_email='gabriel@gbeckers.nl',
    description='A memory-mapped array of arbitrarily shaped numpy ndarrays.',
    install_requires=['darr'],
)
