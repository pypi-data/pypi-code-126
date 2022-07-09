# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['std', 'std.cargo', 'std.docker', 'std.generic', 'std.helm']

package_data = \
{'': ['*'], 'std.cargo': ['data/certs/*']}

install_requires = \
['httpx>=0.23.0,<0.24.0',
 'kraken-core>=0.2.9,<0.3.0',
 'proxy.py>=2.4.3,<3.0.0',
 'tomli-w>=1.0.0,<2.0.0',
 'tomli>=2.0.1,<3.0.0']

setup_kwargs = {
    'name': 'kraken-std',
    'version': '0.1.6',
    'description': 'The Kraken standard library.',
    'long_description': '# kraken-std\n\n[![Python application](https://github.com/kraken-build/kraken-std/actions/workflows/python-package.yml/badge.svg)](https://github.com/kraken-build/kraken-std/actions/workflows/python-package.yml)\n[![PyPI version](https://badge.fury.io/py/kraken-std.svg)](https://badge.fury.io/py/kraken-std)\n\nThe Kraken standard library.\n\n__Features__\n\n* [Cargo](#cargo)\n* [Docker](#docker)\n* [Helm](#helm)\n\n---\n\n## Cargo\n\n  [Rust]: https://www.rust-lang.org/\n  [Cargo]: https://doc.rust-lang.org/cargo/\n  [rust-lang/cargo#10592]: https://github.com/rust-lang/cargo/pull/10592\n\nBuild [Rust][] projects with [Cargo][].\n\n__Features__\n\n* Inject HTTP(S) Basic-auth credentials into Git clone and Cargo download requests in `cargo build` for\n  compatibility with private registries (workaround until [rust-lang/cargo#10592][] is working and merged).\n\n__Quickstart__\n\n```py\n# kraken.build.py\nfrom kraken.std.cargo import cargo_build, cargo_publish, cargo_settings\n\nsettings = cargo_settings()\nsettings.add_auth("example.jfrog.io", "me@example.org", "<API_TOKEN>")\nsettings.add_registry(\n    "private-repo",\n    "https://example.jfrog.io/artifactory/git/default-cargo-local.git",\n    publish_token="Bearer ${PASSWORD}",\n)\n\ncargo_build()\ncargo_publish(registry="private-repo")\n```\n\n> __Note__\n>\n> * The registry URL configured in the Kraken build script is currently written only temporarily into the\n>   `.cargo/config.toml` configuration file. In a future version, we may permanently write it into the file to keep\n>   it synchronized or instead pick up the configured registries by reading the configuration file instead.\n\n__Integration tests__\n\nThe `cargo_publish()` and `cargo_build()` tasks are continuously integration tested against JFrog Artifactory\nand Cloudsmith.\n\n---\n\n## Docker\n\n  [Kaniko]: https://github.com/GoogleContainerTools/kaniko\n  [Buildx]: https://docs.docker.com/buildx/working-with-buildx/\n\nBuild and publish Docker images.\n\n__Supported backends__\n\n* [ ] Native Docker\n* [x] [Buildx][] (missing auth)\n* [x] [Kaniko][]\n\n__Quickstart__\n\n```py\n# kraken.build.py\nfrom kraken.std.docker import build_docker_image\n\nbuild_docker_image(\n    name="buildDocker",\n    dockerfile="docker/release.Dockerfile",\n    tags=["kraken-example"],\n    load=True,\n)\n```\n\n---\n\n## Helm\n\n  [Helm]: https://helm.sh/\n\nPackage and publish [Helm][] charts to OCI or HTTP(S) registries.\n\n__Quickstart__\n\n```py\n# kraken.build.py\nfrom kraken.std.helm import helm_push, helm_package, helm_settings\n\nhelm_settings().add_auth("example.jfrog.io", "me@example.org", "api_token")\npackage = helm_package(chart_path="./my-helm-chart")\nhelm_push(chart_tarball=package.chart_tarball, registry="example.jfrog.io/helm-local", tag)\n```\n',
    'author': 'Niklas Rosenstein',
    'author_email': 'rosensteinniklas@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
