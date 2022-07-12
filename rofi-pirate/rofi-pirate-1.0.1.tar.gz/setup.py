# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rofi_pirate']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.11.1,<5.0.0',
 'python-dateutil>=2.8.2,<3.0.0',
 'requests>=2.28.1,<3.0.0']

entry_points = \
{'console_scripts': ['rofi-pirate = rofi_pirate.cli:cli']}

setup_kwargs = {
    'name': 'rofi-pirate',
    'version': '1.0.1',
    'description': 'Rofi module for searching torrents using Jackett API.',
    'long_description': '# 🏴\u200d☠ Rofi Pirate\n\n![](./assets/logo.png)\n\nRofi module for searching torrents using Jackett API. You can also instantly play media files without having to leave the Rofi menu. The project is still in beta.\n\n## Requirements\n\n1. Streaming torrent client: [Peerflix](https://github.com/mafintosh/peerflix) (to play media files without downloading it first)\n2. qBittorent (optional)\n3. Nerd Fonts\n\n## Setup process\n\n1. First, you need a running instance of Jackett and install Peerflix\n\n```shell\n# Arch Linux users\nyay -S jackett-bin\nsystemctl start jackett.service # then go to http://localhost:9117/\n# Or Docker image\ndocker pull linuxserver/jackett\n# Peerflix install\nnpm install -g peerflix\n```\n\n2. Set up your indexers through the dashboard and also obtain an API key from there.\n\n3. Install rofi-python package.\n\n```shell\npip install rofi-pirate\n```\n\n4. Place the configuration file under ```~/.config/rofi_pirate/config.json```. **Don\'t forget** to specify your API key.\n\nConfig example:\n\n```json\n{\n  "JACKETT_ENDPOINT": "http://127.0.0.1:9117",\n  "JACKETT_APIKEY": "<API_KEY>", \n  "SEARCH_LIMIT": 25,\n  "PEERFLIX_CMD": "peerflix -t -k -a",\n  "PEERFLIX_CACHE": "~/Downloads/Torrents",\n  "HISTORY_CACHE": "~/.config/rofi_pirate/history.db",\n}\n```\n\n## TODO\n\n- [ ] Dynamic indexer configuration.\n- [ ] Ability to preview torrent images (movie/music covers).',
    'author': 'Pierre Linn',
    'author_email': 'haarnel@proton.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/haarnel/rofi-pirate',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
