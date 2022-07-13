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
  version='0.0.5',
  description='Basic caching tool',
  long_description='Basic caching tool\nUse example:\n\nCacheSys.WriteCache("example.txt", "example text", ".")\n\na = CacheSys.ReadCache("example.txt", ".")\n\nif a == "example text":\n    print(a)',
  url='',  
  author='LeahYes',
  author_email='LeahYesX@gmail.com',
  license='MIT',
  classifiers=classifiers,
  keywords='cache', 
  packages=find_packages(),
  install_requires=[''] 
)