from typing import Any, Dict
from pathlib import Path

try:
    import tomllib  # type: ignore
except ModuleNotFoundError:
    import tomli as tomllib  # type: ignore

__version__ = "0.1.0"


class Tool:
    def __init__(self, d: Dict[Any, Any]) -> None:
        for k, v in d.items():
            setattr(self, k.replace("-", "_"), v)


class ToolTable:
    def __init__(self, d: Dict[Any, Any]) -> None:
        for k, v in d.items():
            setattr(self, k.replace("-", "_"), Tool(v))


class PyProjectToml:
    def __init__(self) -> None:
        search_root = Path().cwd()
        search_depth = 1
        max_search_depth = 3
        paths = list(search_root.glob("pyproject.toml"))
        while not paths and search_depth <= max_search_depth:
            search_root = search_root.parent
            paths = list(search_root.glob("pyproject.toml"))
            search_depth += 1
        if not paths:
            raise FileNotFoundError(f"Max search depth reached. Could not find pyproject.toml in {search_root}")
        path = paths.pop()
        with open(path, "rb") as fp:
            self.data = tomllib.load(fp)
        self.tool_table = ToolTable(self.data.get("tool", {}))
