from __future__ import annotations

import os
from typing import List
from requests import Session, Response
from facebookcloudapi.api.abstract import APIAbstract
from facebookcloudapi.api.dto.message_object import MessageObject, MessageType
from facebookcloudapi.api.dto import (TextObject, ContactObject, InteractiveObject, LocationObject, TemplateObject)


class API(APIAbstract):
    version = "v13.0"

    def send_message_object(self, from_number_id: str, message_object: MessageObject,
                            object_data: TextObject | List[ContactObject] | InteractiveObject | LocationObject | TemplateObject,
                            messaging_product="whatsapp") -> Response:
        url = f"{self.api_url}/{from_number_id}/messages"
        object_data_parse = None

        if isinstance(object_data, list):
            object_data_parse = list(map(lambda obj: obj.to_dict(), object_data))
        else:
            object_data_parse = object_data.to_dict()

        data = {
            "type": message_object.message_type.value,
            "messaging_product": messaging_product,
            "to": message_object.to,
            message_object.message_type.value: object_data_parse
        }

        if message_object.recipient_type:
            data["recipient_type"] = message_object.recipient_type

        return self.session.post(
            url=url,
            json=data
        )

    def send_message(self, from_number_id: str, message_object: MessageObject, object_data: TextObject,
                     messaging_product="whatsapp") -> Response:
        return self.send_message_object(
            from_number_id=from_number_id,
            message_object=message_object,
            object_data=object_data,
            messaging_product=messaging_product
        )

    def send_contact(self, from_number_id: str, message_object: MessageObject, object_data: List[ContactObject],
                     messaging_product="whatsapp") -> Response:
        return self.send_message_object(
            from_number_id=from_number_id,
            message_object=message_object,
            object_data=object_data,
            messaging_product=messaging_product
        )

    def send_interactive(self, from_number_id: str, message_object: MessageObject, object_data: InteractiveObject,
                         messaging_product="whatsapp") -> Response:
        return self.send_message_object(
            from_number_id=from_number_id,
            message_object=message_object,
            object_data=object_data,
            messaging_product=messaging_product
        )

    def send_location(self, from_number_id: str, message_object: MessageObject, object_data: LocationObject,
                      messaging_product="whatsapp"):
        return self.send_message_object(
            from_number_id=from_number_id,
            message_object=message_object,
            object_data=object_data,
            messaging_product=messaging_product
        )

    def send_template(self, from_number_id: str, message_object: MessageObject, object_data: TemplateObject,
                      messaging_product="whatsapp") -> Response:
        return self.send_message_object(
            from_number_id=from_number_id,
            message_object=message_object,
            object_data=object_data,
            messaging_product=messaging_product
        )
