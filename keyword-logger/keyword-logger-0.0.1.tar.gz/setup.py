import json
import os

from setuptools import setup

pkg_filepath = os.path.join(os.path.dirname(__file__), "pkg.json")
with open(pkg_filepath, mode="r", encoding="utf-8") as f:
    values = json.load(f)

setup(
    name=values["package_name"],
    version=values["version"],
    packages=[values["module_name"]],
    package_dir={
        values["module_name"]: "src"
    },
    include_package_data=True,
    author="Ivo Simonsmeier",
    author_email="simonsmeier@dive-solutions.de",
    description="This is a dependency confusion placeholder.",
    url="http://dive-solutions.de",
    project_urls={
        "App": "https://app.dive-solutions.de",
    },
)
