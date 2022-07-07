import requests
from requests import HTTPError
from .base import BaseClient
from .exceptions import ClientAPIException, ClientNotFoundError


class RemoteIdentificationClient(BaseClient):
    ROUTE_CUSTOMER_INFO = 'customer-info'
    ROUTE_CUSTOMER_PASSPORT = 'customer-photo'
    ROUTE_CUSTOMER_SELFIE = 'customer-selfie'

    def get_user(
            self,
            phone: str,
            do_print: bool = True
    ) -> dict:
        """
            Вытаскивает данные пользователя с УИ,
            если не найдено кидает ошибку ClientNotFoundError
        """
        phone = self._strip_phone(phone)
        data = self._request('get', f'{self.ROUTE_CUSTOMER_INFO}/{phone}', {}, do_print)
        return self._check_data_with_status(data)

    def get_passport_photos(
            self,
            phone,
            do_print: bool = True
    ) -> dict:
        """
            Вытаскивает фото паспорта (passportForwardPhoto, passportBackPhoto, facePhoto),
            если не найдено кидает ошибку ClientNotFoundError
        """
        phone = self._strip_phone(phone)
        data = self._request('get', f'{self.ROUTE_CUSTOMER_PASSPORT}/{phone}', {}, do_print)
        return self._check_data_with_status(data)

    def get_selfie(
            self,
            phone,
            do_print: bool = True
    ) -> str:
        """
            Вытаскивает селфи с УИ, если не найдено кидает ошибку ClientNotFoundError
        """
        phone = self._strip_phone(phone)
        data = self._request('get', f'{self.ROUTE_CUSTOMER_SELFIE}/{phone}', {}, do_print)
        return self._check_data_with_status(data).get('selfie')

    @staticmethod
    def _check_data_with_status(data) -> dict:
        if data.get('status', None):
            if data['status'] == 1:
                return data
        raise ClientNotFoundError(404, 'Не найдено')

    def _request(self, method, route, data, do_print=True, headers=None):
        if not headers:
            headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        headers.update({"holy": self._token})

        response = None
        try:
            response = requests.request(
                method,
                self._build_absolute_url(route, data),
                headers=headers
            )
        except HTTPError:
            raise ClientAPIException(response.status_code, response.text)
        self._checker_response(response)

        if do_print:
            print(response.json())
        return response.json()
