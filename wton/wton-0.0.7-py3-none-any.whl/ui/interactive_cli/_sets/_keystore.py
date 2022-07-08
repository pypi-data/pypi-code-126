import os
from collections import OrderedDict
import inquirer

from wton.tonclient.utils import Whitelist
from wton.tonsdk.contract.wallet import SendModeEnum, WalletVersionEnum, Wallets
from wton.utils import storage
from ._base import BaseSet
from ..._utils import SharedObject, md_table
from .._utils import echo_success, echo_error
from wton.tonsdk.utils import Address


class KeystoreSet(BaseSet):
    def __init__(self, ctx: SharedObject, keystore_name: str) -> None:
        super().__init__(ctx)
        ctx.keystore = ctx.keystores.get_keystore(
            keystore_name, raise_none=True)
        ctx.whitelist = Whitelist(
            ctx.config.wton.whitelist_path)

    def _handlers(self) -> OrderedDict:
        ord_dict = OrderedDict()
        ord_dict["List wallets"] = self._handle_list_wallets
        ord_dict["Transfer"] = self._handle_transfer
        ord_dict["Create wallet"] = self._handle_create_wallet
        ord_dict["Init wallet"] = self._handle_init_wallet
        ord_dict["Get wallet"] = self._handle_get_wallet
        ord_dict["Edit wallet"] = self._handle_edit_wallet
        ord_dict["Delete wallet"] = self._handle_delete_wallet
        ord_dict["Reveal wallet mnemonics"] = self._handle_reveal_wallet_mnemonics
        ord_dict["Import from mnemonics"] = self._handle_import_from_mnemonics
        ord_dict["Wallet to .addr and .pk"] = self._handle_wallet_to_addr_pk
        ord_dict["Backup keystore"] = self._handle_backup_keystore
        ord_dict["Back"] = self._handle_exit
        return ord_dict

    def _handle_list_wallets(self):
        questions = [
            inquirer.Confirm(
                "verbose", message='Show verbose information?', default=True),
        ]
        verbose = self._prompt(questions)["verbose"]

        field_names = ['Name', 'Version', 'WC', 'Address', 'Comment']
        if verbose:
            field_names += ['State', 'Balance']

        wallets = self.ctx.keystore.records

        table = md_table()
        table.field_names = field_names
        if verbose:
            wallet_infos = self.ctx.ton_client.get_addresses_information(
                [wallet.address for wallet in wallets])

            for wallet, wallet_info in zip(wallets, wallet_infos):
                table.add_row([wallet.name, wallet.version, wallet.workchain,
                               wallet.address_to_show, wallet.comment,
                               wallet_info.state, wallet_info.balance])
        else:
            for wallet in wallets:
                table.add_row([wallet.name, wallet.version, wallet.workchain,
                               wallet.address_to_show, wallet.comment])

        echo_success(table, only_msg=True)

    def _handle_transfer(self):
        from_wallet = self.__select_wallet_or_false("Transfer from")
        if from_wallet == False:
            return
        questions = [
            inquirer.Password("keystore_password",
                              message='Keystore password'),
        ]
        keystore_password = self._prompt(questions)["keystore_password"]
        record = self.ctx.keystore.get_record_by_name(
            from_wallet, raise_none=True)
        mnemonics = self.ctx.keystore.get_secret(
            record, keystore_password).split(" ")

        to_contact = self.__select_contact_or_false("Send to")
        if to_contact == False:
            return
        contact = self.ctx.whitelist.get_contact(
            to_contact, raise_none=True)

        questions = [
            inquirer.Text("amount", message='Amount to transfer (TON coins)'),
            inquirer.Text(
                "message", message='Message (press \'Enter\' to skip)'),
            inquirer.Confirm(
                "destroy_if_zero", message='Destroy if zero?', default=False),
            inquirer.Confirm(
                "transfer_all", message='Transfer all?', default=False),
        ]
        ans = self._prompt(questions)

        amount = float(ans["amount"])
        message = ans["message"]
        destroy_if_zero = ans["destroy_if_zero"]
        transfer_all = ans["transfer_all"]
        send_mode = SendModeEnum.ignore_errors | SendModeEnum.pay_gas_separately
        if destroy_if_zero:
            send_mode |= SendModeEnum.destroy_account_if_zero
        if transfer_all:
            send_mode |= SendModeEnum.carry_all_remaining_balance

        _mnemonics, _pub_k, _priv_k, wallet = Wallets.from_mnemonics(mnemonics, record.version,
                                                                     record.workchain)

        result = self.ctx.ton_client.transfer(
            wallet, contact.address, amount, message, send_mode)

        echo_success(result)

    def _handle_create_wallet(self):
        questions = [
            inquirer.List(
                "version", message='Wallet version', choices=[e.value for e in WalletVersionEnum], carousel=True),
            inquirer.Text(
                "workchain", message='Workchain'),
            inquirer.Text("name", message='Wallet name'),
            inquirer.Text(
                "comment", message='Wallet description (leave blank to skip)'),
            inquirer.Text(
                "contact_name", message='Enter name to save to whitelist (leave blank to skip)'),
        ]
        ans = self._prompt(questions)

        name = ans["name"]
        version = WalletVersionEnum(ans["version"])
        workchain = int(ans["workchain"])
        comment = ans["comment"]
        contact_name = ans["contact_name"]

        if contact_name:
            contact = self.ctx.whitelist.get_contact(contact_name)
            if contact is not None:
                raise Exception(
                    f"Contact with the name '{contact_name}' already exists")

        mnemonics, pub_k, _priv_k, wallet = Wallets.create(version, workchain)
        self.ctx.keystore.add_record(name, wallet.address,
                                     pub_k.hex(), mnemonics, version,
                                     workchain, comment, save=True)

        if contact_name:
            self.ctx.whitelist.add_contact(
                contact_name, wallet.address.to_string(True), save=True)

        echo_success()

    def _handle_init_wallet(self):
        wallet_name_to_init = self.__select_wallet_or_false("Wallet to init")
        if wallet_name_to_init == False:
            return
        questions = [
            inquirer.Password("keystore_password",
                              message='Keystore password'),
        ]
        keystore_password = self._prompt(questions)["keystore_password"]
        record = self.ctx.keystore.get_record_by_name(
            wallet_name_to_init, raise_none=True)
        mnemonics = self.ctx.keystore.get_secret(
            record, keystore_password).split(" ")
        _mnemonics, _pub_k, _priv_k, wallet = Wallets.from_mnemonics(mnemonics, record.version,
                                                                     record.workchain)
        result = self.ctx.ton_client.deploy_wallet(wallet)
        echo_success(result)

    def _handle_get_wallet(self):
        wallet_name = self.__select_wallet_or_false("Get wallet")
        if wallet_name == False:
            return

        wallet = self.ctx.keystore.get_record_by_name(
            wallet_name, raise_none=True)

        questions = [
            inquirer.Confirm(
                "verbose", message='Show verbose information?', default=True),
        ]
        verbose = self._prompt(questions)["verbose"]

        addr = Address(wallet.address)

        if verbose:
            addr_info = self.ctx.ton_client.get_address_information(
                wallet.address)

        echo_success(
            f"Raw address: {addr.to_string(False, False, False)}", True)
        echo_success(
            f"Nonbounceable address: {addr.to_string(True, True, False)}", True)
        echo_success(
            f"Bounceable address: {addr.to_string(True, True, True)}", True)
        echo_success(f"Version: {wallet.version}", True)
        echo_success(f"Workchain: {wallet.workchain}", True)
        echo_success(f"Comment: {wallet.comment}", True)

        if verbose:
            echo_success("--- Verbose wallet information ---", True)
            for k, v in addr_info.dict().items():
                echo_success(str(k) + ': ' + str(v), True)

    def _handle_edit_wallet(self):
        wallet_name = self.__select_wallet_or_false("Edit wallet")
        if wallet_name == False:
            return

        questions = [
            inquirer.Text(
                "new_name", message='New wallet name (leave blank to skip)'),
            inquirer.Text(
                "new_comment", message='New wallet description (leave blank to skip)'),
        ]
        ans = self._prompt(questions)

        new_name = ans["new_name"]
        new_comment = ans["new_comment"]

        self.ctx.keystore.edit_record(
            wallet_name, new_name, new_comment, save=True)

        echo_success()

    def _handle_delete_wallet(self):
        wallet_name = self.__select_wallet_or_false("Delete wallet")
        if wallet_name == False:
            return
        questions = [
            inquirer.Confirm(
                "is_sure", message=f'Are you sure you want to delete {wallet_name} wallet?', default=False,)
        ]
        is_sure = self._prompt(questions)["is_sure"]

        if not is_sure:
            echo_success("Action canceled.", True)
            return

        self.ctx.keystore.delete_record(wallet_name, save=True)

        echo_success()

    def _handle_reveal_wallet_mnemonics(self):
        wallet_name = self.__select_wallet_or_false("Wallet to reveal")
        if wallet_name == False:
            return

        questions = [
            inquirer.Password("keystore_password",
                              message='Keystore password'),
        ]
        keystore_password = self._prompt(questions)["keystore_password"]

        record = self.ctx.keystore.get_record_by_name(
            wallet_name, raise_none=True)
        mnemonics = self.ctx.keystore.get_secret(record, keystore_password)
        echo_success(mnemonics)

    def _handle_import_from_mnemonics(self):
        questions = [
            inquirer.Text(
                "mnemonics", message="Mnemonic words (splited by space)"),
            inquirer.List(
                "version", message='Wallet version', choices=[e.value for e in WalletVersionEnum], carousel=True),
            inquirer.Text(
                "workchain", message='Workchain'),
        ]
        ans = self._prompt(questions)
        mnemonics = ans["mnemonics"].split(" ")
        version = WalletVersionEnum(ans["version"])
        workchain = int(ans["workchain"])

        mnemonics, pub_k, _priv_k, wallet = Wallets.from_mnemonics(
            mnemonics, version, workchain)

        questions = [
            inquirer.Text("name", message='Wallet name'),
            inquirer.Text(
                "comment", message='Wallet description (leave blank to skip)'),
            inquirer.Text(
                "contact_name", message='Enter name to save to whitelist (leave blank to skip)'),
        ]
        ans = self._prompt(questions)
        name = ans["name"]
        comment = ans["comment"]
        contact_name = ans["contact_name"]

        if contact_name:
            contact = self.ctx.whitelist.get_contact(contact_name)
            if contact is not None:
                raise Exception(
                    f"Contact with the name '{contact_name}' already exists")

        self.ctx.keystore.add_record(name, wallet.address,
                                     pub_k.hex(), mnemonics, version,
                                     workchain, comment, save=True)

        if contact_name:
            self.ctx.whitelist.add_contact(
                contact_name, wallet.address.to_string(True), save=True)

        echo_success()

    def _handle_wallet_to_addr_pk(self):
        wallet_name = self.__select_wallet_or_false("Wallet to use")
        if wallet_name == False:
            return
        questions = [
            inquirer.Text("destination_dir",
                          message='Directory path to export into'),
            inquirer.Password("keystore_password",
                              message='Keystore password'),
        ]
        ans = self._prompt(questions)
        destination_dir = ans["destination_dir"]
        keystore_password = ans["keystore_password"]

        record = self.ctx.keystore.get_record_by_name(
            wallet_name, raise_none=True)
        mnemonics = self.ctx.keystore.get_secret(
            record, keystore_password).split(" ")
        addr, pk = Wallets.to_addr_pk(mnemonics, record.version,
                                      record.workchain)
        addr_path = os.path.join(
            destination_dir, record.name + ".addr")
        pk_path = os.path.join(destination_dir, record.name + ".pk")
        storage.save_bytes(addr_path, addr)
        storage.save_bytes(pk_path, pk)
        echo_success()

    def _handle_backup_keystore(self):
        questions = [
            inquirer.Text("backup_file_path", message='Backup filepath'),
            inquirer.Password("keystore_password",
                              message='Keystore password'),
            inquirer.Confirm(
                "is_sure",
                message='Backup stores keys in UNENCRYPTED FORM. Are you sure want to export unencrypted keys to disk?',
                default=False),

        ]
        ans = self._prompt(questions)
        backup_file_path = ans["backup_file_path"]
        keystore_password = ans["keystore_password"]
        is_sure = ans["is_sure"]

        if not is_sure:
            echo_success("Action canceled.", True)
            return

        self.ctx.keystore.backup(
            backup_file_path, keystore_password)

        echo_success()

    def __select_wallet_or_false(self, message):
        if self.ctx.keystore.records:
            questions = [
                inquirer.List(
                    "wallet",
                    message=message,
                    choices=[record.name for record in self.ctx.keystore.records],
                    carousel=True
                )
            ]
            return self._prompt(questions)["wallet"]

        echo_success("You do not have any wallets yet.")
        return False

    def __select_contact_or_false(self, message):
        if self.ctx.whitelist.contacts:
            questions = [
                inquirer.List(
                    "contact",
                    message=message,
                    choices=[
                        record.name for record in self.ctx.whitelist.contacts],
                    carousel=True
                )
            ]
            return self._prompt(questions)["contact"]

        echo_success("You do not have any contacts yet.")
        return False
