from setuptools import setup

setup(
    name='cameo_table',
    version='0.2.1',
    description='modify table file, and save modified file result',
    long_description = open('README.md','r',encoding='utf-8').read(),
    long_description_content_type = 'text/markdown',
    release_notes='fixed bugs, added documentation',
    url='https://github.com/bohachu/cameo_table',
    author='JC Wang',
    author_email='jcxgtcw@gmail.com',
    license='BSD 2-clause',
    packages=['cameo_table'],
    install_requires=[
        'fastparquet==0.8.1',
        'numpy==1.22.3',
        'pandas==1.4.2',
        'polars==0.13.40',
        'pyarrow==7.0.0',
        'requests==2.28.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)