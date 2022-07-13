from marshmallow import fields, pre_load, validate

from ._base import DataObject, Envelope


class Text(DataObject):
    text = fields.Str(required=True)


class Image(DataObject):
    url = fields.Url(required=True)
    caption = fields.Str()


class Commands(Envelope):
    text = fields.Nested(Text)
    image = fields.Nested(Image)

    @pre_load(pass_many=True)
    def short_syntax_list(self, data, **kwargs):
        if isinstance(data, str):
            # short syntax single text command instead of command list
            data = [{"text": {"text": data}}]
        return data


class End(DataObject):
    pass


class Listen(DataObject):
    pass


class Followup(DataObject):
    pass


class JumpTo(DataObject):
    node = fields.Str(required=True)
    transition = fields.Str(required=True, validate=validate.OneOf(["condition", "response"]))


class NodeCommands(Commands):
    end = fields.Nested(End)
    listen = fields.Nested(Listen)
    followup = fields.Nested(Followup)
    jump_to = fields.Nested(JumpTo)


class Response(DataObject):
    pass


class MoveOn(DataObject):
    pass


class ListenAgain(DataObject):
    pass


class PromptAgain(DataObject):
    pass


class FoundCommands(Commands):
    move_on = fields.Nested(MoveOn)
    prompt_again = fields.Nested(PromptAgain)
    listen_again = fields.Nested(ListenAgain)
    response = fields.Nested(Response)


class NotFoundCommands(Commands):
    prompt_again = fields.Nested(PromptAgain)
    listen_again = fields.Nested(ListenAgain)
    response = fields.Nested(Response)


class PromptCommands(Commands):
    listen_again = fields.Nested(ListenAgain)
    response = fields.Nested(Response)


class SlotHandlerCommands(Commands):
    move_on = fields.Nested(MoveOn)
    response = fields.Nested(Response)
