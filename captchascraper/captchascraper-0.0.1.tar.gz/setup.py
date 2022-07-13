from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()





setup(name='captchascraper',
      version="0.0.1",
      description='Captcha Bypass API',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/zearakun/captchascraper',
      install_requires=['requests'],
      author='zearadiscord',
      author_email='info@2captcha.com',
      packages=find_packages(),
      include_package_data=True,
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      python_requires='>=3.6',
      test_suite='tests')