from functools import cached_property

from marshmallow import ValidationError, fields, post_load, validate

from ._base import Config
from .commands import (
    FoundCommands,
    NodeCommands,
    NotFoundCommands,
    PromptCommands,
    SlotHandlerCommands,
)


class Intent(Config):
    name = fields.Str(required=True)
    examples = fields.List(fields.Str(), load_default=list)


class EntityValue(Config):
    name = fields.Str(required=True)
    phrases = fields.List(fields.Str(), load_default=list)
    regexps = fields.List(fields.Str(), load_default=list)


class Entity(Config):
    name = fields.Str(required=True)
    values = fields.List(fields.Nested(EntityValue()), load_default=list)


class ExpressionField(fields.Field):
    def _deserialize(self, value, attr, data, **kwargs):
        if isinstance(value, (str, bool, int, float)):
            return value
        raise ValidationError("Invalid expression. Must be one of: str, bool, number")


class Template(Config):
    content = fields.Str(required=True)
    syntax = fields.Str(required=True, validate=validate.OneOf(["raw", "yaml"]))

    @post_load
    def create(self, data, **kwargs):
        data["schema"] = self.context["schema"]
        return data


class ScenarioField(fields.Nested):
    @cached_property
    def template(self):
        template = Template()
        template.context = {"schema": self.schema}
        return template

    def _deserialize(self, value, attr, data, partial=None, **kwargs):
        if isinstance(value, dict):
            return self.template.load(value)
        else:
            return self._load(value, data, partial=partial)


class Slot(Config):
    name = fields.Str(required=True)
    check_for = ExpressionField(required=True)
    value = ExpressionField()
    condition = ExpressionField()
    prompt = ScenarioField(PromptCommands, many=True)
    found = ScenarioField(FoundCommands, many=True)
    not_found = ScenarioField(NotFoundCommands, many=True)


class SlotHandler(Config):
    condition = ExpressionField(required=True)
    response = ScenarioField(SlotHandlerCommands, many=True, required=True)


class NodeSettings(Config):
    after_digression_followup = fields.Str(
        validate=validate.OneOf(["never_return", "allow_return"]), load_default="allow_return"
    )


class Node(Config):
    label = fields.Str()
    condition = ExpressionField(required=True)
    slot_filling = fields.List(fields.Nested(Slot()), load_default=list)
    slot_handlers = fields.List(fields.Nested(SlotHandler()), load_default=list)
    response = ScenarioField(NodeCommands, many=True, required=True)
    followup = fields.List(fields.Nested(lambda: Node()), load_default=list)
    settings = fields.Nested(NodeSettings(), load_default=NodeSettings().load({}))
