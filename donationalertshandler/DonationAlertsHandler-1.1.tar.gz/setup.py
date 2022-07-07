from distutils.core import setup

from setuptools import find_packages

setup(name='DonationAlertsHandler',
      version='1.1',
      description='Donation Alerts Handler',
      author='bezumnui',
      author_email='bezumnui.mistikgt@gmail.com',
      url='https://github.com/TGeniusFamily/DonationAlertsHandler',
      requires=[
          "aiohttp"
      ]
      )
