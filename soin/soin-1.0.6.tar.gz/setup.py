from setuptools import setup, find_packages

setup(
    name='soin',
    version='1.0.6',
    url='https://github.com/louis-she/soin.git',
    author='Chenglu',
    author_email='chenglu.she@gmail.com',
    description='tool set for spiders',
    long_description="tool set for spiders",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'soin = soin.cli:cli',
        ],
    }
)
