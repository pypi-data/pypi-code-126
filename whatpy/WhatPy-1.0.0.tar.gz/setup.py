from setuptools import setup, find_packages


setup(
    name='WhatPy',
    version='1.0.0',
    license='GNU GPLv3',
    author="Koder9",
    author_email='Notpublic@example.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/Koder9/Python-whatapp',
    keywords='Python whatsapp automation',
    install_requires=[
          'pyautogui',
      ],

)