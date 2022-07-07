from distutils.core import setup
from setuptools import find_packages

with open("README.rst", "r") as f:
  long_description = f.read()

setup(name="FLARE22_DSC_NSD_TEST",
      version="0.0.1",
      description="FLARE22_DSC_NSD_Evaluation",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/JunMa11/FLARE",
      author="Cheng Ge",
      author_email="13851520957@163.com",
      install_requires=[],
      license="MIT",
      packages=find_packages(),
      platforms=["all"],
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Natural Language :: Chinese (Simplified)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Topic :: Software Development :: Libraries'
      ],
      )