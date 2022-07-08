# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src',
 'core': 'src/core',
 'core.loader': 'src/core/loader',
 'testing': 'src/testing'}

packages = \
['api', 'core', 'core.loader', 'testing']

package_data = \
{'': ['*']}

install_requires = \
['localimport>=1.7.6,<2.0.0',
 'networkx>=2.6.0,<3.0.0',
 'setuptools>=33.1.0',
 'typeapi>=0.2.1,<0.3.0']

extras_require = \
{'testing': ['pytest>=6.0.0']}

entry_points = \
{'kraken.core.loader': ['python_script = '
                        'kraken.core.loader.python_script:PythonScriptProjectLoader'],
 'pytest11': ['kraken-testing = kraken.testing']}

setup_kwargs = {
    'name': 'kraken-core',
    'version': '0.2.7',
    'description': '',
    'long_description': '# kraken-core\n\n[![Python application](https://github.com/kraken-build/kraken-core/actions/workflows/python-package.yml/badge.svg)](https://github.com/kraken-build/kraken-core/actions/workflows/python-package.yml)\n[![PyPI version](https://badge.fury.io/py/kraken-core.svg)](https://badge.fury.io/py/kraken-core)\n\nThe `kraken.core` package provides the primitives of describing a build and deriving build tasks.\n\nAside from the `kraken.core` package, this package also provides the `kraken.api` module that is\nused only at runtime by Kraken build scripts and the `kraken.testing` module for Pytest fixtures.\n\n## How does it work?\n\nKraken uses **tasks** to describe units of work that can be chained and establish dependencies between each other.\nEach task has a **schema** that defines its input and output properties. When an output property is linked to the\ninput property of another task, this established as dependency between the tasks.\n\n```py\nfrom kraken.std.docker_gen import generate_dockerfile\nfrom kraken.std.docker_build import build_docker_image\ndockerfile = generate_dockerfile(source_file="Dockerfile.yml")\nbuild_docker_image(dockerfile=dockerfile.path, tags=["example:latest"], load=True)\n```\n\nThis populates the project with two **tasks** and connects the computed output property of one to the other,\nallowing the tasks that will run for `build_docker_image()` to pick up the dynamically generated Dockerfile that\nis written into a location in the build directory by the `generate_dockerfile()` task.\n\n<p align="center"><img src="assets/graph.png" height="225px"></p>\n\n## Core API\n\nKraken **tasks** are described with a schema. Each schema field has a type and may be an input or output parameter.\nOutput parameters are only available once a resource is executed; Kraken will that a proper execution order is\nestablished such that output properties are hydrated before another resource tries to access them as an input.\n\n```py\nfrom kraken.core.task import Context, Task, Property, Output, task_factory\nfrom typing_extensions import Annotated\n\nclass GenerateDockerfileTask(Task):\n    source_file: Property[str]\n    path: Annotated[Property[str], Output]\n\n    def execute(self, ctx: Context) -> None:\n        path = Path(self.path.setdefault(str(ctx.build_directory / "Dockerfile")))\n        path.write_text(render_dockerfile(Path(self.source_file.get()).read_text()))\n\ngenerate_dockerfile = task_factory(GenerateDockerfileTask)\n```\n\n## Integration testing API\n\nThe `kraken.testing` module provides Pytest fixtures for integration testing Kraken extension modules. The\n`kraken_project` fixture provides you with access to a Kraken project object. The `kraken.testing.execute()`\nfunction is a rudimentary implementation to correctly execute a build graph, but it is not recommended for\nproduction use and should be used in tests only.\n\n__Example__\n\n```py\ndef test__helm_push_to_oci_registry(kraken_project: Project, oci_registry: str) -> None:\n    """This integration test publishes a Helm chart to a local registry and checks if after publishing it, the\n    chart can be accessed via the registry."""\n\n    helm_settings(kraken_project).add_auth(oci_registry, USER_NAME, USER_PASS, insecure=True)\n    package = helm_package(chart_directory="data/example-chart")\n    helm_push(chart_tarball=package.chart_tarball, registry=f"oci://{oci_registry}/example")\n    kraken_project.context.execute([":helmPush"])\n    response = httpx.get(f"http://{oci_registry}/v2/example/example-chart/tags/list", auth=(USER_NAME, USER_PASS))\n    response.raise_for_status()\n    tags = response.json()\n    assert tags == {"name": "example/example-chart", "tags": ["0.1.0"]}\n```\n\n> This is a working example from the `kraken-std` package.\n',
    'author': 'Niklas Rosenstein',
    'author_email': 'rosensteinniklas@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
