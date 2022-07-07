import typing
import datetime


class Donations:
    def __init__(self, id: int,
                 name: str,
                 username: str,
                 message_type: str,
                 message: str,
                 amount: int,
                 currency: str,
                 is_shown: str,
                 created_at: str,
                 shown_at: typing.Union[str, None],
                 **kwargs
                 ):
        """
        Obtains array of objects of user donation alerts list. Requires user authorization with the oauth-donation-index scope

        :param id: The unique donation alert identifier
        :param name: Type of the alert. Always donation in this case
        :param username: The name of the user who sent the donation and the alert
        :param message_type: The message type. The possible values are text for a text messages and audio for an audio messages
        :param message: The message sent along with the donation and the alert
        :param amount: The donation amount
        :param currency: The currency code (ISO 4217 formatted)
        :param is_shown: A flag indicating whether the alert was shown in the streamer's widget
        :param created_at: The donation date and time (YYYY-MM-DD HH.MM.SS formatted)
        :param shown_at: Date and time indicating when the alert was shown (YYYY-MM-DD HH.MM.SS formatted). Or null if the alert is not shown yet
        """

        self.id = id
        self.name = name
        self.username = username
        self.message_type = message_type
        self.message = message
        self.amount = amount
        self.currency = currency
        self.is_shown = is_shown
        date_format = "%Y-%m-%d %H:%M:%S"  # YYYY-MM-DD HH.MM.SS
        self.created_at = datetime.datetime.strptime(created_at, date_format)
        self.shown_at = datetime.datetime.strptime(shown_at, date_format) if shown_at else None

    def __repr__(self):
        return str(self.__dict__)
