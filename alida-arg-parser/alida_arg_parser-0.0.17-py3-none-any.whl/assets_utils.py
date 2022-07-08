from alidaargparser import ArgumentParser


def get_asset_property(asset_name, property):
    parser = ArgumentParser(None, None)
    args = parser.parse_args()
    return args[asset_name + "." + property]
