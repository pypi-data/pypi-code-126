from distutils.core import setup
from setuptools import find_packages

setup(name='countRunTime',  # 对外我们模块的名字
      version='5.0.0',  # 版本号
      description='测试本地发布模块',  # 描述
      long_description='测试本地发布模块',  # 描述
      author='Lugwit',  # 作者
      author_email='1485179300@qq.com',
      license='BSD License',
      packages=['countRunTime'],
      package_dir={'countRunTime': 'countRunTime'},
      include_package_data=True,
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
          'Programming Language :: Python :: 3.9',
          'Topic :: Software Development :: Libraries'
      ],
      )