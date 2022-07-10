from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

# with open('HISTORY.md') as history_file:
#     HISTORY = history_file.read()

setup_args = dict(
    name='AncientLibrary',
    version='0.0.1',
    description='Complete Data Science Package from Scratch',
    long_description_content_type="text/markdown",
    long_description=README, # + '\n\n' + HISTORY,
    packages=find_packages(),
    author='Ryan Holmes',
    author_email='holmesforlan@gmail.com',
    url='https://github.com/cranialplating/AncientLibrary',
)

install_requires = []
# do not think any install requirements needed

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)