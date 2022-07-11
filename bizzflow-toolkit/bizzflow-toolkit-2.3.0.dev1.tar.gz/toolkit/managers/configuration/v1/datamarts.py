from logging import getLogger
from typing import TYPE_CHECKING

from toolkit.managers.configuration.datamarts import BaseDatamartLoader
from toolkit.managers.configuration.v1.validators import DatamartsValidator

if TYPE_CHECKING:
    from toolkit.managers.configuration.v1.loader import V1ConfigurationLoader

logger = getLogger(__name__)


class DatamartLoader(BaseDatamartLoader):
    validator = DatamartsValidator()

    def __init__(self, project_loader: "V1ConfigurationLoader"):
        super().__init__(project_loader)
