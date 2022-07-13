# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['slidge',
 'slidge.legacy',
 'slidge.plugins',
 'slidge.plugins.signal',
 'slidge.plugins.telegram',
 'slidge.xep_0055',
 'slidge.xep_0077',
 'slidge.xep_0100',
 'slidge.xep_0115',
 'slidge.xep_0333',
 'slidge.xep_0356',
 'slidge.xep_0363']

package_data = \
{'': ['*']}

install_requires = \
['ConfigArgParse>=1.5.3,<2.0.0',
 'Pillow>=8.1.0',
 'aiohttp>=3.8.1',
 'qrcode>=7.3',
 'slixmpp>=1.8.2,<2.0.0']

extras_require = \
{'discord': ['nextcord>=2.0.0-alpha.10,<3.0.0'],
 'facebook': ['mautrix-facebook>=0.4.0,<0.5.0'],
 'mattermost': ['mattermostdriver>=7.3.2,<8.0.0'],
 'signal': ['aiosignald>=0.2,<0.3'],
 'telegram': ['aiotdlib>=0.19.2,<0.20.0', 'pydantic']}

entry_points = \
{'console_scripts': ['slidge = slidge.__main__:main']}

setup_kwargs = {
    'name': 'slidge',
    'version': '0.1.0a0',
    'description': 'XMPP bridging framework',
    'long_description': "Slidge 🛷\n========\n\n[![Documentation status](https://readthedocs.org/projects/slidge/badge/?version=latest)](https://slidge.readthedocs.io/)\n[![builds.sr.ht status](https://builds.sr.ht/~nicoco/slidge/commits/master/.build.yml.svg)](https://builds.sr.ht/~nicoco/slidge/commits/master/.build.yml?)\n\nPythonic XMPP gateways.\n\nAn XMPP component that provides a generic way to write XMPP ⟷ **legacy network**\ngateways, based on [SliXMPP](https://slixmpp.readthedocs.io).\n\nHomepage: [sourcehut](https://sr.hr/~nicoco/slidge)\n\nChat room:\n[slidge\\@conference.nicoco.fr](xmpp:slidge@conference.nicoco.fr?join)\n\nIssue tracker: https://todo.sr.ht/~nicoco/slidge\n\nStatus\n------\n\nSlidge is not ready for production yet! Right now, only direct messages\nare implemented, for Telegram, Signal and Facebook messenger. Please\ntest it locally and report bugs.\n\nInstallation\n------------\n\nThe easiest way to try out slidge is with docker-compose. Clone the\nrepo, run `docker-compose up` and you should have:\n\n-   an XMPP server (prosody) exposed on port 5222 with a registered user\n    <test@localhost> (password: password)\n-   3 gateway components (a dummy network, signal and telegram)\n-   hot reloading of gateways on code change\n-   signald running in a container (required for signal)\n\nI recommend using gajim to test it. You can launch it with the -p option\nto use a clean profile and not mess up your normal user settings and\nsuch.\n\nIt is definitely possible to set up everything without docker, but note\nthat the aiotdlib package needs to be manually built (wheels from pypi\nare incomplete unfortunately).\n\nAbout privacy\n-------------\n\nSlidge (and most if not all XMPP gateway that I know of) will break\nend-to-end encryption, or more precisely one of the \\'ends\\' become the\ngateway itself. If privacy is a major concern for you, my advice would\nbe to:\n\n-   use XMPP + OMEMO\n-   self-host your gateways\n-   have your gateways hosted by someone you know AFK\n\nRelated projects\n----------------\n\n-   [Spectrum](https://www.spectrum.im/)\n-   [Bitfrost](https://github.com/matrix-org/matrix-bifrost)\n-   [Mautrix](https://github.com/mautrix)\n-   [matterbridge](https://github.com/42wim/matterbridge)\n-   [XMPP-discord-bridge](https://git.polynom.me/PapaTutuWawa/xmpp-discord-bridge)\n\n",
    'author': 'Nicolas Cedilnik',
    'author_email': 'nicoco@nicoco.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
