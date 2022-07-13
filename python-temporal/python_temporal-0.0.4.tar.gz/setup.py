from distutils.core import setup

setup(
    name='python_temporal',
    version='0.0.4',
    author='X.X',
    author_email='xx@example.com',
    url='http://www.example.com/',
    license='LICENSE',
    packages=['src', 'src.config', 'src.interfaces', 'src.types', 'src.utils', ],
    description="The description of the package",
    long_description_content_type="text/markdown",
    long_description="test",
    install_requires=['temporal-python-sdk',
                      'boto3~=1.24.22',
                      'PyYAML',
                      'pandas~=1.4.3',
                      'numpy',
                      'pydantic~=1.9.1'
                      ]
)
