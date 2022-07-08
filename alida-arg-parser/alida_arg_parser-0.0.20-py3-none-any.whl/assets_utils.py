from alidaargparser import ArgumentParser


def get_asset_property(asset_name, property=None):
    parser = ArgumentParser("", "")
    args = vars(parser.parse_args())
    if property is None:
        return args[asset_name]
    return args[asset_name + "." + property]
