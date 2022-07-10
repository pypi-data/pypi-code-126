from setuptools import setup, find_packages

VERSION = '1.0.0' 
DESCRIPTION = 'F1 Telemetry Display'
LONG_DESCRIPTION = 'F1 Telemetry Data Display'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="f1tel", 
        version=VERSION,
        author="Barbato Federico",
        author_email="barbato.federico01@outlook.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=["fastf1",
                            "pandas",
                            "numpy",
                            "matplotlib"],
        
        keywords=['python', 'formula 1', 'telemetry', 'display', 'f1'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)