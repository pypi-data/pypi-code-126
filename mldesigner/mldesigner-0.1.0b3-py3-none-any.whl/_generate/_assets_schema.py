# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
from marshmallow import fields

from azure.ai.ml._schema import PathAwareSchema


class PackageAssetsSchema(PathAwareSchema):
    components = fields.Dict(keys=fields.Str(), values=fields.List(fields.Str()))
