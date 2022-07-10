from distutils.core import setup

setup(
    name='corlyutils',
    version='0.0.8',
    py_modules=['corlyutils.mysql_helper', 'corlyutils.mongo_helper', 'corlyutils.logging_helper',
                'corlyutils.http_helper'],
    author='test',
    author_email='xiaoxiangmuyu@gmail.com',
    url='https://corly.cc/',
    description='hello util',
    install_requires=[
        'requests',
        'pymongo',
        'mysqlclient'
    ]
)
