from os import path

from setuptools import setup, find_packages

current_dir = path.abspath(path.dirname(__file__))
with open(path.join(current_dir, 'README.md')) as f:
    description = f.read()

setup(
    name='tether-price',
    packages=find_packages(),
    version='0.0.2',
    license='MIT',
    description='Tether Price is a library that helps you to get the Tether price from various websites.',
    long_description=description,
    long_description_content_type='text/markdown',
    author='Ali Fotouhi',
    author_email='the.alif.dev@gmail.com ',
    url='https://github.com/iAliF/Tether-Price',
    download_url='https://github.com/iAliF/Tether-Price/archive/refs/tags/v0.0.1-alpha.tar.gz',
    install_requires=['requests'],
    keywords=[
        'Tether', 'Tether price', 'Tether price to RIAL', 'Tether price to IRR'
    ],
    project_urls={
        'Documentation': 'https://github.com/iAliF/Tether-Price/',
        'Source': 'https://github.com/iAliF/Tether-Price/',
        'Bug Tracker': 'https://github.com/iAliF/Tether-Price/issues',
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ]
)
