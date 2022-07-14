from setuptools import setup, find_packages


# Setting up
setup(
    name="convertinhours",
    version='1.0',
    author="Pratik Giri",
    author_email="<mail@neuralnine.com>",
    description='',
    long_description_content_type="text/markdown",
    long_description='',
    packages=find_packages(),
    install_requires=['openpyxl', 'pandas'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)