from setuptools import setup, find_packages

setup(
    name = 'pysaver',
    version = '0.0.3',
    py_modules = ['pysaver'],
    author = 'M J Lally',
    author_email = 'm.j.lally@outlook.com',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    long_description="""# Pysaver\n\n A simple utility to save python REPL history to file.\n\n""",
    long_description_content_type='text/markdown',
    url = 'https://github.com/mjlally/pysaver',
    license = 'MIT',
    keywords = 'pysaver',
)
