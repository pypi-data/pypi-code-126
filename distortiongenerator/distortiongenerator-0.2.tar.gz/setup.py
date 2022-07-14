from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='distortiongenerator',
    version='0.2',
    license='MIT',
    packages=find_packages(),
    url='https://github.com/louzi233/DistortionGenerator',
    install_requires=[
        'opencv-python',
        'numpy',
        'Pillow',
      ],
    long_description=long_description,
    long_description_content_type="text/markdown",

)