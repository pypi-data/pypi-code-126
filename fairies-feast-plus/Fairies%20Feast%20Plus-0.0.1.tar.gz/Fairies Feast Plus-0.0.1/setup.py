from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'A package for many things'
LONG_DESCRIPTION = 'Fairies Feast Plus(or ffp) is a python package that does a variety of things.'

# Setting up
setup(
    name="Fairies Feast Plus",
    version=VERSION,
    author="William Caesar",
    author_email="<fairiesfeast6@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["alexa-reply", "opencv-python", "gtts"],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    keywords=['python', 'ffp', "fairies feast plus", "ffm.pw"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)