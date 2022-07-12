import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="neurosec",
    version="0.0.1",
    author="stdp",
    author_email="info@stdp.io",
    description="A camera class based of the popular VidGear video processing library. Neurosec seemlessly allows you to process inference using the Akida neuromorphic processor.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Apache License 2.0",
    url="https://stdp.io",
    keywords=[
        "stdp",
        "stdp.io",
        "neuromorphic",
        "akida",
        "brainchip",
        "camgear",
        "streaming",
    ],
    project_urls={
        "Bug Tracker": "https://github.com/stdp/neurosec/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=[
        "cv2",
        "PIL",
        "numpy",
        "akida",
        "akida_models",
        "vidgear",
    ],
)
