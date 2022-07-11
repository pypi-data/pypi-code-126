from setuptools import setup, find_packages

setup(
    name = 'pysaver',
    version = '0.0.2',
    py_modules = ['pysaver'],
    author = 'M J Lally',
    author_email = 'm.j.lally@outlook.com',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    description = "A simple utility to save python REPL history to file.",
    url = 'https://github.com/mjlally/pysaver',
    license = 'MIT',
    keywords = 'pysaver',
)
