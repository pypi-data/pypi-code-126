from gettext import find
from setuptools import setup
from setuptools import find_packages

setup(
    name = 'bloom_scraper',
    versions = '1.0',
    description = 'A package that retrieves image and text data about perfumes on the Bloom Perfumery website',
    url = 'https://github.com/emm-sam/Data-Collection-Pipeline/blob/main/webscraper_project/scraper.py',
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

