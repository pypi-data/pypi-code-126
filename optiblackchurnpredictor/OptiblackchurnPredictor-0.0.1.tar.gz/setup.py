from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='OptiblackchurnPredictor',
  version='0.0.1',
  description='SaaS Churn Predictor',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Rohan Joshi',
  author_email='rohan@optiblack.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Churn', 
  packages=find_packages(),
  install_requires=[''] 
)
