from marshmallow import fields, validate

from ._base import Config
from .commands import Commands
from .definitions import Entity, Intent, Node
from .messages import Message


class Telegram(Config):
    api_token = fields.Str(required=True)


class SQLAlchemy(Config):
    url = fields.Str()


class SimilarityRecognizer(Config):
    threshold = fields.Float(validate=validate.Range(min=0.0, max=1.0))


class NLU(Config):
    threshold = fields.Float(validate=validate.Range(min=0.0, max=1.0))


class Services(Config):
    sqlalchemy = fields.Nested(SQLAlchemy)
    similarity_recognizer = fields.Nested(
        SimilarityRecognizer, load_default=SimilarityRecognizer().load({})
    )
    nlu = fields.Nested(NLU, load_default=NLU().load({}))


class Channels(Config):
    telegram = fields.Nested(Telegram())


class Definitions(Config):
    services = fields.Nested(Services(), load_default=Services().load({}))
    channels = fields.Nested(Channels())
    intents = fields.List(fields.Nested(Intent()), load_default=list)
    entities = fields.List(fields.Nested(Entity()), load_default=list)
    dialog = fields.List(fields.Nested(Node()), required=True)


__all__ = ["Config", "Services", "Commands", "Message", "Definitions"]
