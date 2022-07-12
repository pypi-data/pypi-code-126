from setuptools import setup, find_packages

NAME = "kdp-python-connector"
VERSION = "0.5.0"
DESCRIPTION = 'Python Connector for KDP Platform'
LONG_DESCRIPTION = 'Python Connector For Interacting with KDP Platform for various ingestion and retrieval tasks'


# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name=NAME,
        version=VERSION,
        author="Koverse development team",
        author_email="developer@koverse.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['pandas', 'numpy'], # add any additional packages that
        # needs to be installed along with your package. Eg: 'caer'

        keywords=['python', 'kdp'],
        # classifiers= [
        #     "Development Status :: 3 - Alpha",
        #     "Intended Audience :: Science/Research",
        #     "Intended Audience :: Developers",
        #     "Programming Language :: Python :: 3.8",
        #     "Operating System :: MacOS :: MacOS X",
        # ]
)
