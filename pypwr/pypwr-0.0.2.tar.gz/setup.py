import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

     name='pypwr',

     version='0.0.2',

     author="Ernest (Khashayar) Namdar",

     author_email="ernest.namdar@utoronto.ca",

     description="Python version of the pwr R package",

     long_description=long_description,

     long_description_content_type = "text/markdown",

     packages=setuptools.find_packages(),

     classifiers=[

         "Programming Language :: Python :: 3",

         "License :: OSI Approved :: MIT License",

         "Operating System :: OS Independent",

     ],

 )
