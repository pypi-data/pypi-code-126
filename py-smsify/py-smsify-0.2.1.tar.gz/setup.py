# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['py_smsify']

package_data = \
{'': ['*']}

install_requires = \
['anyascii>=0.3.1,<0.4.0']

setup_kwargs = {
    'name': 'py-smsify',
    'version': '0.2.1',
    'description': 'Python library for creating GSM-7 compatible SMS messages',
    'long_description': '![](https://i.imgur.com/xuHAE49.png)\n# Python library for creating GSM-7 compatible SMS messages\n\n### Installation\n`pip install py-smsify`\n\n### Standalone Functions\n```python\nfrom py_smsify import SmsMessage\n\n# Encode python string into a GSM-7 python encoded string\nSmsMessage.encode(string: str) -> str\n\n# Encode a unicode string to a bytearray of SMS characters\nSmsMessage.message_encode(string: str) -> bytearray\n```\n\n### Usage\n```python\nfrom py_smsify import SmsMessage\n\n#Encode to a string of valid characters\nmessage = SmsMessage("Cool Message!").encoded_text\n# result: Cool Message!\n\n#Encode to a python bytestring\nmessage = SmsMessage("Cool Message!").encoded_bytes\n# result: b"Cool Message!"\n\n#Encode with non latin languages/characters\nmessage = SmsMessage("酷短信！").encoded_text\n# result: KuDuanXin!\n\n#Encode with emojis\nmessage = SmsMessage("Cool😎 Message✉️").encoded_text\n# result: "Cool:sunglasses: Message:envelope:"\n```\n\n### Message Stats\n```python\nfrom py_smsify import SmsMessage\n\n#Get message length in bytes\nmessage = SmsMessage("Cool Message!").length\n# result: 13 bytes\nmessage = SmsMessage("He\\\\o W{}rld!").length #{} are characters from the extended table and therefore require 2 bytes of space\n# result: 15 bytes\n\n#Get amount of segments the message will be split to\nmessage = SmsMessage("Cool Message!").segments\n# result: 1 message\n\n#You can also have it calculate segment count with twilio message headers in mind\nmessage = SmsMessage("Cool Message!",twilio=True).segments\n# result: 1 message\n\n```',
    'author': 'Simon Wissotsky',
    'author_email': 'Wissotsky@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/SkyDiverCool/py-smsify',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
