"""Simple PyPi Wrapper for the NOAA NDBC observation data."""

import logging
import json
import aiohttp
import xmltodict
import collections
from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
import pandas as pd
from datetime import datetime, timezone
import calendar
import asyncio

_LOGGER = logging.getLogger("surfline")

STATION_URL = "https://www.ndbc.noaa.gov/activestations.xml"
OBSERVATION_BASE_URL = "https://www.ndbc.noaa.gov/data/realtime2/"

class NDBC:
    def __init__(
        self, 
        station_id:str,
    ):
        self._station_id = station_id

    async def get_data(self):
        """Get the observation data and structure to meet defined spec."""
        stations = Stations()
        stations_list = await stations.list()
        await stations.close()
        
        if not stations_list[self._station_id]:
            raise ValueError(f"Station ID {self._station_id} is invalid.")

        station = stations_list[self._station_id]
        data = await self.get_json()
        
        structured = {}
        observation = {}

        """Structure the location details."""
        structured["location"] = {
            "latitude": float(station["@lat"]),
            "longitude": float(station["@lon"]),
            "elevation": int(station.get("@elev",0)),
            "name": station["@name"]
        }

        """Structure the observation time."""
        observation_time = datetime(
            int(data[1]["YY"]),
            int(data[1]["MM"]),
            int(data[1]["DD"]),
            int(data[1]["hh"]),
            int(data[1]["mm"]),
            tzinfo=timezone.utc
        )

        observation["time"] = {
            "utc_time": observation_time.isoformat(),
            "unix_time": calendar.timegm(observation_time.utctimetuple())
        }

        """Structure the observation wind."""
        observation["wind"] = {
            "direction": None,
            "direction_unit": data[0]["WDIR"],
            "direction_compass": None,
            "speed": None,
            "speed_unit": data[0]["WSPD"],
            "gusts": None,
            "gusts_unit": data[0]["GST"]
        }

        if data[1]["WDIR"] != "MM":
            observation["wind"]["direction"] = int(data[1]["WDIR"])
            observation["wind"]["direction_compass"] = self.compass_direction(float(data[1]["WDIR"]))

        if data[1]["WSPD"] != "MM":
            observation["wind"]["speed"] = float(data[1]["WSPD"])

        if data[1]["GST"] != "MM":
            observation["wind"]["gusts"] = float(data[1]["GST"])

        """Structure the observation waves."""
        observation["waves"] = {
            "height": None,
            "height_unit": data[0]["WVHT"],
            "period": None,
            "period_unit": data[0]["DPD"],
            "average_period": None,
            "average_period_unit": data[0]["APD"],
            "direction": None,
            "direction_unit": data[0]["MWD"],
            "direction_compass": None,
        }

        if data[1]["WVHT"] != "MM":
            observation["waves"]["height"] = float(data[1]["WVHT"])

        if data[1]["DPD"] != "MM":
            observation["waves"]["period"] = int(data[1]["DPD"])
        
        if data[1]["APD"] != "MM":
            observation["waves"]["average_period"] = int(data[1]["APD"])
        
        if data[1]["MWD"] != "MM":
            observation["waves"]["direction"] = int(data[1]["MWD"])
            observation["waves"]["direction_compass"] = self.compass_direction(float(data[1]["MWD"]))

        """Structure the observation weather."""
        observation["weather"] = {
            "pressure": None,
            "pressure_unit": data[0]["PRES"],
            "air_temperature": None,
            "air_temperature_unit": data[0]["ATMP"],
            "water_temperature": None,
            "water_temperature_unit": data[0]["WTMP"],
            "dewpoint": None,
            "dewpoint_unit": data[0]["DEWP"],
            "visibility": None,
            "visibility_unit": data[0]["VIS"],
            "pressure_tendency": None,
            "pressure_tendency_unit": data[0]["PTDY"],
            "tide": None,
            "tide_unit": data[0]["TIDE"]
        }

        if data[1]["PRES"] != "MM":
            observation["weather"]["pressure"] = float(data[1]["PRES"])

        if data[1]["ATMP"] != "MM":
            observation["weather"]["air_temperature"] = float(data[1]["ATMP"])

        if data[1]["WTMP"] != "MM":
            observation["weather"]["water_temperature"] = float(data[1]["WTMP"])

        if data[1]["DEWP"] != "MM":
            observation["weather"]["dewpoint"] = float(data[1]["DEWP"])

        if data[1]["VIS"] != "MM":
            observation["weather"]["visibility"] = float(data[1]["VIS"])

        if data[1]["PTDY"] != "MM":
            observation["weather"]["pressure_tendency"] = float(data[1]["PTDY"])

        if data[1]["TIDE"] != "MM":
            observation["weather"]["tide"] = float(data[1]["TIDE"])

        """Add the observation to the structured data and return."""
        structured["observation"] = observation

        return structured

    async def get_json(self):
        """Get the observation data from NOAA and convert to json object."""
        response = {}

        if response is not None:
            try:
                data =  await asyncio.gather(self.get_dataframe())
                return data[0]
            except json.decoder.JSONDecodeError as error:
                raise ValueError(f"Error decoding data from NDBC ({error}).")
            except Exception as error:
                raise ValueError(f"Unknown error in NDBC data ({error})")
        else:
            raise ConnectionError("Error getting data from NDBC.")
    
    async def get_dataframe(self):
        request_url = f"{OBSERVATION_BASE_URL}{self._station_id}.txt"
        col_specification = [
            (0,4),
            (5,7),
            (8,10),
            (11,13),
            (14,16),
            (17,21),
            (22,26),
            (27,31),
            (32,38),
            (39,44),
            (45,48),
            (49,52),
            (53,60),
            (61,66),
            (67,72),
            (73,78),
            (79,82),
            (83,88),
            (89,93),
        ]

        data = pd.read_fwf(request_url, colspecs=col_specification)
        data = data.rename(columns={"#YY":"YY"})

        return json.loads(data.to_json(orient="records"))

    def compass_direction(self, degrees:float):
        if degrees > 11.25 and degrees <= 33.75:
            return "NNE"
        elif degrees > 33.75 and degrees <= 56.25:
            return "NE"
        elif degrees > 56.25 and degrees <= 78.75:
            return "ENE"
        elif degrees > 78.75 and degrees <= 101.25:
            return "E"
        elif degrees > 101.25 and degrees <= 123.75:
            return "ESE"
        elif degrees > 123.75 and degrees <= 146.25:
            return "SE"
        elif degrees > 146.25 and degrees <= 168.75:
            return "SSE"
        elif degrees > 168.75 and degrees <= 191.25:
            return "S"
        elif degrees > 191.25 and degrees <= 213.75:
            return "SSW"
        elif degrees > 213.75 and degrees <= 236.25:
            return "SW"
        elif degrees > 236.25 and degrees <= 258.75:
            return "WSW"
        elif degrees > 258.75 and degrees <= 281.25:
            return "W"
        elif degrees > 281.25 and degrees <= 303.75:
            return "WNW"
        elif degrees > 303.75 and degrees <= 326.25:
            return "NW"
        elif degrees > 326.25 and degrees <= 348.75:
            return "NNW"

        return "N"


class Stations:
    def __init__(self) -> None:
        self._session = aiohttp.ClientSession()

    async def close(self):
        await self._session.close()
        
    async def list(self):
        response = ""

        async with await self._session.get(STATION_URL) as resp:
            response = await resp.text()

        try:
            my_dict = xmltodict.parse(response)
            json_data = json.dumps(my_dict)
        except:
            raise Exception("Error converting Hayward data to JSON.")

        stations = json.loads(json_data)
        list = {}

        for station in stations["stations"]["station"]:
            list[station["@id"]] = station

        return list
