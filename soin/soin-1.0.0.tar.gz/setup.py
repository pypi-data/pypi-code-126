from setuptools import setup, find_packages

setup(
    name='soin',
    version='1.0.0',
    url='https://github.com/louis-she/spider.git',
    author='Chenglu',
    author_email='chenglu.she@gmail.com',
    description='my spiders',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'soin = soin.cli:cli',
        ],
    }
)
