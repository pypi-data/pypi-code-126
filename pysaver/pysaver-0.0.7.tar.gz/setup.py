from setuptools import setup, find_packages
from pathlib import Path


this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name = 'pysaver',
    version = '0.0.7',
    py_modules = ['pysaver'],
    author = 'M J Lally',
    author_email = 'm.j.lally@outlook.com',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    long_description = long_description,
    long_description_content_type='text/markdown',
    url = 'https://github.com/mjlally/pysaver',
    license = 'MIT',
    keywords = 'pysaver',
)
