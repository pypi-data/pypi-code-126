#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['pyconverters_grobid']

package_data = \
{'': ['*']}

package_dir = \
{'': 'src'}

install_requires = \
['pymultirole-plugins>=0.5.0,<0.6.0', 'grobid-client==0.8.2', 'requests']

extras_require = \
{'dev': ['flit', 'pre-commit', 'bump2version'],
 'docs': ['sphinx',
          'sphinx-rtd-theme',
          'm2r2',
          'sphinxcontrib.apidoc',
          'jupyter_sphinx'],
 'test': ['pytest',
          'pytest-cov',
          'pytest-flake8',
          'pytest-black',
          'flake8==3.9.2',
          'tox']}

entry_points = \
{'pyconverters.plugins': ['grobid = '
                          'pyconverters_grobid.grobid:GrobidConverter']}

setup(name='pyconverters-grobid',
      version='0.5.83',
      description='Convert PDF to structured text using Grobid',
      author='Olivier Terrier',
      author_email='olivier.terrier@kairntech.com',
      url='https://github.com/oterrier/pyconverters_grobid/',
      packages=packages,
      package_data=package_data,
      package_dir=package_dir,
      install_requires=install_requires,
      extras_require=extras_require,
      entry_points=entry_points,
      python_requires='>=3.8',
     )
