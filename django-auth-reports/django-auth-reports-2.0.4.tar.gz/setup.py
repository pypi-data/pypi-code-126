# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['auth_reports']

package_data = \
{'': ['*'], 'auth_reports': ['static/admin/js/*', 'static/auth_reports/css/*']}

setup_kwargs = {
    'name': 'django-auth-reports',
    'version': '2.0.4',
    'description': 'Adds csv reports for auth groups, right-side filtering for filter_horizontal m2m widgets',
    'long_description': "\nDjango Auth Reports\n===================\n\nA Django application that:  \n-Adds csv downloads of group permissions  \n-Adds right-side filtering in m2m filter_horizontal widgets\n\nCompatibility\n=============\n\nFor Django 1.x, use django-auth-reports 1.x\n\nFor Django 2.x, use django-auth-reports 2.x\n\nInstallation\n============\n\n    $ pip install django-auth-reports\n\nAdd the following to the top of the INSTALLED_APPS in your project's settings file, above django.contrib.admin and django.contrib auth:\n\n    'auth_reports',\n\nCollect static media:\n\n   ``manage.py collectstatic``\n",
    'author': 'Imagescape',
    'author_email': 'info@imagescape.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ImaginaryLandscape/django-auth-reports',
    'packages': packages,
    'package_data': package_data,
}


setup(**setup_kwargs)
