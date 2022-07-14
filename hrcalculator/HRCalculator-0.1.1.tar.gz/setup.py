import setuptools
setuptools.setup(
name='HRCalculator',
version='0.1.1',
author="Abdulrahman Badr",
author_email="aba884682@gmail.com",
description="it's package uses the ppg signal to calculate heart rate using a robost peak detection algorithm which gives very accurate results for small periods of time about 10s and may be down to 6s but it's not recommended for medical applications ",
packages=setuptools.find_packages(),
classifiers=[
"Programming Language :: Python :: 3",
"License :: OSI Approved :: MIT License",
"Operating System :: OS Independent",
],
)