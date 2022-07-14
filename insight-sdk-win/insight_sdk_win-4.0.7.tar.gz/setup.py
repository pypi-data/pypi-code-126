from setuptools import find_packages
from setuptools import setup

setup(
    name="insight_sdk_win",
    author="htsc",
    version="4.0.7",
    author_email="insight@htsc.com",
    description="insight_sdk_win",
    long_description="insight_sdk_win",
    license='insightpythonsdkwin',
    project_urls={
        'Documentation': 'https://packaging.python.org/tutorials/distributing-packages/',
        'Funding': 'https://donate.pypi.org',
        'Source': 'https://github.com/pypa/sampleproject/',
        'Tracker': 'https://github.com/pypa/sampleproject/issues',
    },

    packages=['insight_sdk_win',
              'insight_sdk_win/com',
              'insight_sdk_win/com/interface',
              'insight_sdk_win/com/cert',
              'insight_sdk_win/com/insight',

              'insight_sdk_win/com/libs/python37/x64',
              'insight_sdk_win/com/libs/python36/x64',
              'insight_sdk_win/com/libs/python39/x64',
              'insight_sdk_win/com/libs/python310/x64',

              'insight_sdk_win/com/libs/python37/x86',
              'insight_sdk_win/com/libs/python36/x86',
              'insight_sdk_win/com/libs/python39/x86',
              'insight_sdk_win/com/libs/python310/x86',

              ],

    package_dir={
                 'insight_sdk_win/com/cert': 'insight_sdk_win/com/cert',

                 'insight_sdk_win/com/libs/python37/x64':
                     'insight_sdk_win/com/libs/python37/x64',
                 'insight_sdk_win/com/libs/python36/x64':
                     'insight_sdk_win/com/libs/python36/x64',
                 'insight_sdk_win/com/libs/python39/x64':
                     'insight_sdk_win/com/libs/python39/x64',
                 'insight_sdk_win/com/libs/python310/x64':
                     'insight_sdk_win/com/libs/python310/x64',

                 'insight_sdk_win/com/libs/python37/x86':
                     'insight_sdk_win/com/libs/python37/x86',
                 'insight_sdk_win/com/libs/python36/x86':
                     'insight_sdk_win/com/libs/python36/x86',
                 'insight_sdk_win/com/libs/python39/x86':
                     'insight_sdk_win/com/libs/python39/x86',
                 'insight_sdk_win/com/libs/python310/x86':
                     'insight_sdk_win/com/libs/python310/x86',

                 },

    package_data={
        'insight_sdk_win/com/cert': ['HTInsightCA.crt', 'InsightClientCert.pem', 'HTISCA.crt', 'InsightClientKeyPkcs8.pem'],
        'insight_sdk_win/com/libs/python37/x64': ['_mdc_gateway_client.pyd', 'ACE.dll', 'ACE_SSL.dll', 'libeay32.dll',
                                              "ssleay32.dll", "insight_query_client.dll", "mdc_gateway_client.py"],
        'insight_sdk_win/com/libs/python36/x64': ['_mdc_gateway_client.pyd', 'ACE.dll', 'ACE_SSL.dll', 'libeay32.dll',
                                              "ssleay32.dll", "insight_query_client.dll", "mdc_gateway_client.py"],
        'insight_sdk_win/com/libs/python39/x64': ['_mdc_gateway_client.pyd', 'ACE.dll', 'ACE_SSL.dll', 'libeay32.dll',
                                              "ssleay32.dll", "insight_query_client.dll", "mdc_gateway_client.py"],
        'insight_sdk_win/com/libs/python310/x64': ['_mdc_gateway_client.pyd', 'ACE.dll', 'ACE_SSL.dll', 'libeay32.dll',
                                               "ssleay32.dll", "insight_query_client.dll", "mdc_gateway_client.py"],

        'insight_sdk_win/com/libs/python37/x86': ['_mdc_gateway_client.pyd', 'ACE.dll', 'ACE_SSL.dll', 'libeay32.dll',
                                              "ssleay32.dll", "insight_query_client.dll", "mdc_gateway_client.py"],
        'insight_sdk_win/com/libs/python36/x86': ['_mdc_gateway_client.pyd', 'ACE.dll', 'ACE_SSL.dll', 'libeay32.dll',
                                              "ssleay32.dll", "insight_query_client.dll", "mdc_gateway_client.py"],
        'insight_sdk_win/com/libs/python39/x86': ['_mdc_gateway_client.pyd', 'ACE.dll', 'ACE_SSL.dll', 'libeay32.dll',
                                              "ssleay32.dll", "insight_query_client.dll", "mdc_gateway_client.py"],
        'insight_sdk_win/com/libs/python310/x86': ['_mdc_gateway_client.pyd', 'ACE.dll', 'ACE_SSL.dll', 'libeay32.dll',
                                               "ssleay32.dll", "insight_query_client.dll", "mdc_gateway_client.py"],
        },

    install_requires=[],

    python_requires='>=3.6.*',
)
