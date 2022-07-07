from setuptools import setup, find_packages


setup(
    name='gascomp',
    version='1.0.9',
    description='GasComp',
    long_description='GasComp',
    author='Michael Fischer',
    author_email='mfischer.sw@gmail.com',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.6, <4',
    project_urls={
        'Source': 'https://github.com/mfischersw/GasComp/',
    }
)
