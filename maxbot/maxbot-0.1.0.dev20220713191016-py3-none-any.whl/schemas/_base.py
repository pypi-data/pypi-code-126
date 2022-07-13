from types import SimpleNamespace

from marshmallow import Schema, ValidationError, post_load, pre_load

from ..errors import BotError, YamlSnippet, YamlSymbols
from ._render import Yaml, YamlConfig


class _BaseSchema(Schema):
    def handle_error(self, exc, data, **kwargs):
        """
        Raise only the first error with corresponding source data
        from marshmallow's normalized error messages
        """

        def first_error(errors, source):
            key, messages = next(iter(errors.items()))
            if isinstance(messages, dict):
                return first_error(messages, source[key])
            elif isinstance(messages, list):
                messages = "\n".join(messages)
            return BotError(messages, YamlSnippet.format(source, key=key))

        raise first_error(exc.normalized_messages(), data) from exc


class Config(_BaseSchema):
    class Meta:
        render_module = YamlConfig()

    def from_yaml(self, filename, variables=None):
        with open(filename, "r") as f:
            return self.loads(f, variables=variables)

    @post_load(pass_original=True)
    def create(self, data, original_data, **kwargs):
        for name in self._declared_fields:
            if name in data and name in original_data:
                YamlSymbols.reference(data[name], original_data[name])
            data.setdefault(name, None)
        rv = SimpleNamespace(**data)
        YamlSymbols.reference(rv, original_data)
        return rv


class DataObject(Schema):
    @pre_load
    def short_syntax(self, data, **kwargs):
        # short syntax for schemas class with one required argument
        if isinstance(data, str):
            for name, field in self._declared_fields.items():
                if field.required:
                    data = {name: data}
                    break
        return data

    @post_load
    def create(self, data, **kwargs):
        for name in self._declared_fields:
            data.setdefault(name, None)
        return data


class Envelope(_BaseSchema):
    class Meta:
        render_module = Yaml()

    @post_load
    def unwrap_envelope(self, data, **kwargs):
        if not isinstance(data, dict):
            raise ValidationError("Input data must be a dict.")
        if len(data) != 1:
            raise ValidationError("Input dict must contain exactly one key.")
        name, args = next(iter(data.items()))
        # TODO use dataclasses
        return SimpleNamespace(name=name, **args)
