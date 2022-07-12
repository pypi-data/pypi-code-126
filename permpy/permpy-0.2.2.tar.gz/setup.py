# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['permpy',
 'permpy.InsertionEncoding',
 'permpy.PegPermutations',
 'permpy.RestrictedContainer',
 'permpy.deprecated']

package_data = \
{'': ['*']}

install_requires = \
['pytest>=7.1.2,<8.0.0']

setup_kwargs = {
    'name': 'permpy',
    'version': '0.2.2',
    'description': 'A package for analyzing permutation patterns.',
    'long_description': "permpy\n=======\n\n## A Python Permutations Class\n\nContains Various tools for working interactively with permutations. \nEasily extensible.\n\n### Examples:\n```python\n>>> import permpy as pp\n>>> \n>>> p = pp.Perm.random(8)\n>>> p\n 5 4 7 1 6 2 3 8 \n>>> p.cycles()\n'( 6 2 4 1 5 ) ( 7 3 ) ( 8 )'\n>>> p.order()\n10 \n>>> p ** p.order()\n 1 2 3 4 5 6 7 8\n>>>\n>>> S = pp.PermSet.all(6)\n>>> S\nSet of 720 permutations\n>>> S.total_statistic(pp.Perm.num_inversions)\n5400\n>>> S.total_statistic(pp.Perm.num_descents)\n1800\n>>> \n>>> A = pp.AvClass([ 132 ])\n>>> A\n[Set of 0 permutations, \n Set of 1 permutations, \n Set of 2 permutations, \n Set of 5 permutations, \n Set of 14 permutations, \n Set of 42 permutations, \n Set of 132 permutations, \n Set of 429 permutations, \n Set of 1430 permutations]\n>>> \n```\n\n## Build Instructions\nFor a summary of how PermPy is built, go [here](https://py-pkgs.org/03-how-to-package-a-python#summary-and-next-steps).\n```bash\n$ python -m poetry build\n$ python -m poetry publish\n```",
    'author': 'Michael Engen',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
