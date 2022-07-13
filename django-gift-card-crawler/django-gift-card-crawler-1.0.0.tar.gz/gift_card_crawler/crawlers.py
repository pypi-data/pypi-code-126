import abc
import json
import time
from urllib.parse import urlparse, parse_qs

import requests
from bs4 import BeautifulSoup
from django.core.exceptions import ValidationError


class BaseCrawler(metaclass=abc.ABCMeta):

    def __init__(self, **kwargs):
        time.sleep(2)  # set time sleep

        self.link = kwargs.get('link')
        self.code = kwargs.get('code')

    @abc.abstractmethod
    def crawl(self):
        """
        send request to self.link to get page info then parse the html and extract code and serial
        """
        pass


class EGiftActivationSpot(BaseCrawler):
    def crawl(self):
        response = requests.get(self.link)
        soup = BeautifulSoup(response.text, "lxml")

        # parse price
        price = soup.select_one(selector="#amount").getText()

        # parse card number
        card_number = soup.select_one(selector="#cardNumber2").getText()

        # parse serial number
        serial_number_p = soup.select_one(selector=".gcmTerms").find_all('p').pop()
        serial_number = serial_number_p.getText()
        if serial_number.find("Serial number:") >= 0:
            serial_number = serial_number.replace("Serial number:", "")

        result = [{
            'link': self.link,
            'price': price.strip()[1:],
            'card_number': card_number.strip(),
            'serial_number': serial_number.strip(),
        }]

        return result, None


class ClaimEGifterRewards(BaseCrawler):
    base_url = 'https://claim.egifterrewards.com/api/claim/lineitem'

    def __init__(self, **kwargs):
        super(ClaimEGifterRewards, self).__init__(**kwargs)

        parsed_url = urlparse(self.link)
        url_params = parse_qs(parsed_url.query)

        try:
            self.item_id = url_params['lineItemId'][0]
            self.token = parsed_url.path.split('/').pop()
        except Exception as e:
            raise ValidationError('Error Occurred. Bad request. Please check the link.')

        self.headers = {'Content-Type': 'application/json'}

    def crawl(self):
        auth, error = self.authentication()
        if not auth:
            return None, error

        url = '{base_url}/{item_id}?token={token}'.format(base_url=self.base_url, item_id=self.item_id,
                                                          token=self.token)
        response = requests.get(url, headers={'Cookie': auth.headers.get('Set-Cookie')})
        if response.status_code != 200:
            return None, response.text

        result = []
        data = response.json()
        for info in data.get('Codes'):
            result.append({
                'link': self.link,
                'password': self.code,
                'price': info.get('Value'),
                'card_number': info.get('Code'),
                'serial_number': info.get('Pin'),
            })

        return result, None

    def authentication(self):
        url = "{base_url}/{item_id}/challenge?token={token}".format(base_url=self.base_url, item_id=self.item_id,
                                                                    token=self.token)
        payload = json.dumps({"Token": self.code.lower()})
        response = requests.post(url, data=payload, headers=self.headers)
        if response.status_code != 200:
            return None, response.text

        return response, None

