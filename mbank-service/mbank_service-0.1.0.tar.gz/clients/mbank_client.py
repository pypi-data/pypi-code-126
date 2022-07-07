import requests
from requests import HTTPError
from clients.base import BaseClient
from clients.exceptions import ClientAPIException, ClientNotFoundError


class MBankClient(BaseClient):
    ROUTE_CHECK_MBANK = 'check'

    def _request(self, method, route, data, do_print=True, headers=None):
        if not headers:
            headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        headers.update({"authenticate": self._token})

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

    def check_mbank_exist(self, phone, do_print=True):
        """
            Проверяет наличие Мбанк по номеру телефона
            Check if payer exists
            field status of response json can be in two states:
            0 - payer exists in the system
            114 - payer not found
        """
        phone = self._strip_phone(phone)
        data = {'phone': phone}
        data = self._request('get', f'{self.ROUTE_CHECK_MBANK}', data, do_print)
        return self._check_data_with_code(data)

    @staticmethod
    def _check_data_with_code(data) -> dict:
        if 'code' in data:
            if data.get('code', 114) == 0:
                return data
        raise ClientNotFoundError(404, 'Не найдено')
