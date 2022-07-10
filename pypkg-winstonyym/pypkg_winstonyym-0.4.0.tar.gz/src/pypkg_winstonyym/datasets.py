from importlib import resources

def get_zen():
    with resources.path("pypkg_winstonyym.data", "zen.txt") as filepath:
        return filepath