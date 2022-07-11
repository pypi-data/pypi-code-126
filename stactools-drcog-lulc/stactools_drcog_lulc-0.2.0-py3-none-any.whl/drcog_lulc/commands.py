import logging
import os
from typing import Optional

import click
from pystac import CatalogType

from stactools.drcog_lulc import stac
from stactools.drcog_lulc.tile import remove_nodata, tile

logger = logging.getLogger(__name__)


def create_drcog_lulc_command(cli):
    """Creates the stactools-drcog-lulc command line utility."""

    @cli.group(
        "drcog-lulc",
        short_help=("Commands for working with stactools-drcog-lulc"),
    )
    def drcog_lulc():
        pass

    @drcog_lulc.command(
        "create-collection",
        short_help="Creates a STAC collection",
    )
    @click.argument("OUTDIR")
    @click.option("-f", "--file-list", help="File containing list of COG tile HREFs")
    @click.option(
        "--validate/--no-validate",
        help="Validate the collection before saving",
        default=True,
    )
    def create_collection_command(
        outdir: str,
        file_list: Optional[str],
        validate: bool,
    ):
        """Creates a STAC Collection.

        \b
        Args:
            outdir (str): The destination directory.
            file_list (Optional[str]): Text file containing one HREF per line.
                The HREFs should point to COG classification tiles.
            validate (bool): Flag to validate the Collection and all Items.
        """
        collection = stac.create_collection()

        if file_list:
            with open(file_list) as f:
                cog_hrefs = [os.path.abspath(line.strip()) for line in f.readlines()]
            for cog_href in cog_hrefs:
                item = stac.create_item(cog_href)
                collection.add_item(item)
            collection.update_extent_from_items()

        collection.normalize_hrefs(outdir)
        if validate:
            collection.validate_all()
        collection.make_all_asset_hrefs_relative()
        collection.save(catalog_type=CatalogType.SELF_CONTAINED)

        return None

    @drcog_lulc.command("create-item", short_help="Creates a STAC item")
    @click.argument("INFILE")
    @click.argument("OUTDIR")
    def create_item_command(infile: str, outdir: str):
        """Creates a STAC Item

        \b
        Args:
            infile (str): HREF of a classificaton COG tile.
            outdir (str): Directory that will contain the STAC Item.
        """
        item = stac.create_item(infile)
        item_path = os.path.join(outdir, f"{item.id}.json")
        item.set_self_href(item_path)
        item.make_asset_hrefs_relative()
        item.validate()
        item.save_object(include_self_link=False)

        return None

    @drcog_lulc.command("tile", short_help="Tiles a GeoTIFF to a grid of COGs")
    @click.argument("INFILE")
    @click.argument("OUTDIR")
    @click.argument("ORIGIN_X", type=int)
    @click.argument("ORIGIN_Y", type=int)
    @click.argument("SIZE", type=int)
    @click.option("-n", "--nodata", type=int, help="nodata value")
    def tile_command(
        infile: str,
        outdir: str,
        origin_x: int,
        origin_y: int,
        size: int,
        nodata: Optional[int] = None,
    ) -> None:
        """Tiles an input GeoTIFF to a grid of COGs.

        \b
        Args:
            infile (str): HREF to source GeoTIFF to be tiled
            outdir (str): Directory that will contain the COG tiles
            origin_x (int): X coordinate of the tile grid origin. The origin is
                the lower left corner of the area to be tiled.
            origin_y (int): Y coordinate of the tile grid origin. The origin is
                the lower left corner of the area to be tiled.
            size (int): Tile size in linear units of data, e.g., meters or feet.
            nodata (Optional[int]): nodata value to use for tiled COGs. Only
                necessary if the INFILE GeoTIFF does not contain a correct
                nodata value.
        """
        tile(infile, outdir, size, origin_x, origin_y, nodata)

        return None

    @drcog_lulc.command(
        "remove-nodata-tifs",
        short_help="Removes TIF files that contain only nodata values",
    )
    @click.argument("INDIR")
    @click.option("-n", "--nodata_dir", help="directory to place nodata TIF files")
    def remove_nodata_tifs_command(
        indir: str, nodata_dir: Optional[str] = None
    ) -> None:
        """Moves TIF files that contain only nodata values to a new directory.

        Useful after tiling a large area where many tiles do not intersect valid
        data. The default location for the nodata-only TIF files is a new
        subdirectory named 'nodata_tifs' within the directory of the TIF files
        being examined. Use the --nodata_dir option to override this default
        name and location.

        \b
        Args:
            indir (str): Directory of TIF files to be examined.
            nodata_dir (Optional[str]): Optional directory for the nodata TIF
                files.
        """
        if nodata_dir is None:
            nodata_dir = os.path.join(indir, "nodata_tifs")
        remove_nodata(indir, nodata_dir)

        return None

    return drcog_lulc
