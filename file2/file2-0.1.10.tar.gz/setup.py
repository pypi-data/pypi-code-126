import sys

from setuptools import setup, find_packages

version = sys.argv[1]
del sys.argv[1]

setup(
    name="file2",
    version='0.1.' + version,
    author='Alex Marder',
    # author_email='notlisted',
    description="File opener for gzip, bzip2, xz, or uncompressed files.",
    url="https://github.com/alexmarder/file2",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    python_requires='>3.6'
)
