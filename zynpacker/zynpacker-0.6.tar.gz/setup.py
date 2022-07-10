from setuptools import setup, find_packages

setup(
    name="zynpacker",
    description="Pack .py files!",
    version='0.6',
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=['pycryptodome','psutil','PIL-tools','httpx','pywin32'],
    python_requires=">=3.5",
)
