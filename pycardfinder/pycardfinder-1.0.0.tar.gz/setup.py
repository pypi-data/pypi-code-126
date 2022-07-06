from setuptools import setup

setup(
    name='pycardfinder',
    packages=['pycardfinder'],
    version='1.0.0',
    license='GPL-3.0 license',
    description='PyCardFinder is a cross-platform tool for searching filesystems for credit card information written in Python',
    author='Felix Cheruiyot',
    author_email='felix@intasend.com',
    url='https://github.com/felixcheruiyot/pycardfinder',
    download_url='https://github.com/felixcheruiyot/pycardfinder/archive/v_1.0.0.tar.gz',
    keywords=['cards', 'pci', 'card', 'pycardfinder', 'card scan'],
    install_requires=[
        "card-identifier==1.0",
        "click==8.1.3",
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python :: 3',
    ]
)