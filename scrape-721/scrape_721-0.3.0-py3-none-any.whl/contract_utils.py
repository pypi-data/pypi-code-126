import os

from dotenv import load_dotenv
from scrape_721.constants import ERC_165_ABI, ERC_721_INTERFACE_ID
from web3 import Web3

load_dotenv()
w3_global = None


def configure(rpc_url: str | None = None):
    global w3_global

    w3_global = (
        Web3(Web3.HTTPProvider(rpc_url))
        if rpc_url is not None
        else Web3(Web3.HTTPProvider(os.environ["RPC_URL"]))
    )


def is_contract(address, w3=None, block=None):
    if w3 is None:
        w3 = w3_global

    address = w3.toChecksumAddress(address)
    code = (
        w3.eth.get_code(address) if block is None else w3.eth.get_code(address, block)
    )

    return True if code != b"" else False


def supports_erc_721(address, w3=None):
    if w3 is None:
        w3 = w3_global

    address = w3.toChecksumAddress(address)
    contract_erc_165 = w3.eth.contract(address=address, abi=ERC_165_ABI)

    try:
        return contract_erc_165.functions.supportsInterface(ERC_721_INTERFACE_ID).call()
    except:
        return False


def find_contract_deploy(address, w3=None, start_block=0, end_block=None):
    if w3 is None:
        w3 = w3_global

    if end_block is None:
        end_block = w3.eth.get_block_number()

    mid_block = ((end_block - start_block) // 2) + start_block
    is_contract_at_mid = is_contract(address, w3, mid_block)

    if mid_block == start_block:
        if is_contract_at_mid:
            return start_block
        else:
            if is_contract(address, w3, end_block):
                return end_block
            else:
                raise Exception("Could not find contract deploy")

    if is_contract_at_mid:
        return find_contract_deploy(address, w3, start_block, mid_block)
    else:
        return find_contract_deploy(address, w3, mid_block, end_block)
