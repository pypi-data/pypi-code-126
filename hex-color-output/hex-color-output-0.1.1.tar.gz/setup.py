from setuptools import setup, find_packages


setup(
    name='hex-color-output',
    version='0.1.1',
    license='MIT',
    author="Cownex",
    author_email='contact@cownex.de',
    packages=find_packages('source'),
    package_dir={'': 'source'},
    url='https://github.com/Cownex/HexOutput',
    keywords='python hex color terminal output color-output',
)