from setuptools import setup

readme = open('./README.md', "r")

setup(
    name = 'jefrysaludo',
    packages = ['jefrysaludo'],
    version='0.1',
    description='Esta es la descripcion de mi paquete',
    long_description=readme.read(),
    long_description_content_type = 'text/markdown',
    author='Jefry Zarate',
    author_email='jefryzarate@gmail.com',
    url='https://github.com/Jefry-bot/jefrysaludo',
    download_url='https://github.com/Jefry-bot/jefrysaludo/tarball/0.1',
    keywords=['testing', 'logging', 'example'],
    classifiers=[],
    license="MIT",
    include_package_data=True
)