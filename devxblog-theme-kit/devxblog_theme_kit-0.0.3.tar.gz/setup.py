from setuptools import setup, find_packages

setup(
    name='devxblog_theme_kit',
    version='0.0.3',
    install_requires=[
        'click==8.1.3',
        'django==4.0.2',
        'rich==12.4.4',
        'requests==2.27.1',
        'pyyaml==6',
        'twine==4.0.1',
        'bump2version==1.0.1'
    ],
    packages=find_packages('.'),
    entry_points={
        'console_scripts': [
            'devxblog-theme-kit = devxblog_theme_kit.cli:main'
        ]
    }
)
