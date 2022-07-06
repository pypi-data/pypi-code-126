# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_ark_record', 'nonebot_ark_record.ark']

package_data = \
{'': ['*'],
 'nonebot_ark_record': ['res_file/record_image/*',
                        'resource/*',
                        'resource/profile/*',
                        'resource/ttf/*']}

install_requires = \
['Pillow', 'apsyncio', 'matplotlib', 'requests']

setup_kwargs = {
    'name': 'nonebot-ark-record',
    'version': '1.0',
    'description': 'Nonebot plugin for fetching and analyzing gacha records of arknights',
    'long_description': '📦 setup.py (for humans)\n=======================\n\nThis repo exists to provide [an example setup.py] file, that can be used\nto bootstrap your next Python project. It includes some advanced\npatterns and best practices for `setup.py`, as well as some\ncommented–out nice–to–haves.\n\nFor example, this `setup.py` provides a `$ python setup.py upload`\ncommand, which creates a *universal wheel* (and *sdist*) and uploads\nyour package to [PyPi] using [Twine], without the need for an annoying\n`setup.cfg` file. It also creates/uploads a new git tag, automatically.\n\nIn short, `setup.py` files can be daunting to approach, when first\nstarting out — even Guido has been heard saying, "everyone cargo cults\nthems". It\'s true — so, I want this repo to be the best place to\ncopy–paste from :)\n\n[Check out the example!][an example setup.py]\n\nInstallation\n-----\n\n```bash\ncd your_project\n\n# Download the setup.py file:\n#  download with wget\nwget https://raw.githubusercontent.com/navdeep-G/setup.py/master/setup.py -O setup.py\n\n#  download with curl\ncurl -O https://raw.githubusercontent.com/navdeep-G/setup.py/master/setup.py\n```\n\nTo Do\n-----\n\n-   Tests via `$ setup.py test` (if it\'s concise).\n\nPull requests are encouraged!\n\nMore Resources\n--------------\n\n-   [What is setup.py?] on Stack Overflow\n-   [Official Python Packaging User Guide](https://packaging.python.org)\n-   [The Hitchhiker\'s Guide to Packaging]\n-   [Cookiecutter template for a Python package]\n\nLicense\n-------\n\nThis is free and unencumbered software released into the public domain.\n\nAnyone is free to copy, modify, publish, use, compile, sell, or\ndistribute this software, either in source code form or as a compiled\nbinary, for any purpose, commercial or non-commercial, and by any means.\n\n  [an example setup.py]: https://github.com/navdeep-G/setup.py/blob/master/setup.py\n  [PyPi]: https://docs.python.org/3/distutils/packageindex.html\n  [Twine]: https://pypi.python.org/pypi/twine\n  [image]: https://farm1.staticflickr.com/628/33173824932_58add34581_k_d.jpg\n  [What is setup.py?]: https://stackoverflow.com/questions/1471994/what-is-setup-py\n  [The Hitchhiker\'s Guide to Packaging]: https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/creation.html\n  [Cookiecutter template for a Python package]: https://github.com/audreyr/cookiecutter-pypackage\n',
    'author': 'Kawataku',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/zheuziihau',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
