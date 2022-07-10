from setuptools import setup, find_packages

setup(
    name='ztDemo',
    version='0.0.26',
    description='a common test framework support for both UI and API test with run in parallel ability.',
    author='kevin.cai',
    author_email='不告诉你@outlook.com',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(include=['ztDemo', 'ztDemo.*']),
    install_requires=[
        'requests',
        'selenium',
        'concurrent_log_handler',
        'PyYAML',
        'openpyxl',
        'PyMySQL',
        'assertpy',
        'xlrd'
    ],
    license='MIT',
    url='https://www.testertalk.com',
    entry_points={
        'console_scripts': [
            'ztDemo = ztDemo.main:main'
        ]
    }
)
