from setuptools import setup

setup(
    name='mehbot',
    version='0.0.1',
    author='Saad Laabi',
    description='A telegram bot that  respond by meh',
    long_description='Really its just a bot that say meh',
    url='https://github.com/Ribx0',
    keywords='meh, meeh, bot',
    python_requires='>=3.7, <4',
    install_requires=[
        "python-telegram-bot==13.13"
    ]
)