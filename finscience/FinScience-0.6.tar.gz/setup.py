from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 4 - Beta',
    'Environment :: MacOS X',
    'Framework :: Jupyter',
    'Intended Audience :: Science/Research',
    'Operating System :: MacOS',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.10'
]

setup(
    name = 'FinScience',
    version = '0.6',
    description = 'A trend indicator and two algoritmic trading strategies based on the alternative data provided by FinScience',
    long_description = open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    author = 'Andrea Frattini',
    author_email = 'andreafrattini20@gmail.com',
    license = 'MIT',
    classifiers = classifiers,
    keywords = 'finscience',
    packages = find_packages()
)