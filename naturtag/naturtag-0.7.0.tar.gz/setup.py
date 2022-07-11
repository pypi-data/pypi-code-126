# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['naturtag',
 'naturtag.app',
 'naturtag.controllers',
 'naturtag.metadata',
 'naturtag.utils',
 'naturtag.widgets']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=21.2',
 'click-help-colors>=0.9',
 'click>=8.0',
 'pillow>=9.1',
 'pyexiv2>=2.6.2',
 'pyinaturalist-convert>=0.4.1.dev1',
 'pyinaturalist>=0.17.2',
 'pyside6>=6.3.0,<7.0.0',
 'pyyaml>=6.0',
 'qtawesome>=1.1.1,<2.0.0',
 'qtmodern>=0.2,<0.3',
 'sqlalchemy>=1.4.36,<2.0.0']

extras_require = \
{'docs': ['furo>=2022.6.4,<2023.0.0',
          'linkify-it-py>=1.0.1,<2.0.0',
          'myst-parser>=0.17.0,<0.18.0',
          'sphinx>=4.5.0,<5.0.0',
          'sphinx-autodoc-typehints>=1.17,<2.0',
          'sphinx-copybutton>=0.5',
          'sphinx-design>=0.2',
          'sphinxcontrib-apidoc>=0.3,<0.4']}

entry_points = \
{'console_scripts': ['naturtag = naturtag.cli:main',
                     'naturtag-ui = naturtag.app.app:main',
                     'nt = naturtag.cli:main']}

setup_kwargs = {
    'name': 'naturtag',
    'version': '0.7.0',
    'description': 'A CLI tool to add iNaturalist taxonomy metadata to local observation photos',
    'long_description': "# Naturtag\n\n[![Build status](https://github.com/JWCook/naturtag/workflows/Build/badge.svg)](https://github.com/JWCook/naturtag/actions)\n[![Documentation Status](https://readthedocs.org/projects/naturtag/badge/?version=latest)](https://naturtag.readthedocs.io)\n[![GitHub issues](https://img.shields.io/github/issues/JWCook/naturtag)](https://github.com/JWCook/naturtag/issues)\n[![PyPI](https://img.shields.io/pypi/v/naturtag?color=blue)](https://pypi.org/project/naturtag)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/naturtag)](https://pypi.org/project/naturtag)\n\n\n<!-- RTD-IGNORE -->\n<br />\n\n[![](assets/icons/naturtag-gh-preview.png)](https://naturtag.readthedocs.io)\n\n## Contents\n- [Summary](#summary)\n- [Use Cases](#use-cases)\n- [Installation](#installation)\n- [Usage](#usage)\n  - [GUI](#gui)\n  - [CLI](#cli)\n  - [Library](#library)\n- [Development Status](#development-status)\n<!-- END-RTD-IGNORE -->\n\n## Summary\nNaturtag is a tool for tagging image files with iNaturalist taxonomy & observation metadata.\nThis includes a basic **command-line interface**, a work-in-progress **desktop application**,\nand can also be used as a **python library**.\n\n## Use Cases\nNaturtag takes useful information from your own iNaturalist observations and embeds it in your local\nphoto collection, mainly using [XMP](https://en.wikipedia.org/wiki/Extensible_Metadata_Platform) and\n[EXIF](https://en.wikipedia.org/wiki/Exif) metadata. This has a variety of uses, including:\n\n### Local photo organization\nIf you like the way you can search and filter your observations on iNaturalist.org and its mobile\napps, and you wish you could do that with your local photos, naturtag can help.\nIt can tag your photos with **hierarchical keywords**, which can then be used in a photo viewer or\nDAM such as [**Lightroom**](https://millennialdiyer.com/articles/photography/lightroom-keyword-hierarchy/), [**FastPictureViewer**](https://www.fastpictureviewer.com), or\n[**XnViewMP**](https://www.xnview.com/en/xnviewmp).\n\nThis essentially gives you a phylogenetic tree for browsing and filtering your photos.\nExample in XnView:\n\n![screenshot](assets/screenshots/xnview.png)\n\n### Photo hosting\nNaturtag can also simplify tagging photos for photo hosting sites like Flickr. For that use case, this\ntool generates structured keywords in the same format as\n[iNaturalist's Flickr Tagger](https://www.inaturalist.org/taxa/flickr_tagger).\n\nExample search using these tags: https://www.flickr.com/photos/tags/taxonomy:class=arachnida\n\nExample of taxonomy tags on a Flickr photo page:\n\n![screenshot](assets/screenshots/flickr.png)\n\n\n### Other biodiversity tools\nFinally, naturtag can improve interoperability with other tools and systems that interact with biodiversity\ndata. For example, in addition to iNaturalist you might submit some observations to another\nplatform with a more specific focus, such as **eBird**, **BugGuide**, or **Mushroom Observer**.\nFor that use case, this tool supports [Simple Darwin Core](https://dwc.tdwg.org/simple).\n\n## Installation\nSee [GitHub Releases](https://github.com/pyinat/naturtag/releases) for downloads and\n[Installation](https://naturtag.readthedocs.io/en/latest/installation.html)\nfor platform-specific instructions.\n\nTo just install naturtag as a python package, run:\n```bash\npip install naturtag\n```\n\n## Usage\n\n### GUI\nThe main interface for this project is still a work in progress.\n\nIt includes an interface for selecting and tagging images:\n\n![Screenshot](assets/screenshots/image-selector.png)\n\nAnd tools to search and browse species to tag your images with:\n\n![Screenshot](assets/screenshots/taxon-search.png)\n\nSee [Application Guide](https://naturtag.readthedocs.io/en/latest/app.html) for more details.\n\n### CLI\nNaturtag also includes a command-line interface. It takes an observation or species, plus some image\nfiles, and generates EXIF and XMP metadata to write to those images. You can see it in action here:\n[![asciicast](https://asciinema.org/a/0a6gzpt7AI9QpGoq0OGMDOxqi.svg)](https://asciinema.org/a/0a6gzpt7AI9QpGoq0OGMDOxqi)\n\nSee [CLI documentation](https://naturtag.readthedocs.io/en/latest/cli.html) for more details.\n\n### Library\nYou can also import `naturtag` as a python library, and use its main features in your own scripts or\napplications. Basic example:\n```python\nfrom naturtag import tag_images, refresh_tags\n\n# Tag images with full observation metadata\ntag_images(['img1.jpg', 'img2.jpg'], observation_id=1234)\n\n# Refresh previously tagged images with latest observation and taxonomy metadata\nrefresh_tags(['~/observations/'], recursive=True)\n```\n\nSee [API Reference](https://naturtag.readthedocs.io/en/latest/reference.html) for more details.\n\n\n## Development Status\n* See [Issues](https://github.com/JWCook/naturtag/issues?q=) for planned features and current progress.\n* If you have any suggestions, questions, or requests, please\n  [create an issue](https://github.com/JWCook/naturtag/issues/new/choose), or ping me (**@jcook**)\n  on the [iNaturalist Community Forum](https://forum.inaturalist.org/c/general/14).\n* When I'm not working on this, I'm usually working on other libraries that naturtag benefits from, including\n  [requests-cache](https://requests-cache.readthedocs.io),\n  [pyinaturalist](https://pyinaturalist.readthedocs.io), and\n  [pyinaturalist-convert](https://github.com/JWCook/pyinaturalist-convert).\n",
    'author': 'Jordan Cook',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/JWCook/naturtag',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
