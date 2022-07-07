from setuptools import setup, find_packages


setup(
    name='gstorage_backupx',
    version='0.7.2',
    license='MIT',
    author="Rodrigo F. Sacht",
    author_email='rodrigofsacht@gmail.com',
    packages=find_packages('.'),
    package_dir={'': 'src'},
    url='https://bitbucket.org/offertech/gstorage_backup',
    keywords='gcp storage backup',
    install_requires=[
          'google-cloud-storage',
          'fire',
          'python-dotenv',
          'python-slugify',
          'wheel'
      ],

)