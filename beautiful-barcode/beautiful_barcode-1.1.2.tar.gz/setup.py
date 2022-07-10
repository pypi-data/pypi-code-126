# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['beautiful_barcode']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'beautiful-barcode',
    'version': '1.1.2',
    'description': 'Generate nicely formatted barcodes (UPC-A and EAN)',
    'long_description': "# beautiful_barcode\nGenerate well-formatted, production-ready Barcodes.\n\nBy default, existing Python barcode libraries like [python-barcode](https://pypi.org/project/python-barcode/) generate good barcodes, but any and all formatting of the text is left up to the user. beautiful_barcode generates a nicely formatted barcode with interleaved text out of the box:\n\n![Example barcode](example_path.svg)\n\nDepending on your renderer (and true by default), text in the barcode is *not* an SVG `<text>` element, as such an elment may render differently on different machines depending on font availability.\n\nThis library is currently limited to UPC-A/EAN and EPS/SVG – that's all we (the original authors) needed. Patches welcome!\n\n# Installation\n\n```sh\n$ pip install beautiful_barcode\n```\n\n# Usage\n\n```\n>>> from beautiful_barcode import GTIN\n>>> GTIN('123456789012').write('output.svg')\n```\n\nCommand line:\n\n```sh\n$ python -m beautiful_barcode 123456789012 -o output.svg\n```\n\n## Quickstart\n\n```bash\n~$ git clone https://github.com/boxine/beautiful_barcode.git\n~$ cd beautiful_barcode\n~/beautiful_barcode$ make\nhelp                 List all commands\ninstall-poetry       install or update poetry\ninstall              install via poetry\nupdate               Update the dependencies as according to the pyproject.toml file\nlint                 Run code formatters and linter\nfix-code-style       Fix code formatting\ntox-listenvs         List all tox test environments\ntox                  Run pytest via tox with all environments\ntox-py36             Run pytest via tox with *python v3.6*\ntox-py37             Run pytest via tox with *python v3.7*\ntox-py38             Run pytest via tox with *python v3.8*\ntox-py39             Run pytest via tox with *python v3.9*\npytest               Run pytest\npytest-ci            Run pytest with CI settings\npublish              Release new version to PyPi\nmakemessages         Make and compile locales message files\n```\n\n# License\n\n[MIT](LICENSE)\n",
    'author': 'Philipp Hagemeister',
    'author_email': 'phihag@phihag.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0.0',
}


setup(**setup_kwargs)
