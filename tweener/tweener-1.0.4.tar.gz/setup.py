from setuptools import setup, find_packages

VERSION = '1.0.4'
DESCRIPTION = 'Helper functions for easing and tweening'

# Setting up
setup(
    name="tweener",
    version=VERSION,
    author="Gin Ryu Rabino",
    author_email="ginryurabino@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    keywords=['python', 'animation', 'easing']
)
