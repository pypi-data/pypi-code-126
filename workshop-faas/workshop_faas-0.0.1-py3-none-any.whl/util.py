import yaml


def load_yaml(file_path: str) -> dict:
    res = {}
    with open(file_path, "r") as f:
        try:
            res = yaml.safe_load(f)
        except yaml.YAMLError as exc:
            print(exc)
    return res
