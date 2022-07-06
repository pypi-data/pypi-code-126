# coding: utf-8

# @Time:2020/3/15 12:34
# @Auther:sahala


from setuptools import setup, find_packages  # 这个包没有的可以pip一下

setup(
    name="httprunner_zt",  # 这里是pip项目发布的名称
    version="1.5.15.1.1",  # 版本号，数值大的会优先被pip
    keywords=("pip", "httprunner_zt", "featureextraction"),
    description="httprunner定制化",
    long_description="用例中接口失败后间隔一段时间后重试",
    license="MIT Licence",

    url="https://github.com/",  # 项目相关文件地址，一般是github
    author="liyubin",
    author_email="1399393088@qq.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[
        "certifi==2019.11.28",
        "charset-normalizer==2.0.12",
        "colorama==0.4.3",
        "colorlog==4.1.0",
        "har2case==0.3.1",
        # "HttpRunner==1.5.15",
        "idna==2.8",
        "Jinja2==2.10.3",
        "MarkupSafe==1.1.1",
        "pip==21.1.2",
        "PyYAML==5.2",
        "requests==2.27.1",
        "requests-toolbelt==0.9.1",
        "setuptools==57.0.0",
        "urllib3==1.26.9",
        "wheel==0.36.2",
    ]  # 这个项目需要的第三方库
)

# 步骤：

# 1.setup.py放在被打包同级
# 本地打包项目文件
# python setup.py sdist

# 2.上传项目到pypi服务器
# pip install twine
# twine upload dist/name.tar.gz

# 3.下载上传的库
# pip install name


