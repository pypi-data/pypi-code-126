import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gridlessEngine",                     # This is the name of the package
    ulr="https://github.com/PackTheCommand/gridlessEngine",
    version="0.0.2",                        # The initial release version
    
    author="PackTheCommand",                     # Full name of the author
    description="An simple Engine for Aplication and App design",
    long_description = "this Engine is based on 'Tkinter' canvas Window an is a 2D cubeHitbox based Engine",     # Long description read from the the readme file
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages("os","sys"),    # List of all python modules to be installed
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.9',                # Minimum version requirement of the package
    py_modules=["gridlessEngine"],             # Name of the python package
    package_dir={'':'gridlessEngine/src'},     # Directory of the source code of the package
    install_requires=["pynput","psutil","pyautogui"]                     # Install other dependencies if any
)





