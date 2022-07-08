from setuptools import setup, find_packages

setup(name='hawksoft.ptaScore',
      version='1.0.1',
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # 多文件模块写法
      author="xingyongkang",
      author_email="xingyongkang@cqu.edu.cn",
      description="针对pintia.cn网站教学，生成学生的多次作业成绩总表。",
      long_description=open('./README.md', encoding='utf-8').read(),
      long_description_content_type = "text/markdown",
      #long_description="http://gitee.comg/xingyongkang",
      license="MIT",
      url = "https://gitee.com/xingyongkang/ptaScore",
      include_package_data=True,
      platforms="any",
      install_requires=['openpyxl'],
      keywords='pintia, excel',
      entry_points={
          'console_scripts': [
              'ptaScore = hawksoft.main:main'
          ]
      }
)