import os
from typing import NamedTuple, Optional

# pip dependencies
import yaml
from schema import Optional as Nullable, Schema, SchemaError, Or

SCHEMA_ENTRY = {
    # TODO: tags
    Nullable("requirements"): {
        Nullable("binaries"): list[str],
        Nullable("files"): list[str],
        Nullable("dirs"): list[str],
    },
    # One of the following two options should be given
    Or("contents", "contents-mako", "file", only_one=True): str,
}

FILE_SCHEMA = Schema(
    {
        "output_dir": str,
        "entries": [
            {
                "name": str,
                "options": list[SCHEMA_ENTRY],
            }
        ],
    }
)


class ConfigOption(NamedTuple):
    # Flat hirachies are easier to handle in code: requirements.binaries -> required_binaries, ...
    required_binaries: list[str]
    required_files: list[str]
    required_dirs: list[str]
    contents_mako: Optional[str]
    contents_str: Optional[str]
    contents_file: Optional[str]


class ConfigEntry(NamedTuple):
    name: str
    options: list[ConfigOption]


class Config(NamedTuple):
    output_dir: str
    entries: dict[str, ConfigEntry]


class ConfigParser:
    def __init__(self, path: str):
        self.config_path = path
        self.config_dir = os.path.abspath(os.path.dirname(path))

    def parse_config(self) -> Config:
        with open(self.config_path, "rb") as f:
            data = yaml.safe_load(f)
        FILE_SCHEMA.validate(data)

        output_dir = data["output_dir"]

        entries = {}
        for entry_data in data["entries"]:
            entry = self.parse_config_entry(entry_data)

            if entry.name in entries:
                raise Exception(f"Multiple entries for '{name}'")
            else:
                entries[entry.name] = entry

        return Config(
            entries=entries,
            output_dir=self.abs_path(output_dir),
        )

    def parse_config_entry(self, entry: dict) -> ConfigEntry:
        name = entry["name"]
        options = []
        for opt in entry["options"]:
            requirements = opt.get("requirements", {})
            bins = requirements.get("binaries", [])
            files = requirements.get("files", [])
            dirs = requirements.get("dirs", [])

            contents_mako = opt.get("contents-mako")
            contents_str = opt.get("contents")
            contents_file = opt.get("file")

            if not (contents_str or contents_mako or contents_file):
                raise Exception(f"Script contents are all empty: {opt}")

            options.append(ConfigOption(
                required_binaries=bins,
                required_files=self.abs_paths(files),
                required_dirs=self.abs_paths(dirs),
                contents_mako=contents_mako,
                contents_str=contents_str,
                contents_file=self.abs_path(contents_file),
            ))

        return ConfigEntry(
            name=name,
            options=options,
        )

    def abs_paths(self, path_list: list[str]) -> list[str]:
        return [self.abs_path(path) for path in path_list]

    def abs_path(self, path: Optional[str]) -> Optional[str]:
        if not path:
            return None

        # Replace "$CONFIG" with the directory that the config is in
        if path.startswith("$CONFIG"):
            path = path.replace("$CONFIG", self.config_dir, 1)

        real_path = os.path.expanduser(path)
        if not os.path.isabs(real_path):
            raise Exception(f"Path is relative, but has to be absolute: '{path}'")
        return real_path


def parse_config(path: str) -> Config:
    return ConfigParser(path).parse_config()
