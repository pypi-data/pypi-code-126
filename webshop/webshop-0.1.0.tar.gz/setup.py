from setuptools import setup

# List of all classifiers: https://pypi.org/pypi?%3Aaction=list_classifiers

setup(
    name='webshop',
    version='0.1.0',    
    description='Python package for WebShop environment',
    url='https://github.com/princeton-nlp/web-agent-site',
    author='John Yang',
    author_email='jy1682@princeton.edu',
    license='Princeton License',
    packages=['webshop'],
    install_requires=[
        'beautifulsoup4',
        'cleantext',
        'Flask',
        'gym',
        'numpy',
        'pandas',
        'pyserini',
        'PyYAML',
        'rank_bm25',
        'requests',
        'requests_mock',
        'rich',
        'scikit_learn',
        'selenium',
        'spacy',
        'thefuzz',
        'torch',
        'tqdm',
        'train',
        'transformers',
    ],

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: MacOS X",
        "Framework :: Flask",
        "Intended Audience :: Science/Research",
        "License :: Other/Proprietary License",
        "Programming Language :: Python :: 3.8",
    ],
)