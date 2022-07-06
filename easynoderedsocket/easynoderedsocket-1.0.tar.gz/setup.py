from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='easynoderedsocket',
    version='1.0',
    license='Apache 2.0',
    author="Siwat Sirichai",
    author_email='siwat@siwatinc.com',
    long_description=readme(),
    long_description_content_type="text/markdown",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/SiwatINC/siwat-light-control-protocol',
    keywords='nodered',
    install_requires=[
          'wheel'
      ],

)