import setuptools

classifiers = [
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setuptools.setup(
    name = 'ccstd',
    version = '0.0.2',
    description = 'CCSTD is a library for logging in Python.',
    long_description = open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url = '',
    author = 'Ceys',
    author_email = 'hidden@hidden.hidden',
    license = 'MIT',
    classifiers = classifiers,
    keywords = '',
    package = setuptools.find_packages(),
    install_requires = ['datetime']
)