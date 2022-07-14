from typing import Any, Dict, List, Optional

from settrade.util import response_to_dict

from .context import Context, Option


class _BaseEquity:
    def __init__(self, context: Context):
        self._ctx = context


class InvestorEquity(_BaseEquity):
    def __init__(self, context: Context, account_no: str):
        super().__init__(context)
        self._account_no = account_no
        self.base_url = (
            f"{self._ctx.base_url}/api/seos/v3/{self._ctx.broker_id}/accounts"
        )

    def get_account_info(self) -> Dict[str, Any]:
        path = f"{self.base_url}/{self._account_no}/account-info"
        response = self._ctx.dispatch(Option("GET", path))
        return response_to_dict(response)

    def get_order(self, order_no: str) -> Dict[str, Any]:
        path = f"{self.base_url}/{self._account_no}/orders/{order_no}"
        response = self._ctx.dispatch(Option("GET", path))
        return response_to_dict(response)

    def get_orders(self) -> List[Dict[str, Any]]:
        path = f"{self.base_url}/{self._account_no}/orders"
        response = self._ctx.dispatch(Option("GET", path))
        return response_to_dict(response)  # type: ignore

    def get_portfolios(self) -> List[Dict[str, Any]]:
        path = f"{self.base_url}/{self._account_no}/portfolios"
        response = self._ctx.dispatch(Option("GET", path))
        return response_to_dict(response)  # type: ignore

    def get_trades(self) -> List[Dict[str, Any]]:
        path = f"{self.base_url}/{self._account_no}/trades"
        response = self._ctx.dispatch(Option("GET", path))
        return response_to_dict(response)  # type: ignore

    def place_order(
        self,
        pin: str,
        side: str,
        symbol: str,
        trustee_id_type: str,
        volume: int,
        qty_open: int,
        price: float,
        price_type: str,
        validity_type: str,
        client_type: str,
        bypass_warning: bool,
        valid_till_date: str,
    ) -> Dict[str, Any]:
        path = f"{self.base_url}/{self._account_no}/orders"
        body = {
            "side": side,
            "symbol": symbol,
            "trusteeIdType": trustee_id_type,
            "volume": volume,
            "qtyOpen": qty_open,
            "price": price,
            "priceType": price_type,
            "validityType": validity_type,
            "clientType": client_type,
            "bypassWarning": bypass_warning,
            "validTillDate": valid_till_date,
            "pin": pin,
        }
        response = self._ctx.dispatch(
            Option(method="POST", endpoint=path, payload=body)
        )
        return response_to_dict(response)

    def change_order(
        self,
        order_no: str,
        new_trustee_id_type: str,
        new_price: Optional[float],
        new_volume: int,
        bypass_warning: bool,
        pin: str,
        new_iceberg_volume: Optional[int],
    ):
        path = f"{self.base_url}/{self._account_no}/orders/{order_no}/change"
        body = {
            "newTrusteeIdType": new_trustee_id_type,
            "pin": pin,
            "newPrice": new_price,
            "newVolume": new_volume,
            "newIcebergVolume": new_iceberg_volume,
            "bypassWarning": bypass_warning,
        }
        response = self._ctx.dispatch(
            Option(method="PATCH", endpoint=path, payload=body)
        )
        return response_to_dict(response)

    def cancel_order(self, order_no: str, pin: str):
        path = f"{self.base_url}/{self._account_no}/orders/{order_no}/cancel"
        body = {
            "pin": pin,
        }
        response = self._ctx.dispatch(
            Option(method="PATCH", endpoint=path, payload=body)
        )
        return response_to_dict(response)

    def cancel_orders(self, order_no_list: List[str], pin: str) -> Dict[str, Any]:
        path = f"{self.base_url}/{self._account_no}/cancel"
        body = {
            "pin": pin,
            "orders": order_no_list,
        }
        response = self._ctx.dispatch(
            Option(method="PATCH", endpoint=path, payload=body)
        )
        return response_to_dict(response)


class MarketRepEquity(_BaseEquity):
    def __init__(self, context: Context):
        super().__init__(context)
        self.base_url = f"{self._ctx.base_url}/api/seos/v3/{self._ctx.broker_id}/mktrep"

    def get_account_info(self, account_no: str) -> Dict[str, Any]:
        path = f"{self.base_url}/accounts/{account_no}/account-info"
        response = self._ctx.dispatch(Option("GET", path))
        return response_to_dict(response)

    def get_order(self, order_no: str) -> Dict[str, Any]:
        path = f"{self.base_url}/orders/{order_no}"
        response = self._ctx.dispatch(Option("GET", path))
        return response_to_dict(response)

    def get_orders(self) -> List[Dict[str, Any]]:
        path = f"{self.base_url}/orders"
        response = self._ctx.dispatch(Option("GET", path))
        return response_to_dict(response)  # type: ignore

    def get_orders_by_account_no(self, account_no: str) -> List[Dict[str, Any]]:
        path = f"{self.base_url}/accounts/{account_no}/orders"
        response = self._ctx.dispatch(Option("GET", path))
        return response_to_dict(response)  # type: ignore

    def get_portfolios(self, account_no: str) -> List[Dict[str, Any]]:
        path = f"{self.base_url}/accounts/{account_no}/portfolios"
        response = self._ctx.dispatch(Option("GET", path))
        return response_to_dict(response)  # type: ignore

    def get_trades(self, account_no: str) -> List[Dict[str, Any]]:
        path = f"{self.base_url}/accounts/{account_no}/trades"
        response = self._ctx.dispatch(Option("GET", path))
        return response_to_dict(response)  # type: ignore

    def place_order(
        self,
        account_no: str,
        side: str,
        symbol: str,
        trustee_id_type: str,
        volume: int,
        qty_open: int,
        price: float,
        price_type: str,
        validity_type: str,
        client_type: str,
        bypass_warning: bool,
        valid_till_date: str,
    ) -> Dict[str, Any]:
        path = f"{self.base_url}/accounts/{account_no}/orders"
        body = {
            "side": side,
            "symbol": symbol,
            "trusteeIdType": trustee_id_type,
            "volume": volume,
            "qtyOpen": qty_open,
            "price": price,
            "priceType": price_type,
            "validityType": validity_type,
            "clientType": client_type,
            "bypassWarning": bypass_warning,
            "validTillDate": valid_till_date,
        }
        response = self._ctx.dispatch(
            Option(method="POST", endpoint=path, payload=body)
        )
        return response_to_dict(response)

    def change_order(
        self,
        account_no: str,
        order_no: str,
        new_account_no: Optional[str],
        new_trustee_id_type: Optional[str],
        new_price: Optional[float],
        new_volume: Optional[int],
        bypass_warning: Optional[bool],
        new_iceberg_volume: Optional[int],
    ):
        path = f"{self.base_url}/accounts/{account_no}/orders/{order_no}/change"
        body = {
            "newAccountNo": new_account_no,
            "newTrusteeIdType": new_trustee_id_type,
            "newPrice": new_price,
            "newVolume": new_volume,
            "newIcebergVolume": new_iceberg_volume,
            "bypassWarning": bypass_warning,
        }
        response = self._ctx.dispatch(
            Option(method="PATCH", endpoint=path, payload=body)
        )
        return response_to_dict(response)

    def cancel_order(self, account_no: str, order_no: str):
        path = f"{self.base_url}/accounts/{account_no}/orders/{order_no}/cancel"
        body = {}
        response = self._ctx.dispatch(
            Option(method="PATCH", endpoint=path, payload=body)
        )
        return response_to_dict(response)

    def cancel_orders(
        self, account_no: str, order_no_list: List[str]
    ) -> Dict[str, Any]:
        path = f"{self.base_url}/accounts/{account_no}/cancel"
        body = order_no_list
        response = self._ctx.dispatch(
            Option(method="PATCH", endpoint=path, payload=body)
        )
        return response_to_dict(response)
