import sys

from setuptools import setup, find_packages

# version = ''
# if sys.argv[1].startswith('version='):
#     version = '.' + sys.argv[1].partition('=')[2]
#     del sys.argv[1]
# elif sys.argv[1] != 'test':
#     print('Warning: no version number supplied.', file=sys.stderr)

setup(
    name="file2",
    # version='0.1' + version,
    version='0.2.15',
    author='Alex Marder',
    # author_email='notlisted',
    description="File opener for gzip, bzip2, xz, or uncompressed files.",
    url="https://github.com/alexmarder/file2",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    python_requires='>3.6'
)
