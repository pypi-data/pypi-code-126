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
import datetime
import errno
import json
import logging
import os
from datetime import datetime, timezone
from typing import Any, Dict, Final, List, Tuple

from load_shedding.providers import Provider, Stage, ProviderError, StageError, Province, Suburb
from load_shedding.providers.eskom import Eskom

CACHE_TTL: Final = 86400  # 24 hours


class LoadSheddingError(Exception):
    pass


def get_stage(provider: Provider) -> Stage:
    try:
        stage = provider.get_stage()
    except Exception as e:
        msg = f"Unable to get stage from {provider.name}."
        logging.error(msg, exc_info=True)
        raise ProviderError(msg)
    return stage


def get_schedule(provider: Provider, province: Province, suburb: Suburb, stage: Stage = None,
                 cached: bool = True) -> List[Tuple]:
    try:
        os.makedirs('.cache')
    except OSError as e:
        if e.errno != errno.EEXIST:
            msg = f"Unable to make cache dir."
            logging.error(msg, exc_info=True)
            raise LoadSheddingError(msg)

    if stage in [None]:
        stage = get_stage(provider)

    if stage in [Stage.UNKNOWN, Stage.NO_LOAD_SHEDDING]:
        raise StageError(f"{stage}")

    cached_schedules = {}
    cached_schedule = []
    now = datetime.now(timezone.utc)
    try:
        cache_file = ".cache/{suburb_id}.json".format(suburb_id=suburb.id)
        with open(cache_file, "r") as cache:
            for k, v in json.loads(cache.read()).items():
                cached_schedules[Stage(int(k)).value] = v

            cached_schedule = cached_schedules.get(stage.value, {})

        if not isinstance(cached_schedule, dict) or len(cached_schedule) == 0:
            """ Upgrade from previous list """
            cached = False

        if cached and cached_schedule:
            updated_at = datetime.fromisoformat(cached_schedule.get("updated_at", None))

            cache_age = (now - updated_at)
            if cache_age.total_seconds() < CACHE_TTL:
                return cached_schedule.get("schedule", {})
    except FileNotFoundError as e:
        logging.error("Unable to get schedule from cache. {e}".format(e=e))

    try:
        schedule = provider.get_schedule(province=province, suburb=suburb, stage=stage)
    except Exception as e:
        if cached_schedule:
            return cached_schedule  # best effort
        msg = f"Unable to get schedule from {provider.name}."
        logging.error(msg, exc_info=True)
        raise ProviderError(msg)
    else:
        cache_file = ".cache/{suburb_id}.json".format(suburb_id=suburb.id)
        with open(cache_file, "w") as cache:
            cached_schedules[stage.value] = {
                "updated_at": str(now),
                "schedule": schedule,
            }
            cache.write(json.dumps(cached_schedules))
        return schedule


def search(provider: Provider, search_text: str, max_results: int = None) -> List[Any]:
    try:
        results = provider.search(search_text, max_results)
    except Exception as e:
        msg = f"Unable to search {search_text} from {provider.name}."
        logging.error(msg, exc_info=True)
        raise ProviderError(msg)
    else:
        return results


def list_to_dict(schedule: list) -> Dict:
    schedule_dict = {}
    now = datetime.now(timezone.utc)
    for item in schedule:
        start = datetime.fromisoformat(item[0])
        end = datetime.fromisoformat(item[1])

    schedule_dict[start.strftime("%Y-%m-%d")] = (
        start.replace(second=now.second).strftime("%H:%M"),
        end.replace(second=now.second).strftime("%H:%M"),
    )
    return schedule_dict


def get_providers() -> List[Provider]:
    return [Eskom()]


def search_suburb(provider: Provider, suburb: str) -> Dict:
    try:
        suburb = provider.search_suburb()
    except ProviderError as e:
        msg = f"Unable to search suburb from {provider.name}."
        logging.error(msg, exc_info=True)
        raise StageError(msg)
    return suburb


def dict_list_to_obj_list(data: List[Dict], T: Any) -> Any:
    objs: List = []
    for d in data:
        s = T(**d)
        objs.append(s)
    return objs


def filter_empty_suburbs(suburbs: List[Suburb]) -> List[Suburb]:
    filtered: List[Suburb] = []
    for s in suburbs:
        if not s.total:
            continue
        filtered.append(s)
    return filtered
