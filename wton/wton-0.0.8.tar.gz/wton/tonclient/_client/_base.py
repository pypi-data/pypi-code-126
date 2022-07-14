from abc import ABC, abstractmethod
from typing import List, Optional

from pydantic import BaseModel

from wton.config import Config
from wton.tonsdk.utils import TonCurrencyEnum
from wton.tonsdk.contract.wallet import SendModeEnum, WalletContract


class AddressInfoResult(BaseModel):
    address: Optional[str] = None
    contract_type: Optional[str] = None
    seqno: Optional[str] = None
    state: Optional[str] = None
    balance: Optional[str] = None
    last_activity: Optional[str] = None
    code: Optional[str] = None
    data: Optional[str] = None


class TonClient(ABC):
    @abstractmethod
    def __init__(self, config: Config):
        raise NotImplementedError

    @abstractmethod
    def get_address_information(self, address: str,
                                currency_to_show: TonCurrencyEnum = TonCurrencyEnum.ton) -> AddressInfoResult:
        raise NotImplementedError

    @abstractmethod
    def get_addresses_information(self, addresses: List[str],
                                  currency_to_show: TonCurrencyEnum = TonCurrencyEnum.ton) -> List[AddressInfoResult]:
        raise NotImplementedError

    @abstractmethod
    def seqno(self, addr: str):
        raise NotImplementedError

    @abstractmethod
    def deploy_wallet(self, wallet: WalletContract, wait_for_result=False):
        raise NotImplementedError

    @abstractmethod
    def transfer(self, from_wallet: WalletContract, to_addr: str, amount: TonCurrencyEnum.ton, payload=None,
                 send_mode=SendModeEnum.ignore_errors | SendModeEnum.pay_gas_separately, wait_for_result=False) -> bool:
        raise NotImplementedError
