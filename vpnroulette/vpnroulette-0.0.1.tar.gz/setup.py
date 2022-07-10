"""Setup vpnroulette client"""

# Standard library imports
import pathlib
from setuptools import setup, find_packages
HERE = pathlib.Path(__file__).resolve().parent
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name='vpnroulette',
    version='0.0.1',
    description='VPNROULETTE CLIENT',
    long_description=README,
    long_description_content_type="text/markdown",
    python_requires=">=3.6, <4",
    url='https://github.com/vpnroulette/vpnr-client',
    author='Vpnroulette',
    author_email='hello@vpnroulette.com',
    license='Apache',
    install_requires=['requests==2.27.1',
                      'pyfiglet', 'termcolor','itsdangerous'],
    packages=find_packages(include=['vpnr_client']),
    include_package_data=True,
    entry_points={'console_scripts': ['vpnroulette=vpnr_client.__main__:main']},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
        "Programming Language :: Python",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
