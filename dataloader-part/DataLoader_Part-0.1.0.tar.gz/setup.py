from setuptools import setup

setup(
    name='DataLoader_Part',
    version='0.1.0',
    description='Data Loader Python package',
    author='Ali Rahmati',
    author_email='alirahmati@outlook.com',
    license='BSD 2-clause',
    packages=['data_loader_part'],
    install_requires=['pandas',
                      'json5'],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
