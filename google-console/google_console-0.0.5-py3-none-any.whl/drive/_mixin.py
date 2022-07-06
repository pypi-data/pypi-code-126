from .._pipeline import Base
from typing import List, Union
import builtins

from ._about import About


class DriveMixin(Base):
    
    def __init__(self, api_name: str, client_secret_file: str, api_version: str, scopes: Union[List[str], str],
                 recreate_service: bool, prefix: str, suffix: str, token_dir: str):
        super().__init__(api_name, client_secret_file, api_version, scopes, recreate_service, prefix, suffix, token_dir)
        builtins.__MIXIN__ = self.service

        args = (client_secret_file, api_version, recreate_service, prefix, suffix, token_dir)
        self.about = About(*args)

        del builtins.__MIXIN__  # type: ignore
    