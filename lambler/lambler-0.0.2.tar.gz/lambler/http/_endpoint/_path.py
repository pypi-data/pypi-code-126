import re
from typing import Dict, List


class EndpointPath:
    def __init__(self, pattern: re.Pattern, keys: List[str]):
        self._pattern = pattern
        self._keys = keys

    @classmethod
    def create(cls, path: str) -> 'EndpointPath':
        keys = re.findall(r"\{(.*?)}", path)
        pattern_str = '^' + re.sub(r"\{.*?}", r"(.*?)", path)
        pattern = re.compile(pattern_str)
        return cls(pattern, keys)

    def match(self, path: str) -> bool:
        return bool(self._pattern.match(path))

    def extract_params(self, path: str) -> Dict[str, str]:
        params = self._pattern.findall(path)
        return {key: params[i] for i, key in enumerate(self._keys)}
