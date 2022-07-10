# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['kisskh_downloader']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'm3u8>=2.0.0,<3.0.0',
 'playwright>=1.23.0,<2.0.0',
 'requests>=2.28.1,<3.0.0',
 'tqdm>=4.64.0,<5.0.0',
 'validators>=0.20.0,<0.21.0']

entry_points = \
{'console_scripts': ['kisskh = kisskh_downloader.cli:kisskh']}

setup_kwargs = {
    'name': 'kisskh-downloader',
    'version': '0.1.0',
    'description': 'Simple downloaded for https://kisskh.me/',
    'long_description': '# kisskh-dl\n\nSimple downloaded for https://kisskh.me/\n\n---\n\n## Installation\n```console\npip install kisskh-downloader\n```\n\n---\n\n## Usage\n\n> **NOTE:** As of now the video files downloaded are in [.ts](https://en.wikipedia.org/wiki/MPEG_transport_stream) format. You can still use players like [VLC](https://www.videolan.org/) to play the video.\n\n### Direct download entire series in highest quality available\n\n```console\nkisskh dl "https://kisskh.me/Drama/Money-Heist--Korea---Joint-Economic-Area?id=5044"\n```\n\n### Search and download entire series in highest quality available\n\n```console\nkisskh dl "Stranger Things"\n1. Stranger Things - Season 4\n2. Stranger Things - Season 1\n3. Stranger Things - Season 2\n4. Stranger Things - Season 3\nPlease select one from above: 1\n```\n\n### Download specific episodes with specific quality\n\nDownloads episode 4 to 8 of `Alchemy of Souls` in 720p:\n```console\nkisskh dl "https://kisskh.me/Drama/Alchemy-of-Souls?id=5043" -e 4:8 -q 720p\n```\n\nDownloads episode 3 of `A Business Proposal` in 720p:\n```console\nkisskh dl "https://kisskh.me/Drama/A-Business-Proposal?id=4608" -e 3 -q 720p\n```\n\n---\n\n# TODO\n- [ ] Add ability to export video in other format using ffmpeg\n- [ ] Add unit test\n- [ ] Handle Ctrl + C signal in terminal\n- [ ] Throw appropriate exception or handles it somehow\n    - [ ] In valid URL pass\n    - [ ] Video file not present\n- [ ] Add option to download subtitles\n',
    'author': 'Debakar Roy',
    'author_email': 'allinonedibakar@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
