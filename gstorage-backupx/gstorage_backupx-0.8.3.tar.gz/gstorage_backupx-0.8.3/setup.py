from setuptools import setup, find_packages


setup(
    name='gstorage_backupx',
    version='0.8.3',
    license='MIT',
    author="Rodrigo F. Sacht",
    author_email='rodrigofsacht@gmail.com',
    packages=find_packages('.'),
    package_dir={'': 'src'},
    url='https://bitbucket.org/offertech/gstorage_backup',
    keywords='gcp storage backup',
    install_requires=[
          'wheel',
          'google-cloud-storage',
          'fire',
          'python-dotenv',
          'python-slugify'
      ],
    entry_points={
    'console_scripts': [
        'gstorage_backup = gstorage_backup:main',
    ],
},

)