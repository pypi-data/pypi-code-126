from setuptools import setup, find_packages

classifier = [
    'Development Status :: 5 - Production/Stable' ,
    'Intended Audience :: Education' ,
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Proggramming Language :: Python :: 3'
]

setup(
    name = 'sagar_basic_calculator',
    version = '0.0.1',
    description = 'A very Basic Calculator' ,
    Long_description = open('readme.txt').read() + '\n\n' + open('changelog.txt').read(),
    url='',
    author = 'Sagar KAkkar',
    author_email='sagarkakkar.btmech20@pec.edu.in',
    Licence = 'MIT',
    keywords = 'calculator',
    packages = find_packages(),
    install_requires = ['']
    )