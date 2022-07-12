import setuptools

setuptools.setup(
    name="GreenMatterAI",
    version="0.0.1",
    author="GreenMatterAI",
    description="GreenMatterAI's package",
    packages=["GreenMatterAI"],
    install_requires=[
        "requests",
        "aws_requests_auth",
        "boto3"
    ]
)
