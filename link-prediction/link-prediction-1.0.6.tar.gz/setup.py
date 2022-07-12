from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="link-prediction",
    version="1.0.6",
    description="Predict links between screens of smartphone applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Christoph A. Johns",
    author_email="christoph.johns@aalto.fi",
    packages=find_packages(exclude=["**/*.joblib", "**/*.npy"]),
    scripts=["bin/predict.py"],
    entry_points={
        "console_scripts": [
            "predict-link = main:predict",
        ]
    },
    package_data={"link-prediction": ["models/*.joblib"]},
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "scipy",
        "tqdm",
        "imbalanced-learn",
        "sentence-transformers",
        "torch",
        "click",
        "joblib",
        "requests",
    ],
)
