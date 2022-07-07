import unittest, os

from facebookcloudapi.api.dto import (TextObject, ContactObject, MessageObject, InteractiveObject, LocationObject,
                                      TemplateObject)
from facebookcloudapi.api.dto.types import (MessageType, InteractiveType, HeaderType)
from facebookcloudapi.api.dto.inherited import (NameObject, ActionObject, BodyObject, ButtonObject, HeaderObject,
                                                FooterObject, SectionObject, RowObject)
from facebookcloudapi.api.version_v13_0 import API


class TestSendMessage(unittest.TestCase):
    def setUp(self) -> None:
        self.api = API()

    def test_send_text(self):
        response = self.api.send_message(
            from_number_id=os.getenv('FACEBOOK_CLOUD_TEST_NUMBER_ID'),
            message_object=MessageObject(
                message_type=MessageType.TEXT,
                to=os.getenv('FACEBOOK_CLOUD_TEST_TO')
            ),
            object_data=TextObject(
                body="Hello World!"
            )
        )
        self.assertIs(response.status_code, 200)
        response.close()

    def test_send_contact(self):
        response = self.api.send_contact(
            from_number_id=os.getenv('FACEBOOK_CLOUD_TEST_NUMBER_ID'),
            message_object=MessageObject(
                message_type=MessageType.CONTACTS,
                to=os.getenv('FACEBOOK_CLOUD_TEST_TO')
            ),
            object_data=[ContactObject(
                name=NameObject(
                    formatted_name="Test User",
                    first_name="Test",
                    last_name="User"
                )
            )]
        )
        self.assertIs(response.status_code, 200)
        response.close()

    def test_send_interactive_button(self):
        response = self.api.send_interactive(
            from_number_id=os.getenv('FACEBOOK_CLOUD_TEST_NUMBER_ID'),
            message_object=MessageObject(
                message_type=MessageType.INTERACTIVE,
                to=os.getenv('FACEBOOK_CLOUD_TEST_TO')
            ),
            object_data=InteractiveObject(
                action=ActionObject(
                    buttons=[
                        ButtonObject(
                            title="Test 01",
                            button_id="test_01"
                        ),
                        ButtonObject(
                            title="Test 02",
                            button_id="test_02"
                        ),
                    ]
                ),
                interactive_type=InteractiveType.BUTTON,
                body=BodyObject(text="Button Test")
            )
        )
        self.assertIs(response.status_code, 200)
        response.close()

    def test_send_interactive_list(self):
        response = self.api.send_interactive(
            from_number_id=os.getenv('FACEBOOK_CLOUD_TEST_NUMBER_ID'),
            message_object=MessageObject(
                message_type=MessageType.INTERACTIVE,
                to=os.getenv('FACEBOOK_CLOUD_TEST_TO')
            ),
            object_data=InteractiveObject(
                header=HeaderObject(
                    header_type=HeaderType.TEXT,
                    text="Header"
                ),
                body=BodyObject(text="Button Test"),
                footer=FooterObject(text="Footer Text"),
                action=ActionObject(
                    button="Button Text",
                    sections=[
                        SectionObject(title="Section 01", rows=[
                            RowObject(row_id="SECTION_1_ROW_1_ID", row_title="SECTION_1_ROW_1_TITLE",
                                      row_description="SECTION_1_ROW_1_DESCRIPTION"),
                            RowObject(row_id="SECTION_1_ROW_2_ID", row_title="SECTION_1_ROW_2_TITLE",
                                      row_description="SECTION_1_ROW_2_DESCRIPTION"),
                        ]),
                        SectionObject(title="Section 02", rows=[
                            RowObject(row_id="SECTION_2_ROW_1_ID", row_title="SECTION_2_ROW_1_TITLE",
                                      row_description="SECTION_2_ROW_1_DESCRIPTION"),
                            RowObject(row_id="SECTION_2_ROW_2_ID", row_title="SECTION_2_ROW_2_TITLE",
                                      row_description="SECTION_2_ROW_2_DESCRIPTION"),
                        ])
                    ]
                ),
                interactive_type=InteractiveType.LIST,

            )
        )
        self.assertIs(response.status_code, 200)
        response.close()

    def test_send_location(self):
        response = self.api.send_location(
            from_number_id=os.getenv('FACEBOOK_CLOUD_TEST_NUMBER_ID'),
            message_object=MessageObject(
                message_type=MessageType.LOCATION,
                to=os.getenv('FACEBOOK_CLOUD_TEST_TO')
            ),
            object_data=LocationObject(
                latitude="-19.3909",
                longitude="-40.0715"
            )
        )
        self.assertIs(response.status_code, 200)
        response.close()

    def test_send_template(self):
        response = self.api.send_template(
            from_number_id=os.getenv('FACEBOOK_CLOUD_TEST_NUMBER_ID'),
            message_object=MessageObject(
                message_type=MessageType.TEMPLATE,
                to=os.getenv('FACEBOOK_CLOUD_TEST_TO')
            ),
            object_data=TemplateObject(
                name="hello_world",
                language={
                    "code": "en_US"
                }
            )
        )
        self.assertIs(response.status_code, 200)
        response.close()


if __name__ == '__main__':
    unittest.main()
