from hondex_scrap import ScrapJob

OBTAIN_METHODS = [
    "obtainStory", 
    "obtainEvents", 
    "obtainFoundry", 
    "obtainExchange", 
    "obtainDorm", 
    "obtainSupply", 
]


class StigScrapper(ScrapJob):
    def __init__(self, **kwargs) -> None:
        super().__init__("Stigmata", "stigmataSet", **kwargs)
    
    def _parse_imgs(self, page, name):
        img_links = page.images

        data = {}
        suspect_icons = []
        suspect_imgs = []
        for link in img_links:
            if name not in link:
                continue
            if "png" not in link:
                continue

            if "Icon" in link:
                suspect_icons.append(link)
            else:
                suspect_imgs.append(link)

        for link in suspect_icons:
            if link.split("%28")[1][0] == "T":
                data["icon_t"] = link
            elif link.split("%28")[1][0] == "M":
                data["icon_m"] = link
            elif link.split("%28")[1][0] == "B":
                data["icon_b"] = link

        for link in suspect_imgs:
            if link.split("%28")[1][0] == "T":
                data["img_t"] = link
            elif link.split("%28")[1][0] == "M":
                data["img_m"] = link
            elif link.split("%28")[1][0] == "B":
                data["img_b"] = link

        return data


    def parse_unit(self, unit: str):
        dict_data, page = super().parse_unit(unit)

        if dict_data is None:
            return None

        for key, val in dict_data.items():
            if val == "no" or val == "yes":
                dict_data[key] = val == "yes"
                continue

            val = val.replace("{{star}}", "*")
            
            dict_data[key] = val

        data = dict_data
        dict_data = {}
        obtain_methods = []

        if not self._must_haves(data, ["name", "rarity"]):
            return None

        data = self._filter_dict(data, 
            ["name", 
            "rarity", 
            "version", 
            "obtainStory", 
            "obtainEvents", 
            "obtainFoundry", 
            "obtainExchange", 
            "obtainDorm", 
            "obtainSupply", 
            "slotT_effect",
            "slotM_effect",
            "slotB_effect",
            "setEffect2p",
            "setEffect3p"]
        )

        for key, val in data.items():
            if key in OBTAIN_METHODS and self._parse_value(
                val, lambda x: x == "yes" or x == "no", 
                lambda x: x == "yes"
            ):
                obtain_methods.append(key[6:])
                continue
            elif key in OBTAIN_METHODS:
                continue

            dict_data[key] = val
        
        dict_data.update(**self._parse_imgs(page, unit))
        dict_data["obtain"] = obtain_methods

        return dict_data

def run_scrap(**kwargs):
    s = StigScrapper(**kwargs)
    return s.run_job(**kwargs)