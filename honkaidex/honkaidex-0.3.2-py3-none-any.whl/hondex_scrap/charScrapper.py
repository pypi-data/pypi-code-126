from hondex_scrap import ScrapJob

class CharScrapper(ScrapJob):
    def __init__(self, **kwargs) -> None:
        super().__init__("Playable_Characters", "character", **kwargs)

    def parse_unit(self, unit: str):
        if "APHO" in unit:
            return None

        dict_data, page = super().parse_unit(unit)

        return self._filter_dict(dict_data,["name", "weight", "height"], must_exist=True)
        

def run_scrap(**kwargs):
    s = CharScrapper(**kwargs)
    return s.run_job(**kwargs)
    