from setuptools import find_packages, setup

setup(
    name="fiopyhelper",
    version="0.0.1",
    description="FrameIO Python Client",
    packages=find_packages(),
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "testfixtures", "responses"],
    install_requires=[
        "requests==2.27.1",
        "jmespath==1.0.0",
        "pyyaml==6.0",
        "python-magic==0.4.25",
        "deepmerge==1.0.1",
    ],
    include_package_data=True,
)
