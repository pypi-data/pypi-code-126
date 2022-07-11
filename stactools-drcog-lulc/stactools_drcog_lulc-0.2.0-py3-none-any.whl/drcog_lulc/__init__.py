import stactools.core

from stactools.drcog_lulc.stac import create_collection, create_item
from stactools.drcog_lulc.tile import remove_nodata, tile

__all__ = ["create_collection", "create_item", "tile", "remove_nodata"]

stactools.core.use_fsspec()


def register_plugin(registry):
    from stactools.drcog_lulc import commands

    registry.register_subcommand(commands.create_drcog_lulc_command)


__version__ = "0.2.0"
