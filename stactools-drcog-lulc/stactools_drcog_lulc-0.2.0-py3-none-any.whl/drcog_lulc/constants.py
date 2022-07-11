from datetime import datetime
from typing import Any, Dict

from pystac import (
    Extent,
    Link,
    Provider,
    ProviderRole,
    SpatialExtent,
    Summaries,
    TemporalExtent,
)
from pystac.extensions.item_assets import AssetDefinition

ITEM_DESCRIPTION = {
    2018: "2018 Denver Regional Council of Governments (DRCOG) Land Use Land Cover (LULC) at 3.28ft (1m) resolution",  # noqa
    2020: "2020 Denver Regional Council of Governments (DRCOG) Land Use Land Cover (LULC) at 1ft resolution",  # noqa
}
MISSION = {
    2018: "2018 DRCOG LULC pilot study covering 1,000 square miles",
    2020: "2020 DRCOG LULC study covering 6,000 square miles",
}
RESOLUTION = {2018: 1, 2020: 0.3}
CLASSIFICATION_SCHEMA = (
    "https://stac-extensions.github.io/classification/v1.1.0/schema.json"
)

# fmt: off
ASSET_PROPS: Dict[str, Any] = {
    "title": "DRCOG LULC",
    "description": "Denver Regional Council of Governments (DRCOG) Land Use Land Cover (LULC) Classifications",  # noqa
    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
    "roles": ["data"],
    "raster:bands": [
        {
            "description": "Classification values",
            "sampling": "area",
            "data_type": "uint8",
            "unit": "usft",
        }
    ],
    "classification:classes": [
        {"value": 1, "description": "Structures", "color_hint": "FF0000"},
        {"value": 2, "description": "Impervious Surfaces", "color_hint": "B2B2B2"},
        {"value": 3, "description": "Water", "color_hint": "00A9E6"},
        {"value": 4, "description": "Prairie/Grassland/Natural Ground Cover", "color_hint": "C7D79E"},   # noqa
        {"value": 5, "description": "Tree Canopy", "color_hint": "267300"},
        {"value": 6, "description": "Turf/Irrigated Land", "color_hint": "70A800"},
        {"value": 7, "description": "Barren Land", "color_hint": "FFEBAF"},
        {"value": 8, "description": "Cropland", "color_hint": "FFAE42"},
    ],
}
# fmt: on

COLLECTION_ID = "drcog-lulc"
COLLECTION_TITLE = "DRCOG LULC"
COLLECTION_DESCRIPTION = "The Denver Regional Council of Governments (DRCOG) Land Use/Land Cover (LULC) datasets are developed in partnership with Babbit Center for Land and Water Policy and the Chesapeake Conservancy's Conservation Innovation Center (CIC). DRCOG LULC includes 2018 data at 1m (3.28ft) resolution covering 1,000 square miles and 2020 data at 1ft resolution covering 6,000 square miles of the Denver, Colorado region. The data is based on USDA's 1 meter National Agricultural Imagery Program (NAIP) aerial imagery and leaf-off aerial ortho-imagery captured as part of the Denver Regional Aerial Photography Project (6-inch resolution everywhere except the mountainous regions to the west, which came in 1-foot resolution)."  # noqa
LICENSE = "proprietary"
LICENSE_LINK = Link(
    rel="license",
    target="https://drcog.org/legal-terms",
    title="DRCOG Legal Terms",
    media_type="text/html",
)
KEYWORDS = ["Land Cover", "Land Use", "NAIP", "USDA"]
PROVIDERS = [
    Provider(
        name="Denver Regional Council of Governments",
        roles=[
            ProviderRole.PRODUCER,
            ProviderRole.LICENSOR,
        ],
        url=(
            "https://drcog.org/services-and-resources/data-maps-and-modeling/"
            "regional-land-use-land-cover-project"
        ),
    )
]
EXTENT = Extent(
    SpatialExtent(
        [
            [
                -105.93962510864995,
                39.10438697007073,
                -103.66801443832743,
                40.320593119647256,
            ],
            [
                -105.54671456161505,
                39.54013841830152,
                -104.46335720577567,
                39.94430501943824,
            ],
        ]
    ),
    TemporalExtent([[datetime(2018, 1, 1), datetime(2020, 12, 31, 23, 59, 59)]]),
)
SUMMARIES = Summaries({"mission": list(MISSION.values())})
ITEM_ASSETS = {"data": AssetDefinition(ASSET_PROPS)}
REPORT_LINK = Link(
    rel="describedby",
    target="https://gis.drcog.org/rdc/supplemental/lulc_pilot_report.zip",
    title="Supplemental Information",
    media_type="application/zip",
)
DATA_LINK_2018 = Link(
    rel="original",
    target="https://landcoverarchive.s3.amazonaws.com/2018/lulc_pilot_raster_2018.zip",
    title="Land_Cover_Raster_Data_2018",
    media_type="application/zip",
)
DATA_LINK_2020 = Link(
    rel="original",
    target="https://landcoverarchive.s3.amazonaws.com/2020/DRCOG_2020_Landcover.zip",
    title="Land_Cover_Raster_Data_2020",
    media_type="application/zip",
)
