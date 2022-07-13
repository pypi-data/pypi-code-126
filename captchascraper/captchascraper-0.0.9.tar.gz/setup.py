from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()





setup(name='captchascraper',
      version="0.0.9",
      description='Captcha Bypass API',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/zearakun/captchascraper',
      install_requires=['requests'],
      author='zearadiscord',
      packages=find_packages(),
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ]
     )