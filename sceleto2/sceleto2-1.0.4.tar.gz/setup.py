from setuptools import setup, find_packages

setup(
name='sceleto2',
license='MIT',
author='Jongeun Park',
author_email='jp24@kaist.ac.kr',
description='sceleto2 is a wrapper package developed by SCMGL to aid in single cell analysis.',

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
version='1.0.4',
long_description=open('README.md').read(),
long_description_content_type='text/markdown',
zip_safe=False,
)