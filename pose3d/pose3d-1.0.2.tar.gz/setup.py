from setuptools import setup, find_packages

VERSION = '1.0.2'
DESCRIPTION = 'Transforming and handling poses.'

# Setting up
setup(
    name="pose3d",
    version=VERSION,
    author="John Halazonetis",
    author_email="<john.halazonetis@icloud.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['numpy', 'scipy'],
    keywords=['python', 'pose', 'transform'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
