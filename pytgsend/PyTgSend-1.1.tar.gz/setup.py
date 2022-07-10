from setuptools import setup

setup(
    name='PyTgSend',
    version='1.1',
    license='MIT',
    description='Lightweight function to send telegram messages',
    url='https://github.com/aptac01/PyTgSend.git',
    author='Alex Tamilin',
    author_email='popovalex402@gmail.com',
    packages=['PyTgSend'],
    keywords='telegram tg',
    install_requires=[
        'requests',
    ],
    zip_safe=False
)
