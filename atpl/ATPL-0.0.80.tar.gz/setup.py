from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ATPL',
    version='0.0.80',
    packages=setuptools.find_packages(),
    url='https://github.com/pypa/sampleproject',
    license='MIT',
    author=' MA JIANLI',
    author_email='majianli@corp.netease.com',
    description='With this Toolset and one audio cable you can simply built end2end audio test paltform base on mac,which means,Its very Lightweight，Easy to build and carry',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
    'gooey',
    'paramiko',
    'wave',
    'applescript',
    'sounddevice',
    'numpy',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    data_files=[
                ('', ['ATPL/dylib/matchsig.dylib']),
                ('', ['ATPL/src/speech.wav']),
                ],

    python_requires='>=3.7',
)

