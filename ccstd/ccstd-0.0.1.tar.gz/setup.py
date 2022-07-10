import setuptools

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setuptools.setup(
    name = 'ccstd',
    version = '0.0.1',
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