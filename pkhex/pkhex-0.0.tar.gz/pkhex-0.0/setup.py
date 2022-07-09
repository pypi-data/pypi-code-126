import sys
from setuptools import setup

args = ' '.join(sys.argv).strip()
if not any(args.endswith(suffix) for suffix in ['setup.py check -r -s', 'setup.py sdist']):
    raise ImportError('Python bindings for PKHeX. Parked for upcoming work on the Pocket/Hammerspace project. If you believe that it has been parked in error, please contact the package owner.')

setup(
    author='Fakas',
    author_email='matthew@caza.ly',
    classifiers=['Development Status :: 7 - Inactive'],
    description='Python bindings for PKHeX. Parked for upcoming work on the Pocket/Hammerspace project. If you believe that it has been parked in error, please contact the package owner.',
    long_description='Python bindings for PKHeX. Parked for upcoming work on the Pocket/Hammerspace project. If you believe that it has been parked in error, please contact the package owner.',
    name='pkhex',
    url='https://github.com/MCazaly',
    version='0.0'
)
