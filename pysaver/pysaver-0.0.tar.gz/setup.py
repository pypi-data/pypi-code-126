from setuptools import setup, find_packages

setup(
    name = 'pysaver',
    version = '0.0',
    py_modules = ['pysaver'],
    author = 'M J Lally',
    author_email = 'm.j.lally@outlook.com',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    url = 'https://github.com/mjlally/pysaver',
    license = 'MIT',
    keywords = 'pysaver',
)
