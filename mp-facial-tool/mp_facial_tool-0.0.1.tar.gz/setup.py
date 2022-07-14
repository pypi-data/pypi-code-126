import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mp_facial_tool",
    version="0.0.1",
    author="VERMAN",
    author_email="justverman@gmail.com",
    description="some facial functions based mediapipe",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VERMANs/mp_utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
