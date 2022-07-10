import setuptools
with open(r'D:\Python\Pypi-uploader\Py-Simple-DB\README.md', 'r', encoding='utf-8') as fh:
	long_description = fh.read()

setuptools.setup(
	name='PySimpleDB',
	version='0.2.0',
	author='Super_Zombi',
	author_email='super.zombi.yt@gmail.com',
	description='Simple json database',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/SuperZombi/Py-Simple-DB',
	packages=['Py-Simple-DB'],
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
)