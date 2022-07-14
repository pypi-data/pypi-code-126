from typing import Any, Dict, List, Optional

from .context import Context, Option
from .util import response_to_dict


class _BaseDerivatives:
    def __init__(self, context: Context):
        self._ctx = context


class InvestorDerivatives(_BaseDerivatives):
    def __init__(self, context: Context, account_no: str):
        super().__init__(context)
        self._account_no = account_no
        self.base_url = (
            f"{self._ctx.base_url}/api/seosd/v3/{self._ctx.broker_id}/accounts"
        )

    def get_account_info(self) -> Dict[str, Any]:
        path = f"{self.base_url}/{self._account_no}/account-info"
        response = self._ctx.dispatch(Option("GET", path))
        return response_to_dict(response)

    def get_account_info_detail(self) -> Dict[str, Any]:
        path = f"{self.base_url}/{self._account_no}/account-info-detail"
        response = self._ctx.dispatch(Option("GET", path))
        return response_to_dict(response)

    def get_commission(self) -> Dict[str, Any]:
        path = f"{self.base_url}/{self._account_no}/commission"
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

    def get_portfolios(self) -> Dict[str, Any]:
        path = f"{self.base_url}/{self._account_no}/portfolios"
        response = self._ctx.dispatch(Option("GET", path))
        return response_to_dict(response)

    def get_trades(self) -> List[Dict[str, Any]]:
        path = f"{self.base_url}/{self._account_no}/trades"
        response = self._ctx.dispatch(Option("GET", path))
        return response_to_dict(response)  # type: ignore

    def get_trade_summaries(self) -> List[Dict[str, Any]]:
        path = f"{self.base_url}/{self._account_no}/trade-summaries"
        response = self._ctx.dispatch(Option("GET", path))
        return response_to_dict(response)  # type: ignore

    def place_order(
        self,
        symbol: str,
        side: str,
        position: str,
        price_type: str,
        price: float,
        volume: int,
        iceberg_vol: int,
        validity_type: str,
        validity_date_condition: Optional[str],
        stop_condition: Optional[str],
        stop_symbol: Optional[str],
        stop_price: Optional[float],
        trigger_session: Optional[str],
        bypass_warning: bool,
        pin: str,
    ) -> Dict[str, Any]:
        path = f"{self.base_url}/{self._account_no}/orders"
        body = {
            "symbol": symbol,
            "side": side,
            "position": position,
            "priceType": price_type,
            "price": price,
            "volume": volume,
            "icebergVol": iceberg_vol,
            "validityType": validity_type,
            "validityDateCondition": validity_date_condition,
            "stopCondition": stop_condition,
            "stopSymbol": stop_symbol,
            "stopPrice": stop_price,
            "triggerSession": trigger_session,
            "bypassWarning": bypass_warning,
            "pin": pin,
        }
        response = self._ctx.dispatch(
            Option(method="POST", endpoint=path, payload=body)
        )
        return response_to_dict(response)

    def place_orders(self, pin: str, order_list: List[dict]) -> Dict[str, Any]:
        path = f"{self.base_url}/{self._account_no}/orders/place-multiple"
        body = {
            "orders": order_list,
            "pin": pin,
        }
        response = self._ctx.dispatch(
            Option(method="POST", endpoint=path, payload=body)
        )
        return response_to_dict(response)

    def change_order(
        self,
        order_no: str,
        new_price: Optional[float],
        new_volume: int,
        bypass_warning: bool,
        pin: str,
    ):
        path = f"{self.base_url}/{self._account_no}/orders/{order_no}/change"
        body = {
            "newPrice": new_price,
            "newVolume": new_volume,
            "bypassWarning": bypass_warning,
            "pin": pin,
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


class MarketRepDerivatives(_BaseDerivatives):
    def __init__(self, context: Context):
        super().__init__(context)
        self.base_url = (
            f"{self._ctx.base_url}/api/seosd/v3/{self._ctx.broker_id}/mktrep"
        )

    def get_account_info(self, account_no: str) -> Dict[str, Any]:
        path = f"{self.base_url}/accounts/{account_no}/account-info"
        response = self._ctx.dispatch(Option("GET", path))
        return response_to_dict(response)

    def get_account_info_detail(self, account_no: str) -> Dict[str, Any]:
        path = f"{self.base_url}/accounts/{account_no}/account-info-detail"
        response = self._ctx.dispatch(Option("GET", path))
        return response_to_dict(response)

    def get_commission(self, account_no: str) -> Dict[str, Any]:
        path = f"{self.base_url}/accounts/{account_no}/commission"
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

    def get_portfolios(self, account_no: str) -> Dict[str, Any]:
        path = f"{self.base_url}/accounts/{account_no}/portfolios"
        response = self._ctx.dispatch(Option("GET", path))
        return response_to_dict(response)

    def get_trades(self, account_no: str) -> List[Dict[str, Any]]:
        path = f"{self.base_url}/accounts/{account_no}/trades"
        response = self._ctx.dispatch(Option("GET", path))
        return response_to_dict(response)  # type: ignore

    def get_trade_summaries(self, account_no: str) -> List[Dict[str, Any]]:
        path = f"{self.base_url}/accounts/{account_no}/trade-summaries"
        response = self._ctx.dispatch(Option("GET", path))
        return response_to_dict(response)  # type: ignore

    def place_order(
        self,
        account_no: str,
        symbol: str,
        side: str,
        position: str,
        price_type: str,
        price: float,
        volume: int,
        iceberg_vol: int,
        validity_type: str,
        validity_date_condition: Optional[str],
        stop_condition: Optional[str],
        stop_symbol: Optional[str],
        stop_price: Optional[float],
        trigger_session: Optional[str],
        bypass_warning: bool,
    ) -> Dict[str, Any]:
        path = f"{self.base_url}/accounts/{account_no}/orders"
        body = {
            "symbol": symbol,
            "side": side,
            "position": position,
            "priceType": price_type,
            "price": price,
            "volume": volume,
            "icebergVol": iceberg_vol,
            "validityType": validity_type,
            "validityDateCondition": validity_date_condition,
            "stopCondition": stop_condition,
            "stopSymbol": stop_symbol,
            "stopPrice": stop_price,
            "triggerSession": trigger_session,
            "bypassWarning": bypass_warning,
        }
        response = self._ctx.dispatch(
            Option(method="POST", endpoint=path, payload=body)
        )
        return response_to_dict(response)

    def place_orders(self, account_no: str, order_list: List[dict]) -> Dict[str, Any]:
        path = f"{self.base_url}/accounts/{account_no}/orders/place-multiple"
        body = {
            "orders": order_list,
        }
        response = self._ctx.dispatch(
            Option(method="POST", endpoint=path, payload=body)
        )
        return response_to_dict(response)

    def change_order(
        self,
        account_no: str,
        order_no: str,
        new_price: Optional[float],
        new_volume: int,
        bypass_warning: bool,
        new_account_no: Optional[str],
    ):
        path = f"{self.base_url}/accounts/{account_no}/orders/{order_no}/change"
        body = {
            "newPrice": new_price,
            "newVolume": new_volume,
            "bypassWarning": bypass_warning,
            "newAccountNo": new_account_no,
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
        response = self._ctx.dispatch(
            Option(method="PATCH", endpoint=path, payload=order_no_list)
        )
        return response_to_dict(response)

    def place_trade_report(
        self,
        buyer: str,
        seller: Optional[str],
        symbol: str,
        position: str,
        price: float,
        volume: int,
        cpm: str,
        ty_type: str,
        control_key: str,
    ):
        path = f"{self.base_url}/orders/tradeReport"
        body = {
            "buyer": buyer,
            "seller": seller,
            "symbol": symbol,
            "position": position,
            "price": price,
            "volume": volume,
            "cpm": cpm,
            "trType": ty_type,
            "controlKey": control_key,
        }
        response = self._ctx.dispatch(
            Option(method="POST", endpoint=path, payload=body)
        )
        return response_to_dict(response)
