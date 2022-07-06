from . import core_interface
from .rules.rules_manager import RulesManager


def start():
    rules = core_interface.login()
    # TODO features and hooks will be received from core need to process features
    if isinstance(rules, dict):
        rules_manager = RulesManager(rules['hooks'])
        rules_manager.apply_rules()


def stop():
    core_interface.stop()


start()
