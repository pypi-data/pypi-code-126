import json
import logging
import pathlib

from jsonschema import ValidationError, validate

from toolkit.managers.configuration.exceptions import ConfigurationNotValid

logger = logging.getLogger(__name__)


class BaseConfigValidator:
    schema_file = NotImplemented
    schema_version = NotImplemented
    ref_files = ["_definitions.schema.json"]

    def __init__(self):
        self._schema = None
        self.schemas_folder = pathlib.Path(__file__).parent / "schemas" / self.schema_version

    @property
    def schema(self):
        if self._schema is None:
            self._schema = self.load_schema()
        return self._schema

    def load_schema(self):
        full_path = self.schemas_folder / self.schema_file
        with open(full_path) as json_file:
            schema_text = json_file.read()
        for ref in self.ref_files:
            schema_text = schema_text.replace(ref, f"file://{self.schemas_folder}/{ref}")
        return json.loads(schema_text)

    def validate(self, config, *args, **kwargs):
        try:
            validate(config, self.schema)
        except ValidationError as e:
            logger.error("Configuration is not valid: %s", e)
            raise ConfigurationNotValid("Configuration is not valid: {}".format(e))
