from setuptools import setup, find_packages
from os import path
from io import open

# setup file path
here = path.abspath(path.dirname(__file__))
reqs = []

# reading README.md, change if needed
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
# if no README.md exist then un-comment the below line
# long_description = '''<add-your-description-here>'''

# reading pre-requisits if any else comment the block
with open(path.join(here, 'requirements.txt'), encoding='utf-8')as f:
    read_lines = f.readlines()
    reqs = [ each.strip() for each in read_lines]

setup(
    name='badcode',
    version='0.1',
    description="badcode place holder",
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/kirankotari/badcode',
    author = 'Kiran Kumar Kotari',
    author_email = 'kirankotari@live.com',

    install_requires=reqs,
    classifiers = [ 
        'Development Status :: 3 - Alpha',
        # Most common <development-status> are: 
        # 3 - Alpha
        # 4 - Beta
        # 5 - Production/Stable

        'Intended Audience :: Developers',
        # Most common <audience> are:
        # Developers
        # Education
        # Manufacturing
        # Science/Research

        'Topic :: Software Development :: Build Tools',
        # In general <package-for> "Software Development" and <package-useage-at> "Build Tools"

        'License :: OSI Approved :: Apache Software License', 
        # In general <license-approved-by> OSI Approved and <license> MIT License

        # Python version support all sub-version of 2 and 3
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',

        # Un-comment below if your package is for a special purpose
        # 'Framework :: <frame-work>',
        # 'Natural Language :: <language>',
        # 'Operating System :: <os-name>',
        # 'Programming Language :: <programming-language>',
        # 'Topic :: <topic>',
        ],
    keywords = 'badcode, badcode-mutable, badcode-immutable',
    
    # add folder-names which need to be ignored under exclude=[]
    packages = find_packages(where='.', exclude=['tests', 'data']),
    include_package_data=True,
)