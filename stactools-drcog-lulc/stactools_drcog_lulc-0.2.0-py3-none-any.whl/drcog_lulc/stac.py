import copy
import logging
import os
from datetime import datetime, timezone
from typing import Optional

import stactools.core.create
from pystac import Asset, Collection, Item
from pystac.extensions.item_assets import ItemAssetsExtension
from pystac.extensions.raster import RasterExtension
from pystac.utils import make_absolute_href
from stactools.core.io import ReadHrefModifier

from stactools.drcog_lulc import constants

logger = logging.getLogger(__name__)


def create_item(
    asset_href: str, read_href_modifier: Optional[ReadHrefModifier] = None
) -> Item:
    """Create a STAC Item with a single Asset for a COG tile of the DRCOG LULC
    classification product.

    Args:
        asset_href (str): An href to a COG containing a tile of classification
            data.
        read_href_modifier (Callable[[str], str]): An optional function to
            modify hrefs (e.g. to add a token to a url).

    Returns:
        Item: STAC Item object representing the landcover tile
    """
    id = os.path.splitext(os.path.basename(asset_href))[0]
    year = int(id.split("_")[1])

    item = stactools.core.create.item(asset_href, read_href_modifier=read_href_modifier)

    item.id = id
    item.common_metadata.start_datetime = datetime(year, 1, 1)
    item.common_metadata.end_datetime = datetime(year, 12, 31, 23, 59, 59)
    item.datetime = None
    item.common_metadata.created = datetime.now(tz=timezone.utc)
    item.common_metadata.description = constants.ITEM_DESCRIPTION[year]
    item.common_metadata.mission = constants.MISSION[year]

    asset_dict = copy.deepcopy(constants.ASSET_PROPS)
    asset_dict["href"] = make_absolute_href(asset_href)
    asset_dict["raster:bands"][0]["spatial_resolution"] = constants.RESOLUTION[year]
    item.add_asset("data", Asset.from_dict(asset_dict))

    RasterExtension.add_to(item)
    item.stac_extensions.append(constants.CLASSIFICATION_SCHEMA)

    item.validate()

    return item


def create_collection(collection_id: str = constants.COLLECTION_ID) -> Collection:
    """Creates a STAC Collection for the 2018 and 2020 DRCOG LULC classification
    product.

    Args:
        collection_id (str): Desired ID for the STAC Collection.

    Returns:
        Collection: The created STAC Collection.
    """
    collection = Collection(
        id=collection_id,
        title=constants.COLLECTION_TITLE,
        description=constants.COLLECTION_DESCRIPTION,
        license=constants.LICENSE,
        keywords=constants.KEYWORDS,
        providers=constants.PROVIDERS,
        extent=constants.EXTENT,
        summaries=constants.SUMMARIES,
    )

    item_assets = ItemAssetsExtension.ext(collection, add_if_missing=True)
    item_assets.item_assets = constants.ITEM_ASSETS

    RasterExtension.add_to(collection)
    collection.stac_extensions.append(constants.CLASSIFICATION_SCHEMA)

    collection.add_links(
        [
            constants.LICENSE_LINK,
            constants.REPORT_LINK,
            constants.DATA_LINK_2018,
            constants.DATA_LINK_2020,
        ]
    )

    return collection
