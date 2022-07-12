import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name='mullaney_testpkg_a',
    version='0.0.1',
    author='Will Mullaney',
    author_email='will.mullaney@gmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/mullaneywt/mullaney-testpkg-a',
    project_urls = {
        "Bug Tracker": "https://github.com/mullaneywt/mullaney-testpkg-a/issues"
    },
    license='MIT',
    packages=['mullaney_testpkg_a'],
    install_requires=['netaddr'],
)