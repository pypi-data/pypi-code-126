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
from typing import Any, List, Tuple

from load_shedding.libs.eskom import LoadShedding
from load_shedding.providers import Suburb, Municipality, Provider, Province, Stage, dict_list_to_obj_list


class AreaInfo:
    def __init__(self, /, **kwargs):
        province = kwargs.get("Province", {})
        self.province = Province(province.get("Id"))
        self.municipality = Municipality(**kwargs.get("Municipality", {}))
        self.suburb = Suburb(**kwargs.get("Suburb", {}), municipality=self.municipality.name,
                             province=self.province.name)
        self.period = kwargs.get("Period")


class Suburb(Suburb):
    def __init__(self, /, **kwargs):
        self.id = kwargs.get("Id", kwargs.get("id"))
        self.name = kwargs.get("Name", kwargs.get("name"))
        self.municipality = Municipality(**kwargs)
        self.province = Eskom.province_from_name(kwargs.get("ProvinceName"))
        self.total = kwargs.get("Total")


class Municipality(Municipality):
    def __init__(self, /, **kwargs):
        self.id = kwargs.get("Value", kwargs.get("Id"))
        self.name = kwargs.get("Text", kwargs.get("MunicipalityName", kwargs.get("Municipality", kwargs.get("Name", kwargs.get("name", "")))))
        self.selected = kwargs.get("Selected")
        self.group = kwargs.get("Group")
        self.disabled = kwargs.get("Disabled")


@Provider.register
class Eskom(Provider):
    name = "Eskom Direct"

    def __init__(self, api: Any = LoadShedding):
        self.api = api()

    def get_schedule(self, province: Province, suburb: Suburb, stage: Stage) -> List[Tuple]:
        data = self.api.get_schedule(province=province.value, suburb_id=suburb.id, stage=stage.value)
        return data

    def get_stage(self) -> Stage:
        data = self.api.get_status()
        return stage_from_status(data)

    def search(self, search_text: str, max_results: int = None) -> List[Any]:
        data = self.api.find_suburbs(search_text, max_results)
        return dict_list_to_obj_list(data, Suburb)


def province_from_name(name: str) -> Province:
    return Provider.province_from_name(name)


def stage_from_status(status: int) -> Stage:
    return {
        1: Stage.NO_LOAD_SHEDDING,
        2: Stage.STAGE_1,
        3: Stage.STAGE_2,
        4: Stage.STAGE_3,
        5: Stage.STAGE_4,
        6: Stage.STAGE_5,
        7: Stage.STAGE_6,
        8: Stage.STAGE_7,
        9: Stage.STAGE_8,
    }.get(status, Stage.UNKNOWN)
