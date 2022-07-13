from setuptools import setup, find_packages
import codecs
import os


from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()



VERSION = '0.0.1'
DESCRIPTION = 'CheXpert Classification with EfficientNet B3'
# Setting up
setup(
    name="ChexpertClassifier",
    version=VERSION,
    author="Mehdi Hosseini Moghadam",
    author_email="<m.h.moghadam1996@gmail.com>",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=['pandas',
                      "numpy",
                      "opencv-python",
                      "torch",
                      "torchvision",
                      "tqdm",
                      "sklearn"],
    keywords=['Chexpert', 
              'Chest X-ray',
              'X-ray image classification',
              'Image classification',
              'Computer Vision', 
              'EfficientNet', 
              'EfficientNet B3',
              'Biomedical image classification'
              'Chest X-ray image classification'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)










