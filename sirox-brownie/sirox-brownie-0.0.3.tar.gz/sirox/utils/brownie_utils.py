import json

from brownie import Contract, network
from typing import List

from os import makedirs

ABI_BASE_PATH = "/tmp/sirox_brownie/abis"


def connect_to_chain(chain: str = "mainnet"):
    """
    Brownie wrapper to connect to given chain
    Expects INFURA_PROJECT_IDS environmental variable
    """
    try:
        network.connect(chain)
    except Exception as e:
        print(f"WARNING: {Exception} as {e}")


def create_dir(path):
    """Creates directories given in path"""
    makedirs(path, exist_ok=True)


def get_abis(addresses: List[str], base_path: str = ABI_BASE_PATH):
    """
    Leverages Contract class from Brownie to get ABI from Etherscan
    Expects ETHERSCAN_TOKEN environmental variable
    """

    print(f"Getting ABI for contracts: {addresses}")

    # Download only from mainnet
    connect_to_chain("mainnet")

    create_dir(base_path)

    for address in addresses:
        # Get contract from explorer
        contract = Contract.from_explorer(address)
        # Save abi from contract
        with open(f"{base_path}/{address.lower()}.json", "w") as file:
            file.write(json.dumps(contract.abi))

    print(f"Done!")
