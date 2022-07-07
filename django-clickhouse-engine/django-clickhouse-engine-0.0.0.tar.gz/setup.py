import setuptools


setuptools.setup(
    name='django-clickhouse-engine',
    version='0.0.0',
    author='Vladimir Chebotarev',
    description='ClickHouse database backend for Django',
    packages=['django_clickhouse_engine'],
    install_requires=[
        'Django'
    ]
)
