from marshmallow import fields, pre_load

from ._base import DataObject, Envelope


class Text(DataObject):
    text = fields.Str(required=True)


class Message(Envelope):
    text = fields.Nested(Text)

    @pre_load
    def short_syntax(self, data, **kwargs):
        if isinstance(data, str):
            # short syntax for text message
            data = {"text": data}
        return data
