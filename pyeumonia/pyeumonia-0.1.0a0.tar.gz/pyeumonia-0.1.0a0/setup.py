from setuptools import setup, find_packages

setup(
    name='pyeumonia',
    version='0.1.0-alpha',
    description='Python Covid-19 data, you can get the latest data from China and the World.',
    author='Senge-Studio',
    author_email='a1356872768@gmail.com',
    install_requires=['requests', 'beautifulsoup4'],
    python_requires='>=3.6',
    # 添加description为Markdown格式
    # long_description=open('README.md', 'r', encoding='utf-8').read(),
    # long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    license='GPLv3',
)
