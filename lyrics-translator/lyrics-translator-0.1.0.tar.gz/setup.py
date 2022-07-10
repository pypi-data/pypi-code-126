# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lyrics_translator']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'lyricsgenius>=3.0.1,<4.0.0',
 'python-docx>=0.8.11,<0.9.0',
 'python-dotenv>=0.20.0,<0.21.0',
 'sacremoses>=0.0.53,<0.0.54',
 'sentencepiece>=0.1.96,<0.2.0',
 'transformers[torch]>=4.20.1,<5.0.0']

entry_points = \
{'console_scripts': ['lyrics-translator = lyrics_translator.console:main']}

setup_kwargs = {
    'name': 'lyrics-translator',
    'version': '0.1.0',
    'description': 'Automated lyrics translation',
    'long_description': '# Lyrics Translator\n\nThe `Lyrics Translator` downloads lyrics from genius and uses hugging face to translate the English lyrics into a target language.\n\nTo use the `Lyrics Translator` you will have to create an API Key from `genius` and add it to a `env` file:\n\nhttps://docs.genius.com/#/getting-started-h1\n',
    'author': 'Mauro Luzzatto',
    'author_email': 'mauroluzzatto@hotmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/MauroLuzzatto/lyrics-translator',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
