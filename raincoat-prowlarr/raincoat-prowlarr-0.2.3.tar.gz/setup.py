# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['raincoat_prowlarr']

package_data = \
{'': ['*']}

install_requires = \
['colorama>=0.4.3,<0.5.0',
 'deluge-client>=1.8.0,<2.0.0',
 'getmovieinfo>=0.1.5,<0.2.0',
 'justlog>=0.1.1.5,<0.2.0.0',
 'python-qbittorrent>=0.4.2,<0.5.0',
 'requests>=2.23.0,<3.0.0',
 'tabulate>=0.8.7,<0.9.0',
 'transmission-clutch>=6.0.2,<7.0.0']

entry_points = \
{'console_scripts': ['raincoat = raincoat_prowlarr.raincoat_prowlarr:main']}

setup_kwargs = {
    'name': 'raincoat-prowlarr',
    'version': '0.2.3',
    'description': 'Raincoat-prowlarr is a tool to search torrents using jackett and search torrents and nzb files using prowlarr/jackett/MovieInfo and send them to your client.',
    'long_description': '# Raincoat\n\nRaincoat_prowlarr is a CLI tool to search torrents using [Jackett](https://github.com/Jackett/Jackett)\'s indexers or [Prowlarr](https://github.com/Prowlarr/Prowlarrand) and send them directly to your client. Prowlarr supports NZB indexer.\n\n### Installation\n\n`pip install raincoat-prowlarr\n\n### Requirements\n\n- Python 3.6+\n- Jackett and configured indexers\n- Or Prowlarr and configure indexers\n- qBittorrent, Transmission or Deluge (or use local download option)\n- nzbget, downloader for nzb files\n- libtorrent if you use local downloader and magnet links.\n  - Arch: `pacman -S libtorrent-rasterbar`\n  - Ubuntu: `apt-get install python-libtorrent -y`\n  - Fedora: `dnf install rb_libtorrent-python2`\n\n### Usage\n\n`raincoat_prowlarr "Terms to search"`\n\n#### Parameters\n\n- --indexer_manager\n  - specify the indexer manager to search; prowlarr or jackett\n- --jackett_ key\n  - Specify a Jackett API key\n- --prowlarr_ key\n  - Specify a Prowlarr API key\n- -l, --length\n  - Max number of characters displayed in the "Description" column.\n- -L, --limit\n  - Limits the number of results displayed.\n- -c, --config\n  - Specifies a different config path.\n- -s, --sort\n  - Change the sorting criteria. Valid choices are: \'cn\',\'protocol\',\'seeders\', \'leechers\', \'ratio\', \'size\' and \'description\'. Default/not specified is \'cn/size\'. cn is chinese subtitle.  protocol is usenet/torrent, if not specified, torrent has high priority or vice versa.\n- --jackett_indexer\n  - Change the indexer for Jackett used for your search, in cases where you want to only search one site. Default is "all".\n- --prowlarr_indexer\n  - Change the indexer for prowlarr used for your search, in cases where you want to only search one site. Default is "". "" for all; -1 for all usenet; -2 for all torrents. look at https://wiki.servarr.com/prowlarr/search\n- -d, --download x\n  - Grab the first x resultd and send to the client immediately. Defaults to 1.\n- -K, --insecure\n  - Don\'t verify certificates  \n- --local\n  - Force use of "local" file download.\n- --list\n  - Specify a file to load search terms from. One term per line.\n- --verbose\n  - Extra verbose logging sent to log file.\n\n#### Configuration file\n\nUpon installation, a config file is created in your home directory. Before you can use Raincoat, you will need to modify it.\n\n```json\n{\n    "indexer_manager": "prowlarr",\n\t"jackett_apikey": "",\n\t"jackett_url": "http://your_base_jackett_url:port",\n\t"jackett_indexer": "all",\n\t"prowlarr_apikey": "",\n\t"prowlarr_url": "http://you_base_prowlarr_url:port",\n    "prowlarr_indexer": "",\n\t"description_length": 100,\n\t"exclude": "words to exclude",\n\t"results_limit": 20,\n\t"client_url": "http://your_torrent_client_api",\n\t"display": "grid",\n\t"torrent_client": "qbittorrent",\n\t"torrent_client_username": "admin",\n\t"torrent_client_password": "admin",\n\t"download_dir": "/some/directory/",\n\t"nzbget_url": "http://your_nzb_server_url",\n    "nzbget_username**: "***",\n    "nzbget_password**: "***",\n    "nzbget_port": 6789\n\n}\n```\n- indexer_manager (string)\n  - indexer manager to search. jackett or prowlarr\n- jackett_apikey (string)\n  - The api key provided by Jackett, found on the dashboard.\n- jackett_url (string)\n  - The base url for your jackett instance. (default: http://127.0.0.1:9117)\n- jackett_indexer (string)\n  - The jackett indexer you wish to use for searches.\n- prowlarr_apikey (string)\n  - The api key provided by Prowlarr, found on the dashboard.\n- prowlarr_url (string)\n  - The base url for your prowlarr instance. (default: not sure)\n- prowlarr_indexer (string)\n  - The prowlarr indexer you wish to use for searches.\n- description_length (int)\n  - The default description length\n- exclude (string)\n  - Words to exclude from your results seperated by a space.\n- results_limit (int)\n  - Max number of lines to show.\n- client_url (string)\n  - The url to your torrent client\'s API\n- display (string)\n  - The display style of the results table. You can view available choices [here](https://pypi.org/project/tabulate/)\n- torrent_client (string)\n  - Your torrent client. Valid options are: local, qbittorrent, transmission and deluge.\n- torrent_client_username (string)\n  - Your torrent client\'s login username.\n- torrent_client_password\n  - Your torrent client\'s login password. Note: Only Transmission accepts empty passwords.\n- download_dir\n  - Where to save the torrent files when using "local" downloader.\n- nzbget_url (string)\n  - url for nzbget server\n- nzbget_username (string)\n  - nzbget username\n- nzbget_password (string)\n  - nzbget pasword\n- nzbget_port (int)\n  - nzbget port\n\n\n# Built with\n\n- requests\n- justlog\n- colorama\n- tabulate\n- transmission-clutch\n- deluge-client\n- python-qbittorrent\n\nAll available on Pypi.\n\n# License\n\nThis project is licensed under the MIT License\n',
    'author': 'crvideoVR',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/crvideo/raincoat_prowlarr',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
