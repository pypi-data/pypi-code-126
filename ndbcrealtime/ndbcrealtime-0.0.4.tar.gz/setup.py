import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ndbcrealtime", 
    packages=["ndbcrealtime"],
    version="0.0.4",
    license='apache-2.0',
    author="Tim Empringham",
    author_email="tim.empringham@live.ca",
    description="NDBC Real Time Buoy Observation Data Wrapper.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/djtimca/ndbc-api",
    download_url = 'https://github.com/djtimca/ndbc-api/archive/refs/tags/0.0.4.tar.gz',
    keywords = ['NDBC', 'Buoy', 'Waves', 'Wind', 'Weather'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    python_requires='>=3.8',
)