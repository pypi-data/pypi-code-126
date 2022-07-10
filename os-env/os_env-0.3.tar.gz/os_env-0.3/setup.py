from setuptools import setup, find_packages


setup(
    name='os_env',
    version='0.3',
    license='MIT',
    author="bob ross",
    author_email='jocktmp+ebwhs@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    keywords='os env .env os-env os_env dotenv',
    install_requires=[
          'python-dotenv',
      ],

)