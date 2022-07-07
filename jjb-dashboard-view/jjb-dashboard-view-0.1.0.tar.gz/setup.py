from setuptools import setup
from jjb_dashboard_view import __version__

setup(
    name='jjb-dashboard-view',
    version=__version__,
    description='Jenkins Job Builder Dashboard View',
    url='https://github.com/oseleznov',
    author='Vasyl Stetsuryn, Oleksii Seleznov',
    author_email='alexey.seleznov@gmail.com',
    license='Apache-2.0 license',
    install_requires=[],
    entry_points={
      'jenkins_jobs.views': [
      'dashboard = jjb_dashboard_view.view_dashboard:Dashboard']},
    packages=['jjb_dashboard_view'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'])
