from setuptools import setup, find_packages

setup(
name='sceleto2',
license='LICENSE',
author='Jongeun Park',
author_email='jp24@kaist.ac.kr',
description='package description',

include_package_data=True,
python_requires='>=3.7',

keywords=['sceleto', 'single cell', 'scRNA-seq'],

packages=find_packages(include=['sceleto2','sceleto2.*','.']),

install_requires=[
   'pandas',
   'numpy',
   'scanpy',
   'scipy',
   'seaborn',
   'networkx',
   'python-igraph',
   'bbknn',
   'geosketch',
   'joblib',
   'datetime',
   'harmonypy',
   'matplotlib',
   'geosketch',
   'scrublet',
   'adjustText',
   'numba',
   'scikit-learn',
   ],
version='1.0.2',
long_description=open('README.md').read(),
long_description_content_type='text/markdown',
zip_safe=False,
)