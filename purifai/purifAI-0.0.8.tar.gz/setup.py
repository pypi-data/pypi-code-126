from setuptools import setup, find_packages

VERSION = '0.0.8' 
DESCRIPTION = 'purifAI package'
LONG_DESCRIPTION = 'SPE & LCMS Method Prediction Python package'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="purifAI", 
        version=VERSION,
        author="Ying Ying Cheung, Luke Perrin, Jennifer Amis",
        author_email="<yycheungds@gmail.com>,<luperrin@westmont.edu>,<jenamis@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'purifAI'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
