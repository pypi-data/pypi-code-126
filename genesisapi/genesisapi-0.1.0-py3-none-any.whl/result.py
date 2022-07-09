from functools import cached_property

from genesisapi.datatypes import JSON


class Result:

    def __init__(self, json: JSON):
        self.json_result = json

    @cached_property
    def json(self):
        return self.json_result

    @cached_property
    def ident(self):
        return Ident(self.json['Ident'])

    @cached_property
    def status(self):
        return Status(self.json['Status'])

    @cached_property
    def parameter(self):
        return Parameter(self.json['Parameter'])

    @cached_property
    def object(self):
        return Object(self.json['Object'])


class Object(Result):

    def __init__(self, json: JSON):
        super().__init__(json)

    @cached_property
    def code(self):
        return super().json['Code']

    @cached_property
    def content(self):
        return super().json['Content']

    @cached_property
    def type(self):
        return super().json['Type']

    @cached_property
    def values(self):
        return super().json['Values']

    @cached_property
    def information(self):
        return super().json['Information']


class Ident(Result):
    def __init__(self, json: JSON):
        super().__init__(json)

    @cached_property
    def service(self):
        return self.json['Service']

    @cached_property
    def method(self):
        return self.json['Method']


class Status(Result):
    def __init__(self, json: JSON):
        super().__init__(json)

    @cached_property
    def code(self):
        return self.json['Code']

    @cached_property
    def content(self):
        return self.json['Content']


class Parameter(Result):
    def __init__(self, json: JSON):
        super().__init__(json)

    @cached_property
    def json(self):
        return super().json


class Variable(Result):

    def __init__(self, json: JSON):
        super().__init__(json)

    @cached_property
    def code(self):
        return super().object.json['Code']

    @cached_property
    def type(self):
        return super().object.json['Type']

    @cached_property
    def content(self):
        return super().object.json['Content']
