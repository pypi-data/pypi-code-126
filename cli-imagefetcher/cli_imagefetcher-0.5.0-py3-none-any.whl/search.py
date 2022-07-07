import requests
from .CONSTANTS import *
from datetime import datetime
from requests.auth import HTTPBasicAuth


def dataApiSearch(apikey, toi, aoi):
    filters = _createFilters(toi, aoi)
    geojsonResponse = networkRequest(apikey, filters)
    feature = _selectResults(geojsonResponse)
    return feature


# Display & cycling results is trivial but time consuming so I have skipped it.
def _selectResults(geojsonResults):
    # prompt = typer.prompt("enter text")
    # typer.echo(f"Prompt: {prompt}")

    # Key error exception here due to no data
    return [geojsonResults["features"][0]["id"]]


def _createFilters(toi, aoi):
    geometryFilter = {
        "type": "GeometryFilter",
        "field_name": "geometry",
        "config": aoi,
    }

    # Convert to Zulu time
    dateArray = toi.split(",")
    dateArrayZuluTime = [
        datetime.strptime(dateString.strip(), "%Y-%m-%d").strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        )
        for dateString in dateArray
    ]

    dateRangeFilter = {
        "type": "DateRangeFilter",
        "field_name": "acquired",
        "config": {"gte": dateArrayZuluTime[0], "lte": dateArrayZuluTime[1]},
    }

    assetsFilter = {"type": "AssetFilter", "config": ["ortho_visual"]}

    permissionsFilter = {
        "type": "PermissionFilter",
        "config": ["assets:download"],
    }

    combinedFilter = {
        "type": "AndFilter",
        "config": [
            geometryFilter,
            dateRangeFilter,
            permissionsFilter,
            assetsFilter,
        ],
    }

    return combinedFilter


def networkRequest(apikey, filters):

    searchRequest = {"item_types": [ITEM_TYPE], "filter": filters}

    search_result = requests.post(
        DATA_API_ENDPOINT, auth=HTTPBasicAuth(apikey, ""), json=searchRequest
    )

    # Assumed result schema
    ## geojson{} > features[] > feature{} > properties{} / geometry{}
    geojson = search_result.json()
    return geojson
