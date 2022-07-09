# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dooit', 'dooit.ui', 'dooit.ui.events', 'dooit.ui.widgets', 'dooit.utils']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'poetry>=1.1.13,<2.0.0',
 'psutil>=5.9.1,<6.0.0',
 'pyperclip>=1.8.2,<2.0.0',
 'textual>=0.1.17,<0.2.0']

entry_points = \
{'console_scripts': ['dooit = dooit.__init__:main']}

setup_kwargs = {
    'name': 'dooit',
    'version': '0.2.1',
    'description': 'A TUI todo manager',
    'long_description': '<img src="https://user-images.githubusercontent.com/97718086/174438959-d8887b62-76de-4587-9619-91a4ecd6e1d6.png" align="right" alt="Todo Icon" width="150" height="150">\n\n# Dooit ✔️\n*A todo manager that you didn\'t ask for, but needed !* \\\nto make sure that you complete your tasks on time ;)\n\n[![GitHub issues](https://img.shields.io/github/issues/kraanzu/dooit?color=red&style=for-the-badge)](https://github.com/kraanzu/doit/issues)\n[![GitHub stars](https://img.shields.io/github/stars/kraanzu/dooit?color=green&style=for-the-badge)](https://github.com/kraanzu/doit/stargazers)\n[![GitHub license](https://img.shields.io/github/license/kraanzu/dooit?color=yellow&style=for-the-badge)](https://github.com/kraanzu/doit/blob/main/LICENSE)\n[![Support Server](https://img.shields.io/discord/989186205025464390.svg?label=Discord&logo=Discord&colorB=7289da&style=for-the-badge)](https://discord.gg/W6Ax4xXy)\n\n# Installation 🔨\n> You can install dooit easily using python one-liner (you must use python version 3.10+)\n\n```bash\npython3 -m pip install git+https://github.com/kraanzu/dooit.git\n```\n> Or the long way?\n```bash\ngit clone https://github.com/kraanzu/dooit.git\ncd dooit\npip3 install .\n```\nAnd then simply type `dooit` in your terminal to launch it.. ezy pzy\n> Note: Config file for `dooit` is located at your $XDG_CONFIG_HOME (or ~/.config/dooit)\n\n> Note: The default icons used in the application are a part of [nerd fonts](https://www.nerdfonts.com/).\\\n        You can change that in the config file.\n\n# Features 🌟\n\n> Some features that dooit comes with:\n\n- An interactive & beautiful UI\n- Configurable icons and themes\n- Both Mouse and Keyboard support (Vim like keybindings)\n- Topicwise seperated Todo Lists (With branching)\n- Editable Todo\'s about, date and urgency\n- Nested todos!\n- Sort options with menu (Name, Date, Urgency, Status)\n- Search & jump-to-todo mode on the fly!\n\n> See Demo Video below in order to get a visual :)\n\n# Demo 🎥\nhttps://user-images.githubusercontent.com/97718086/174479591-5fe4f425-c9f3-4db2-969c-df8aa400e103.mp4\n\n\n# Contribution 🤝\n- Want to contribute? Feel free to open a PR! 😸\n- Got some ideas for improvements? I\'m all ears! 👂\n\n----------------------------\n----------------------------\n\n#### Other TUI projects 🤓 :\nIf you liked dooit then you might wanna try out some of my other TUI projects as well\n- [termtyper](https://github.com/kraanzu/termtyper) - A typing-test app for terminal\n- [gupshup](https://github.com/kraanzu/gupshup) - A localhost TUI chat client\n\n',
    'author': 'kraanzu',
    'author_email': 'kraanzu@gmail.com',
    'maintainer': 'kraanzu',
    'maintainer_email': 'kraanzu@gmail.com',
    'url': 'https://github.com/kraanzu/dooit',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
