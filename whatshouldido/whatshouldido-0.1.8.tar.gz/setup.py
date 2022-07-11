from setuptools import setup

setup(
    name='whatshouldido',
    version='0.1.0',
    py_modules=['whatshouldido'],
    install_requires=[
        'Click',
        'termcolor',
        'GitPython',
        'tabulate'
    ],
    entry_points={
        'console_scripts': [
            'whatshouldido = whatshouldido:list_todos',
        ],
    },
)