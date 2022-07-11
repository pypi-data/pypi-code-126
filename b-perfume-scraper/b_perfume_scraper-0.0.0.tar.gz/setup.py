from setuptools import setup
from setuptools import find_packages

setup(
    name = 'b_perfume_scraper',
    versions = '0.0.1',
    description = 'A package that retrieves image and text data about perfumes on the Bloom Perfumery website',
    url = 'https://github.com/emm-sam/Data-Collection-Pipeline',
    author = 'Emma Samouelle',
    license='MIT',
    packages = find_packages(), 
    install_requires=[
        'pandas',
        'psycopg2-binary',
        'urllib3',
        'boto3',
        'botocore',
        's3transfer',
        'requests',
        'sqlalchemy',
        'botocore',
        'selenium',
        'SQLAlchemy',
        'webdriver_manager',
        'PyYaml'
        ])

