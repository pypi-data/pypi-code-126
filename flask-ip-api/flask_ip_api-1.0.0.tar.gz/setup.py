import setuptools

setuptools.setup(
  name="flask_ip_api",
  version="1.0.0",
  author="EpicCodeWizard2",
  author_email="epiccodewizard@gmail.com",
  description="Gives access to client IP information.",
  long_description=open("README.md", "r").read(),
  long_description_content_type="text/markdown",
  url="https://replit.com/@EpicCodeWizard2/Flask-IP-Info-Extension",
  packages=setuptools.find_packages(),
  install_requires=[
    "werkzeug",
    "flask",
    "requests"
  ],
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ]
)