import sys
from setuptools import setup, find_packages

setup(
    name="pb-amarder",
    version='0.2.3',
    author='Alex Marder',
    # author_email='notlisted',
    description="Custom progress status, primarily for iterators.",
    url="https://github.com/alexmarder/pb-amarder",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    python_requires='>3.6'
)
