from typeguard import typechecked

from genesisapi.datatypes import JSON, Language


class ProfileService:
    service_name = 'profile'

    def __init__(self, client):
        self.client = client

    @typechecked
    def password(
            self,
            username,
            password,
            new,
            repeat,
            language: Language = None
    ) -> JSON:
        pass

    @typechecked
    def remove_result(
            self,
            area,
            language: Language = None
    ) -> JSON:
        pass
