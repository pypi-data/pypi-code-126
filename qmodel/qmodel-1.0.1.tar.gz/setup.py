from setuptools import find_packages, setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='qmodel',
    version='1.0.1',    
    description='package to create a Random Forest Classifier model, to read 7segments display from images ',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Ethan Sebag , Sylvain Perez',
    author_email='ethanspros@hotmail.com , sylvain.perez@q-leap.eu',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['pytest-shutil',
                      'numpy',
                      'scikit-image',
                      
                      'opencv-python',
                      'matplotlib',
                      'pillow',
                      'glob2',
                      'joblib',
                      'seaborn',
                      'scikit-learn', 
                      
                      'sklearn',
                      

                      ],
    keywords=["7-segment", 
              "python", 
              "otp", 
              "Random Forest Classifer", 
              "Random", 
              "Forest",
              "Classifier"
              ],

    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)




