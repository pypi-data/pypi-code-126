from setuptools import setup, find_packages

try:
    with open("README.md") as f:
        long_description = f.read()
except IOError:
    long_description = ""

try:
    with open("requirements.txt") as f:
        requirements = [x.strip() for x in f.read().splitlines() if x.strip()]
except IOError:
    requirements = []

setup(name='msm-calc',
      install_requires=requirements,
      version='1.2',
      description='calculadora',
      author='michel miranda',
      author_email='micheldsmiranda@gmail.com',
      packages=find_packages(),
      long_description=long_description,
      zip_safe=False
     )

#python setup.py sdist bdist_wheel
#python setup.py sdist bdist
#twine upload --repository testpypi dist/*