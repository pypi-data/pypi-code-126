import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name='tsopt',
    version='0.0.1',
    description="Easily solve any multi-stage transshipment cost minimization optimization problem",
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/ryayoung/tsopt',
    license='MIT',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
    ],
    author="Ryan Young",
    author_email='ryanyoung99@live.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    keywords='opendata socrata colorado crime',
    install_requires=[
          'pandas',
          'pyomo',
    ],
    python_requires='>=3.9'


)
