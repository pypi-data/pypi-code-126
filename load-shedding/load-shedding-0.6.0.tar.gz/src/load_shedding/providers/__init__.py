#      A python library for getting Load Shedding schedules.
#      Copyright (C) 2021  Werner Pieterson
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.

import abc
import datetime
from enum import Enum
from typing import List, Dict, Any, Tuple


class Municipality:
    def __init__(self, /, **kwargs):
        self.id = kwargs.get("id")
        self.name = kwargs.get("name")

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"Municipality({self.id}, {self.name}"


class Province(Enum):
    UNKNOWN = 0
    EASTERN_CAPE = 1
    FREE_STATE = 2
    GAUTENG = 3
    KWAZULU_NATAL = 4
    LIMPOPO = 6
    MPUMALANGA = 5
    NORTH_WEST = 7
    NORTERN_CAPE = 8
    WESTERN_CAPE = 9

    def __str__(self):
        return {
            self.EASTERN_CAPE: "Eastern Cape",
            self.FREE_STATE: "Free State",
            self.GAUTENG: "Gauteng",
            self.KWAZULU_NATAL: "Kwa-Zulu Natal",
            self.LIMPOPO: "Limpopo",
            self.MPUMALANGA: "Mpumalanga",
            self.NORTH_WEST: "North West",
            self.NORTERN_CAPE: "Nortern Cape",
            self.WESTERN_CAPE: "Western Cape",
        }.get(self, "Unknown")


class StageError(Exception):
    pass


class Stage(Enum):
    UNKNOWN = -1
    NO_LOAD_SHEDDING = 0
    STAGE_1 = 1
    STAGE_2 = 2
    STAGE_3 = 3
    STAGE_4 = 4
    STAGE_5 = 5
    STAGE_6 = 6
    STAGE_7 = 7
    STAGE_8 = 8

    def __str__(self):
        return {
            self.NO_LOAD_SHEDDING.value: "No Load Shedding",
            self.STAGE_1.value: "Stage 1",
            self.STAGE_2.value: "Stage 2",
            self.STAGE_3.value: "Stage 3",
            self.STAGE_4.value: "Stage 4",
            self.STAGE_5.value: "Stage 5",
            self.STAGE_6.value: "Stage 6",
            self.STAGE_7.value: "Stage 7",
            self.STAGE_8.value: "Stage 8",
        }.get(self.value, "Unknown")


class Suburb:
    def __init__(self, /, **kwargs):
        self.id = kwargs.get("id")
        self.name = kwargs.get("name")
        self.municipality = kwargs.get("municipality")
        self.province = Provider.province_from_name(kwargs.get("province"))
        self.total = kwargs.get("total")

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"Suburb({self.id}, {self.name}, {self.municipality}, {self.province}, {self.total})"


class Timeslot:
    start: datetime.date
    end: datetime.date


def dict_list_to_obj_list(data: List[Dict], T: Any) -> List[Any]:
    objs: List[Any] = []
    for d in data:
        s = T(**d)
        objs.append(s)
    return objs


def obj_list_to_dict_list(data: List[Any]) -> List[Dict]:
    dicts: List[Dict] = []
    for d in data:
        # s = T(**d)
        dicts.append(d.__dict__)
    return dicts


def filter_empty_suburbs(suburbs: List[Suburb]) -> List[Suburb]:
    filtered: List[Suburb] = []
    for s in suburbs:
        if not s.total:
            continue
        filtered.append(s)
    return filtered


class ProviderError(Exception):
    pass


class Provider(abc.ABC):
    name: str = ""

    @classmethod
    def province_from_name(cls, name: str) -> Province:
        return {
            "Eastern Cape": Province.EASTERN_CAPE,
            "Free State": Province.FREE_STATE,
            "Gauteng": Province.GAUTENG,
            "Kwa-Zulu Natal": Province.KWAZULU_NATAL,
            "Limpopo": Province.LIMPOPO,
            "Mpumalanga": Province.MPUMALANGA,
            "North West": Province.NORTH_WEST,
            "Nortern Cape": Province.NORTERN_CAPE,
            "Western Cape": Province.WESTERN_CAPE,
        }.get(name, Province.UNKNOWN)

    @abc.abstractmethod
    def get_stage(self) -> Stage:
        pass

    @abc.abstractmethod
    def get_schedule(self) -> List[Tuple]:
        raise NotImplemented

    @abc.abstractmethod
    def search(self, search_text: str, max_results: int = None) -> List[Any]:
        pass

