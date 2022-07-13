from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='CacheSys',
  version='0.0.2',
  description='Basic caching tool',
  long_description='Basic caching tool',
  url='',  
  author='LeahYes',
  author_email='LeahYesX@gmail.com',
  license='MIT',
  classifiers=classifiers,
  keywords='cache', 
  packages=find_packages(),
  install_requires=[''] 
)