from setuptools import find_packages, setup


setup(
    name='hnph_utils',
    version='0.0.6',
    author="Yushuo",
    author_email='saltfish@126.com',
    maintainer='Yushuo',
    maintainer_email="saltfish@126.com",
    url='https://www.hnpinhe.cn/',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'certifi==2021.10.8',
        'charset-normalizer==2.0.12',
        'et-xmlfile==1.1.0',
        'idna==3.3',
        'openpyxl==3.0.9',
        'Pillow==9.1.0',
        'reportlab==3.6.9',
        'requests==2.27.1',
        'urllib3==1.26.9',
        'xlrd==2.0.1',
        'xlwt==1.3.0',
        'async-timeout==4.0.2',
        'deprecated==1.2.13',
        'packaging==21.3',
        'pyparsing==3.0.9',
        'redis==4.3.4',
        'wrapt==1.14.1',
    ],
    description='湖南品禾网络科技有限公司，Python开发工具包',
    python_requires='>=3.8',
    license='MIT',
    platforms='Windows|Linux|MacOS',
    long_description='Python 开发时常用的工具集合，包含日期处理、字符串处理、加密处理、Excel处理、PDF处理、二维码处理、ZIP包处理、Redis'
)
