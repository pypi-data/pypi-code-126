# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['exo_k', 'exo_k.atm_evolution', 'exo_k.two_stream', 'exo_k.util']

package_data = \
{'': ['*']}

install_requires = \
['astropy>=4.3.1',
 'h5py>=3.7.0',
 'llvmlite>=0.38.1',
 'matplotlib>=3.5.2',
 'numba>=0.55.2',
 'numpy>=1.21.6',
 'pandas>=1.3.5',
 'scipy>=1.7.3']

setup_kwargs = {
    'name': 'exo-k',
    'version': '1.2.0',
    'description': 'Library to handle radiative opacities from various sources for atmospheric applications',
    'long_description': "# Exo_k\n\nAuthor: Jeremy Leconte (CNRS/LAB/Univ. Bordeaux)\n\n`Exo_k` is a Python 3 based library to handle radiative opacities from various sources for atmospheric applications.\nIt enables you to:\n\n* Interpolate efficiently and easily in correlated-k and cross section tables.\n* Convert easily correlated-k and cross section tables from one format to another\n  (hdf5, LMDZ GCM, Exomol, Nemesis, PetitCode, TauREx, ExoREM, ARCIS, etc.).\n* Adapt precomputed correlated-k tables to your needs by changing:\n\n  * the resolution and quadrature (g) grid,\n  * the pressure/temperature grid.\n* Create tables for a mix of gases using tables for individual gases.\n* Create your own tables from high-resolution spectra (for example from K-spectrum, Helios-K, etc.).\n* Use your data in an integrated radiative transfer framework to simulate planetary atmospheres.\n  \nFor a complete online documentation, checkout:\nhttp://perso.astrophy.u-bordeaux.fr/~jleconte/exo_k-doc/index.html\n\nIn this repository, you'll find a [tutorial jupyter notebook](https://forge.oasu.u-bordeaux.fr/jleconte/exo_k-public/-/blob/public/tutorial-exo_k.ipynb) that will show you how to do all that\nwith concrete examples that you can run on your own machine. Many important concepts and options are\npresented along the way.\n\nEnjoy!\n\nJ. Leconte\n\n# Acknowledgements\n\nIf you use this library in your research, please acknowledge it by citing\n[Leconte (2021)](https://ui.adsabs.harvard.edu/abs/2021A%26A...645A..20L/abstract):\n\n  * Spectral binning of precomputed correlated-k coefficients. **Astronomy and Astrophysics** 645. Leconte, J. 2021. doi:10.1051/0004-6361/202039040\n\nThis project has received funding from the European Research Council (ERC)\nunder the European Union's Horizon 2020 research and innovation programme\n(grant agreement n° 679030/WHIPLASH).\n\nThe framework for this documentation has been developped by Aurelien Falco using Sphinx.\nThe Framework for automatic testing has been developped by Alexandre Mechineau. \n\n# last release (see past releases below)\n\nv1.2.0 (July 2022): The model for atmospheric evolution is finally stable and documented.\nThe atm module has also seen several note worthy additions: surface albedo, oceans. \nWe also added a framework for an automatic test suite. In particular, we can test several python versions. Additional tests should rapidly come along.\nRosseland and Planck mean opacities can now be computed from radiative tables. \n\n# Installation\n\nExo_k can be installed using pip (without cloning the repository;\ndependencies should be downloaded automatically):\n```\npip install exo_k\n```\nOr by running the [setup.py](https://forge.oasu.u-bordeaux.fr/jleconte/exo_k-public/-/blob/public/setup.py) script in the cloned repository:\n```\npython setup.py install\n```\n\n# Usage\n\nTo learn how to use `exo_k`, you can follow the [tutorial jupyter notebook](https://forge.oasu.u-bordeaux.fr/jleconte/exo_k-public/-/blob/public/tutorial-exo_k.ipynb).\n\nHave fun!\n\n# Links\n\n* Project homepage: http://perso.astrophy.u-bordeaux.fr/~jleconte/\n* Code repository: https://forge.oasu.u-bordeaux.fr/jleconte/exo_k-public\n* Documentation: http://perso.astrophy.u-bordeaux.fr/~jleconte/exo_k-doc/index.html\n* Contact: jeremy.leconte at u-bordeaux.fr\n\n\n# past releases\n\nv1.1.0 (August 2021): New scheme for the computation of atmospheric emission/transmission\nto ensure an improved numerical accuracy. The variable names to instantiate atm objects have\nchanged accordingly (see tutorial). \n\nv1.0.2 (June 2021): Adds a few missing dependencies. Enables computation of thermal\nemission spectra with scattering through the two-stream method (full documentation pending). \nEnables creating Xtables for a mix of gases (CIA can be added as well). Solves some issues\nwith the 2018 Hitran CIA format.\n\nv1.0.1 (Jan 2021): Solves a binary/string conversion issue introduced by version 3 of h5py.\nEnables linear interpolation in pressure (default is log). Enables creation of\nempty tables to be filled later and extension of the spectral range of existing tables. \n\nv1.0.0 (Dec 2020): Finally our first official version. Creation of a\n'examples' notebook with fully worked out use cases for the `Exo_k`. \n\nv0.0.5 (Oct 2020): Ensures compatibility with latest Exomol correlated-k and cross-section tables.",
    'author': 'Jeremy Leconte',
    'author_email': 'jeremy.leconte@u-bordeaux.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://forge.oasu.u-bordeaux.fr/jleconte/exo_k-public',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<3.10',
}


setup(**setup_kwargs)
