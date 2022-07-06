# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['async_casbin_sqlmodel_adapter']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy[asyncio,mypy]>=1.4.39,<2.0.0',
 'asynccasbin>=1.1.8,<2.0.0',
 'sqlmodel>=0.0.6,<0.0.7']

setup_kwargs = {
    'name': 'async-casbin-sqlmodel-adapter',
    'version': '0.0.1',
    'description': 'Async SQLModel Adapter for PyCasbin',
    'long_description': 'Async SQLModel Adapter for PyCasbin\n====\n\n## Repo\n[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/shepilov-vladislav/async-casbin-sqlmodel-adapter/Pytest?logo=github&style=for-the-badge)](https://github.com/shepilov-vladislav/async-casbin-sqlmodel-adapter)\n[![Codecov](https://img.shields.io/codecov/c/github/shepilov-vladislav/async-casbin-sqlmodel-adapter?logo=codecov&style=for-the-badge)](https://github.com/shepilov-vladislav/async-casbin-sqlmodel-adapter)\n[![Code Climate maintainability](https://img.shields.io/codeclimate/maintainability/shepilov-vladislav/async-casbin-sqlmodel-adapter?logo=code%20climate&style=for-the-badge)](https://github.com/shepilov-vladislav/async-casbin-sqlmodel-adapter)\n[![Dependabot](https://img.shields.io/badge/dependabot-Active-brightgreen?logo=dependabot&style=for-the-badge)](https://github.com/shepilov-vladislav/async-casbin-sqlmodel-adapter)\n\n\n## GitHub\n\n[![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/shepilov-vladislav/async-casbin-sqlmodel-adapter?label=latest%20stable&sort=semver&style=for-the-badge)](https://github.com/shepilov-vladislav/async-casbin-sqlmodel-adapter/releases)\n[![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/shepilov-vladislav/async-casbin-sqlmodel-adapter?label=latest%20unstable&style=for-the-badge)](https://github.com/shepilov-vladislav/async-casbin-sqlmodel-adapter/releases)\n[![GitHub last commit](https://img.shields.io/github/last-commit/shepilov-vladislav/async-casbin-sqlmodel-adapter?style=for-the-badge)](https://github.com/shepilov-vladislav/async-casbin-sqlmodel-adapter/commits/master)\n\n## PyPI\n\n[![PyPI - Version](https://img.shields.io/pypi/v/async-casbin-sqlmodel-adapter?style=for-the-badge)](https://pypi.org/project/async-casbin-sqlmodel-adapter)\n[![PyPI - Python Versions](https://img.shields.io/pypi/pyversions/async-casbin-sqlmodel-adapter?style=for-the-badge)](https://pypi.org/project/async-casbin-sqlmodel-adapter)\n[![PyPI - Python Wheel](https://img.shields.io/pypi/wheel/async-casbin-sqlmodel-adapter?style=for-the-badge)](https://pypi.org/project/async-casbin-sqlmodel-adapter)\n[![PyPI - Format](https://img.shields.io/pypi/format/async-casbin-sqlmodel-adapter?style=for-the-badge)](https://pypi.org/project/async-casbin-sqlmodel-adapter)\n[![PyPI - Status](https://img.shields.io/pypi/status/async-casbin-sqlmodel-adapter?style=for-the-badge)](https://pypi.org/project/async-casbin-sqlmodel-adapter)\n[![PyPI - Downloads](https://img.shields.io/pypi/dd/async-casbin-sqlmodel-adapter?style=for-the-badge)](https://pypi.org/project/async-casbin-sqlmodel-adapter)\n[![PyPI - License](https://img.shields.io/pypi/l/async-casbin-sqlmodel-adapter?style=for-the-badge)](https://pypi.org/project/async-casbin-sqlmodel-adapter)\n\nAsync SQLModel Adapter is the [SQLModel](https://github.com/tiangolo/sqlmodel) adapter for [PyCasbin](https://github.com/casbin/pycasbin). With this library, Casbin can load policy from SQLModel supported database or save policy to it.\n\nBased on [Officially Supported Databases](https://github.com/tiangolo/sqlmodel), The current supported databases are:\n\n- PostgreSQL\n- MySQL\n- SQLite\n\n## Installation\n\n```\npip install async_casbin_sqlmodel_adapter\n```\n\nor\n\n```\npoetry add async-casbin-sqlmodel-adapter\n```\n\n## Simple Example\n\n```python\n# Stdlib:\nimport asyncio\n\n# Thirdparty:\nimport casbin\nfrom async_casbin_sqlmodel_adapter import Adapter\nfrom sqlalchemy.ext.asyncio import create_async_engine\nfrom sqlmodel import Field, SQLModel\n\nengine = create_async_engine("sqlite+aiosqlite:///")\n\n\nclass CasbinRule(SQLModel, table=True):  # type: ignore\n    """\n    CasbinRule class for SQLModel-based Casbin adapter.\n    """\n\n    __tablename__ = "casbin_rule"\n\n    id: int = Field(primary_key=True)\n    ptype: str = Field(max_length=255)\n    v0: str = Field(max_length=255)\n    v1: str = Field(max_length=255)\n    v2: str | None = Field(max_length=255, default=None)\n    v3: str | None = Field(max_length=255, default=None)\n    v4: str | None = Field(max_length=255, default=None)\n    v5: str | None = Field(max_length=255, default=None)\n\n    def __str__(self) -> str:\n        arr = [self.ptype]\n        # pylint: disable=invalid-name\n        for v in (self.v0, self.v1, self.v2, self.v3, self.v4, self.v5):\n            if v is None:\n                break\n            arr.append(v)\n        return ", ".join(arr)\n\n    def __repr__(self) -> str:\n        return f\'<CasbinRule {self.id}: "{str(self)}">\'\n\n\nasync def main():\n    async with engine.begin() as conn:\n        await conn.run_sync(SQLModel.metadata.create_all)\n\n    adapter = Adapter(engine)\n\n    e = casbin.Enforcer("path/to/model.conf", adapter, True)\n\n    sub = "alice"  # the user that wants to access a resource.\n    obj = "data1"  # the resource that is going to be accessed.\n    act = "read"  # the operation that the user performs on the resource.\n\n    if e.enforce(sub, obj, act):\n        # permit alice to read data1async_casbin_sqlmodel_adapter\n        pass\n    else:\n        # deny the request, show an error\n        pass\n\n\nasyncio.run(main())\n```\n\n\n### Getting Help\n\n- [PyCasbin](https://github.com/casbin/pycasbin)\n\n### License\n\nThis project is licensed under the [Apache 2.0 license](LICENSE).\n',
    'author': 'Vladislav Shepilov',
    'author_email': 'shepilov.v@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/shepilov-vladislav/sqlmodel-casbin-adapter',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
