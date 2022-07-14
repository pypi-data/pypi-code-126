from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Developers',
  'Operating System :: MacOS',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='tfinputfn',
  version='2.0.0',
  description='An input function for tensorflow. ',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Vijay Satheesh',
  author_email='vijayskk007@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='tensorflow', 
  packages=find_packages(),
  install_requires=[''] 
)