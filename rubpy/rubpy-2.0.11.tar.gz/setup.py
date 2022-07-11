from setuptools import setup, find_packages

text : str = '''# rubpy
The official rubpy repository, unofficial and high-speed library for rubika...
# how to install library
Enter the following command to install the library in your terminal
```
pip install rubpy
```
# Web Socket Example
```
from rubpy.socket import Client
import asyncio

socket = Client('YOUR-AUTH')
seened : list = []


async def main():
	while 1:
		async for chats in socket.handler():
			try:
				for chat in chats:
					if chat['object_guid'].startswith('g'):
						if not chat['object_guid'] + chat['chat']['last_message']['message_id'] in seened:
							text : str = chat['chat']['last_message']['text']
							print(text)
							seened.append(chat['object_guid'] + chat['chat']['last_message']['message_id'])
			except :
					...
```

This source code receives and prints the latest messages using the Rubica web socket

# روبی
مخزن رسمی روبی، کتابخانه غیر رسمی و پرسرعت روبیکا...

# مثال وب سوکت
```
from rubpy.socket import Client
import asyncio

socket = Client('YOUR-AUTH')
seened : list = []


async def main():
	while 1:
		async for chats in socket.handler():
			try:
				for chat in chats:
					if chat['object_guid'].startswith('g'):
						if not chat['object_guid'] + chat['chat']['last_message']['message_id'] in seened:
							text : str = chat['chat']['last_message']['text']
							print(text)
							seened.append(chat['object_guid'] + chat['chat']['last_message']['message_id'])
			except :
					...
```

این سورس کد با استفاده از وب سوکت روبیکا آخرین پیام ها را دریافت میکند و چاپ میکند


# چگونگی نصب کتابخانه
دستور زیر را در ترمینال خود برای نصب کتابخانه وارد کنید

```
pip install rubpy
```
'''

requirements : list = ["pycryptodome" , "pillow" , "aiohttp" , "websocket-client"]

setup(
    name = "rubpy",
    version = "2.0.11",
    author = "Shayan Heidari",
    author_email = "snipe4kill.tg@gmail.com",
    description = "This is an unofficial library for deploying robots on Rubika accounts.",
    long_description = str(text),
    long_description_content_type = "text/markdown",
    url = "https://github.com/snipe4kill/rubpy/",
    packages = find_packages(),
    install_requires = requirements,
    classifiers = [
    	"Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
    ],
)