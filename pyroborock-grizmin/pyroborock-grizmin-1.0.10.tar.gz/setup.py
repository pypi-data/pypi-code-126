from setuptools import setup, find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='pyroborock-grizmin',
    version='1.0.10',
    packages=['pyroborock'],
    install_requires=['pytuyapi-ipc', 'python-miio', 'pycryptodome'],
    description='Communicate with roborock over tuya protocol',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/grizmin/pyroborock',
    author='jd89',
    author_email='jd89.dev@gmail.com',
)
