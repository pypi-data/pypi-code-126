import setuptools

setuptools.setup(
    name="xwtgzs-lz",
    version="1.1",
    author="刘贞、小於菟工作室",
    author_email="LZ.XWT@outlook.com",
    description="小於菟工作室开发的包。",
    maintainer='lzxwt',
    maintainer_email='lz.xwt@outlook.com',
    install_requires=['qrcode'],
    long_description=open('G:\lz_xwt\README.md', encoding='utf-8').read(),
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    python_requires='>=3.0',
    package_dir={'': 'xwtgzs-lz'}

)
