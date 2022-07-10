from datetime import date
import json
import pandas
from quick_resto_API.quick_resto_objects.quick_resto_object import QuickRestoObject

from quick_resto_API.quick_resto_api import QuickRestoApi
from quick_resto_API.quick_resto_objects.modules.crm.account_type import AccountType
from quick_resto_API.quick_resto_objects.modules.crm.account_balance import AccountBalance
from quick_resto_API.quick_resto_objects.modules.crm.customer import CrmCustomer
from quick_resto_API.quick_resto_objects.modules.crm.customer_token import CustomerToken

class QuickRestoInterface:
    @property
    def api(self):
        return self._api

    def __init__(self, login: str, password: str, use_https: bool = True, layer: str = "quickresto.ru"):
        self._api: QuickRestoApi = QuickRestoApi(login, password, use_https, layer)
        self._ping()

    def _ping(self) -> None:
        # TODO: add good error message for this case
        self._api.get("ping")

    def crm_search_client(self, search: str) -> CrmCustomer:
        json_data = {
            "search": search
        }

        json_response = self._api.post("bonuses/filterCustomers", json_data=json_data).json()

        return CrmCustomer(**json_response)

    def crm_get_customer_info(self, customerToken: CustomerToken) -> CrmCustomer:
        json_data = {
            "customerToken": customerToken.get_json_object
        }

        json_response = self._api.post("bonuses/customerInfo", json_data=json_data).json()

        return CrmCustomer(**json_response)

    def crm_get_client_balance(self, customerToken: CustomerToken, accountType: AccountType) -> AccountBalance:
        json_data = {
            "customerToken": customerToken.get_json_object(),
            "accountType": accountType.get_json_object()
        }

        json_response = self._api.post("bonuses/balance", json_data=json_data).json()

        return AccountBalance(**json_response)

    def crm_get_operation_history(self, customerToken: CustomerToken) -> dict:
        json_data = {
            "customerToken": customerToken.get_json_object()
        }

        json_response = self._api.post("bonuses/operationHistory", json_data=json_data).json()

        return json_response

    def crm_create_customer(self, customer: CrmCustomer) -> CrmCustomer:
        json_data = customer.get_json_object()

        json_response = self._api.post("bonuses/createCustomer", json_data=json_data).json()

        return CrmCustomer(**json_response)

    def crm_depit_hold(self, customerToken: CustomerToken, amount: int, accountType: AccountType, date: date = None,
                       precheck: int = None) -> dict:
        json_data = {
            "customerToken": customerToken.get_json_object(),
            "date": date,
            "precheck": precheck,
            "amount": amount,
            "accountType": accountType.get_json_object(),
        }

        json_response = self._api.post("bonuses/debitHold", json_data=json_data).json()

        return json_response

    def crm_credit_hold(self, customerToken: CustomerToken, accountType: AccountType, amount: int, date: date = None,
                        precheck: int = None) -> dict:
        json_data = {
            "customerToken": customerToken.get_json_object(),
            "date": date,
            "precheck": precheck,
            "amount": amount,
            "accountType": accountType.get_json_object(),
        }

        json_response = self._api.post("bonuses/creditHold", json_data=json_data).json()

        return json_response

    def crm_reverse(self, customerToken: CustomerToken, accountType: AccountType, amount: int, bonusTransactionId: int,
                    date: date = None, precheck: int = None) -> dict:
        json_data = {
            "customerToken": customerToken.get_json_object(),
            "date": date,
            "precheck": precheck,
            "amount": amount,
            "accountType": accountType.get_json_object(),
            "bonusTransactionId": bonusTransactionId
        }

        json_response = self._api.post("bonuses/reverse", json_data=json_data).json()

        return json_response

    def create_csv_file(self, json_data:list|QuickRestoObject, file_name:str):
        file = file_name + ".csv"

        if isinstance(json_data, QuickRestoObject):
            pandas.DataFrame(json.loads(json.dumps(self._get_not_nested_json(json_data.get_json_object())))).to_csv(file)

        if isinstance(json_data, list):
            list_of_json_objects = list()

            for item in json_data:
                if isinstance(item, QuickRestoObject):
                    list_of_json_objects.append(self._get_not_nested_json(item.get_json_object()))

            pandas.DataFrame(json.loads(json.dumps(list_of_json_objects))).to_csv(file)

    def convert_to_csv(self, json_data:list|QuickRestoObject) -> str:
        if isinstance(json_data, QuickRestoObject):
            return pandas.DataFrame(json.loads(json.dumps(self._get_not_nested_json(json_data.get_json_object())))).to_csv()

        if isinstance(json_data, list):
            list_of_json_objects = list()

            for item in json_data:
                if isinstance(item, QuickRestoObject):
                    list_of_json_objects.append(self._get_not_nested_json(item.get_json_object()))

            return pandas.DataFrame(json.loads(json.dumps(list_of_json_objects))).to_csv()

        return ""

    def _get_not_nested_json(self, json:dict, result_json:dict = dict(), nested_names:list = list()) -> dict:
        for i in json.keys():
            if isinstance(json[i], dict):
                nested_names.append(i + "__")

                self._get_not_nested_json(json[i], result_json, nested_names)

                nested_names.pop()
            else:
                result_json["".join(nested_names) + i] =  json[i]

        return result_json
