from setuptools import setup, find_packages
import os

current = os.getcwd()

setup(
    name='FairAlerts',
    version='1.0.0',
    description='A third party alert system interface.',
    url='https://github.com/chazzcoin/fairalerts',
    author='ChazzCoin',
    author_email='chazzcoin@gmail.com',
    license='BSD 2-clause',
    packages=find_packages(),
    package_data={
        'Resources': ['*.txt']
    },
    install_requires=['FCoRE>=1.0.3', 'discord-webhook>=0.16.3'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)