from hondex_scrap import ScrapJob

class BSScrapper(ScrapJob):
    def __init__(self, **kwargs) -> None:
        super().__init__("Battlesuits", "battlesuit", **kwargs)

    def parse_unit(self, unit: str):
        dict_data, page = super().parse_unit(unit)
        
        dict_data = self._filter_dict(
            dict_data,
            ["character", "battlesuit", "version", "rank", "type", "core_strengths",
            "leader", "leaderEffect", 
            "special", "specialEffect", 
            "passive", "passiveEffect",
            "ultimate", "ultimateEffect",
            "evasion", "evasionEffect",
            "basic", "basicEffect",
            "profile","core"
            ]
        )
        if not self._must_haves(dict_data, ["character", "battlesuit", "version", "rank", "type", "core_strengths"]):
            return None
        
        dict_data["name"] = dict_data.pop("battlesuit")
        return dict_data


def run_scrap(**kwargs):
    scrapper = BSScrapper(**kwargs)
    return scrapper.run_job()