from typing import Set

from inflection import underscore
from pydantic import BaseModel

FLAT_STRUCT_DELIMITER = '___'


class MAVLinkMetricBaseModel(BaseModel):
    @classmethod
    def from_mavlink(cls, mavlink_object):
        return cls(**mavlink_object.__dict__)

    @classmethod
    def get_metric_name(cls) -> str:
        return underscore(cls.__name__)

    @classmethod
    def get_list_fields_names(cls) -> Set[str]:
        return set()

    def get_mavlink_data_class_name(self) -> str:
        raise NotImplemented

    def as_flat_dict(self):
        return self.dict()
