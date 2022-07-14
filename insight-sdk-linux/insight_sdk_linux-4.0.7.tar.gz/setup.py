from setuptools import find_packages
from setuptools import setup

setup(
    name="insight_sdk_linux",
    author="htsc",
    version="4.0.7",
    author_email="insight@htsc.com",
    description="insight_sdk_linux",
    long_description="insight_sdk_linux",
    license='insightpythonsdklinux',
    project_urls={
        'Documentation': 'https://packaging.python.org/tutorials/distributing-packages/',
        'Funding': 'https://donate.pypi.org',
        'Source': 'https://github.com/pypa/sampleproject/',
        'Tracker': 'https://github.com/pypa/sampleproject/issues',
    },

    packages=['insight_sdk_linux',
              'insight_sdk_linux/com',
              'insight_sdk_linux/com/interface',
              'insight_sdk_linux/com/cert',
              'insight_sdk_linux/com/insight',

              'insight_sdk_linux/com/libs/linux/python36',
              'insight_sdk_linux/com/libs/linux/python37',
              'insight_sdk_linux/com/libs/linux/python39',
              'insight_sdk_linux/com/libs/linux/python310',

              ],

    package_dir={
                 'insight_sdk_linux/com/cert': 'insight_sdk_linux/com/cert',

                 'insight_sdk_linux/com/libs/linux/python36':
                     'insight_sdk_linux/com/libs/linux/python36',
                 'insight_sdk_linux/com/libs/linux/python37':
                     'insight_sdk_linux/com/libs/linux/python37',
                 'insight_sdk_linux/com/libs/linux/python39':
                     'insight_sdk_linux/com/libs/linux/python39',
                 'insight_sdk_linux/com/libs/linux/python310':
                     'insight_sdk_linux/com/libs/linux/python310',
                 },

    package_data={
        'insight_sdk_linux/com/cert': ['HTInsightCA.crt', 'InsightClientCert.pem', 'HTISCA.crt', 'InsightClientKeyPkcs8.pem'],
        
        'insight_sdk_linux/com/libs/linux/python36': ['_mdc_gateway_client.so', 'libACE.so.6.4.3', 'libACE_SSL.so.6.4.3', 'libprotobuf.so.11',
                                                "libmdc_query_client.so", "mdc_gateway_client.py"],
        'insight_sdk_linux/com/libs/linux/python37': ['_mdc_gateway_client.so', 'libACE.so.6.4.3', 'libACE_SSL.so.6.4.3', 'libprotobuf.so.11',
                                                "libmdc_query_client.so", "mdc_gateway_client.py"],
        'insight_sdk_linux/com/libs/linux/python39': ['_mdc_gateway_client.so', 'libACE.so.6.4.3', 'libACE_SSL.so.6.4.3', 'libprotobuf.so.11',
                                                "libmdc_query_client.so", "mdc_gateway_client.py"],
        'insight_sdk_linux/com/libs/linux/python310': ['_mdc_gateway_client.so', 'libACE.so.6.4.3', 'libACE_SSL.so.6.4.3', 'libprotobuf.so.11',
                                                "libmdc_query_client.so", "mdc_gateway_client.py"],

        },

    install_requires=[],

    python_requires='>=3.6.*',
)
