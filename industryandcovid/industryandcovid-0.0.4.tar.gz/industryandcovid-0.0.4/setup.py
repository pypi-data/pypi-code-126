import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="industryandcovid",
    version="0.0.4",
    author="rinko takei",
    author_email="rtakei@sciencepark.co.jp",
    description="This project will compare amusement park sales with Internet industry sales and the number of people infected with COVID.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ritakei/industryandcovid",
    project_urls={
        "Bug Tracker": "https://github.com/ritakei/industryandcovid",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    py_modules=['industoryandcovid'],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8.5",
    entry_points = {
        'console_scripts': [
            'industryandcovid = industryandcovid:main'
        ]
    },
)
