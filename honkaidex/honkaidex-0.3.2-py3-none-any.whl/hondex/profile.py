import hondex_arch

_JSON_LOAD = {}

def load_stigmata():
    from hondex_model.stigmataSet import StigmataSet
    if StigmataSet not in _JSON_LOAD:
        _JSON_LOAD[StigmataSet] = hondex_arch.load_file("stigmataSet")

    StigmataSet.from_json(_JSON_LOAD[StigmataSet])

def load_character():
    from hondex_model.character import Character
    if Character not in _JSON_LOAD:
        _JSON_LOAD[Character] = hondex_arch.load_file("character")

    Character.from_json(_JSON_LOAD[Character])

def load_battlesuits():
    load_character()

    from hondex_model.battlesuit import Battlesuit
    if Battlesuit not in _JSON_LOAD:
        _JSON_LOAD[Battlesuit] = hondex_arch.load_file("battlesuit")

    with_core_bs = {k : v for k, v in _JSON_LOAD[Battlesuit].items() if v.get("core", None) is not None}
    without_core_bs = {k : v for k, v in _JSON_LOAD[Battlesuit].items() if k not in with_core_bs}

    Battlesuit.from_json(without_core_bs)
    Battlesuit.from_json(with_core_bs)

def load_all():
    load_stigmata()
    load_battlesuits()