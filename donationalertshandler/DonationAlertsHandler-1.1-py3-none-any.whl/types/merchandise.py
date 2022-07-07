import datetime
import typing


class Merchandise:
    def __init__(self,
                 id: int,
                 merchant: object,
                 identifier: str,
                 title: object,
                 is_active: int,
                 is_percentage: int,
                 currency: str,
                 price_user: int,
                 price_service: int,
                 url: typing.Union[str, None],
                 img_url: typing.Union[str, None],
                 end_at: typing.Union[str, None],
                 **kwargs
                 ):
        """

        :param id: Unique merchandise ID on DonationAlerts
        :param merchant: Object carrying identifier and name fields that contain information about the merchant
        :param identifier: Unique merchandise ID on the merchant's online store
        :param title: Object carrying merchandise's titles in different locales
        :param is_active: A flag indicating whether the merchandise is available for purchase or not
        :param is_percentage: A flag indicating whether the price_service and price_user parameters should be recognized as absolute values of the currency currency or as a percent of the sale's total
        :param currency: The currency code of the merchandise (ISO 4217 formatted)
        :param price_user: Amount of revenue added to streamer for each sale of the merchandise
        :param price_service: Amount of revenue added to DonationAlerts for each sale of the merchandise
        :param url: URL to the merchandise's web page. Or null if URL is not set
        :param img_url: URL to the merchandise's image. Or null if image is not set
        :param end_at: Date and time indicating when the merchandise becomes inactive (YYYY-MM-DD HH.MM.SS formatted). Or null if end date is not set
        """
        self.id = id
        self.merchant = merchant
        self.identifier = identifier
        self.title = title
        self.is_active = is_active
        self.is_percentage = is_percentage
        self.currency = currency
        self.price_user = price_user
        self.price_service = price_service
        self.url = url
        self.img_url = img_url
        date_format = "%Y-%m-%d %H:%M:%S"  # YYYY-MM-DD HH.MM.SS
        self.end_at = datetime.datetime.strptime(end_at, date_format) if end_at else None

    def __repr__(self):
        return str(self.__dict__)
