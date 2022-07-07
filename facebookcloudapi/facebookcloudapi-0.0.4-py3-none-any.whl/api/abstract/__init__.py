from __future__ import annotations

import os
from facebookcloudapi import CLOUD_API_BASE_URL, CLOUD_API_LAST_VERSION
from requests import Session, Response

from facebookcloudapi.api.dto import (MessageObject, ContactObject, InteractiveObject, LocationObject, TemplateObject)
from facebookcloudapi.api.dto.text_object import TextObject
from dotenv import load_dotenv

load_dotenv()


class APIAbstract:
    __session: Session = None
    version = CLOUD_API_LAST_VERSION
    api_url = None
    access_token: str = ""

    def __init__(self, access_token: str = os.getenv('FACEBOOK_CLOUD_ACCESS_TOKEN')):
        assert access_token is not None
        self.api_url = f"{CLOUD_API_BASE_URL}/{self.version}"
        self.access_token = access_token

    @property
    def session(self) -> Session:
        if not isinstance(self.__session, Session):
            self.start_session()
            self.__session.headers.update({
                'Authorization': f'Bearer {self.access_token}',
                'Content-Type': 'application/json'
            })

        return self.__session

    def start_session(self):
        self.__session = Session()

    def send_message_object(self, from_number_id: str, message_object: MessageObject,
                            object_data: TextObject | ContactObject | InteractiveObject | LocationObject | TemplateObject,
                            messaging_product="whatsapp") -> Response:
        raise NotImplementedError('This function is not implemented in this class or version.'
                                  'Try on a different version.')

    def send_template(self, from_number_id: str, to: str, message_object: MessageObject, object_data: TemplateObject,
                      messaging_product="whatsapp") -> Response:
        raise NotImplementedError('This function is not implemented in this class or version.'
                                  'Try on a different version.')

    def send_message(self, from_number_id: str, message_object: MessageObject, object_data: TextObject,
                     messaging_product="whatsapp") -> Response:
        raise NotImplementedError('This function is not implemented in this class or version.'
                                  'Try on a different version.')

    def send_contact(self, from_number_id: str, message_object: MessageObject, object_data: ContactObject,
                     messaging_product="whatsapp") -> Response:
        raise NotImplementedError('This function is not implemented in this class or version.'
                                  'Try on a different version.')

    def send_interactive(self, from_number_id: str, message_object: MessageObject, object_data: InteractiveObject,
                         messaging_product="whatsapp") -> Response:
        raise NotImplementedError('This function is not implemented in this class or version.'
                                  'Try on a different version.')

    def send_location(self, from_number_id: str, message_object: MessageObject, object_data: LocationObject,
                      messaging_product="whatsapp") -> Response:
        raise NotImplementedError('This function is not implemented in this class or version.'
                                  'Try on a different version.')
