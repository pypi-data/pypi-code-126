import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="heat_stroke",
    version="0.0.4",
    author="masaki yamamoto",
    author_email="yamamoto.ma25@gmail.com",
    description="a package for predicting the number of heat stroke patients ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/myamamoto325/heat_stroke",
    project_urls={
        "Bug Tracker": "https://github.com/myamamoto325/heat_stroke",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    py_modules=['heat_stroke'],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    entry_points = {
        'console_scripts': [
            'heat_stroke = heat_stroke:main'
        ]
    },
)
