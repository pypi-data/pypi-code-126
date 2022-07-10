from abc import abstractmethod
import logging
import os
from time import sleep
import typing
from mediawiki import MediaWiki
import hondex_arch
import re
import orjson

class ScrapMeta(type):
    _media_wiki_url = "https://honkaiimpact3.fandom.com/api.php"
    _media_wiki_client = None

    def __call__(cls, *args, **kwds):

        if cls._media_wiki_client is None:
            cls._media_wiki_client = MediaWiki(
                url=ScrapMeta._media_wiki_url, 
                rate_limit=True
            )
        
        instance = super().__call__(*args, **kwds)
        return instance
        
class ScrapJob(metaclass=ScrapMeta):
    @property
    def _wiki(self) -> MediaWiki:
        return self.__class__._media_wiki_client

    def __init__(self, 
        category : str, 
        model : str, 
        get_jobs : bool = True,
        redo : bool = False,
        **kwargs
    ) -> None:
        self.category = category
        self.model = model
        self.json_data = hondex_arch.load_file(self.model)    

        self.all_jobs = []

        if get_jobs:
            tree = self._wiki.categorytree(category=self.category, depth=1) if get_jobs else {}
            category_data= tree.get(self.category, {})
            self.all_jobs = category_data.get("links", [])
        
        if get_jobs and not redo:
            for key in list(self.all_jobs):
                if key in self.json_data:
                    self.all_jobs.remove(key)

    @abstractmethod
    def parse_unit(self, unit: str, remove_html_tags : bool = True):
        try:
            wiki_page = self._wiki.page(title=unit, preload=True)
        except:
            return None, None
        
        CLEANR = re.compile('<.*?>')

        wikitexts = wiki_page.wikitext.split("|")
        wikitexts = [x.replace("\n","") for x in wikitexts]
        wikidicts = {}
        for block in wikitexts:
            if "=" not in block:
                continue
            key, value = block.split("=", 1)
            
            if remove_html_tags:
                value = re.sub(CLEANR, '', value)

            value = value.replace("{", "")
            value = value.replace("}", "")
            value = value.replace("'''", "")

            wikidicts[key.strip()] = value.strip()

        return wikidicts, wiki_page

    def _filter_dict(self, dict_data : dict, *args, reverse : bool = False, must_exist : bool = False):
        if len(args) == 0:
            return dict_data
        
        if len(args) == 1 and isinstance(args[0], (list, set, tuple)):
            args = args[0]
        
        if must_exist and not any(key not in dict_data for key in args):
            return None

        if reverse:
            return {key: value for key, value in dict_data.items() if key not in args}

        return {key: value for key, value in dict_data.items() if key in args}

    def _must_haves(self, dict_data : dict, *args, reverse : bool = False):
        if len(args) == 0:
            return False

        if len(args) == 1 and isinstance(args[0], (list, set, tuple)):
            args = args[0]

        if reverse:
            return all(key not in dict_data for key in args)

        return all(key in dict_data for key in args)

    def _parse_value(self, val, match_val : typing.Callable, convert_val : typing.Callable):
        if val is None:
            return None

        if match_val(val):
            return convert_val(val)
        
        return val

    def add_job(self, unit : str, force : bool = False):
        if unit in self.json_data and not force:
            return False
        
        if unit in self.all_jobs:
            return True
        
        self.all_jobs.append(unit)

        return True

    def run_job(self, path : str = None, interval : float = 3, **kwargs):
        if path is not None and not os.path.isfile(path):
            raise ValueError(f"{path} is not a file")

        logging.info(f"Starting {self.model}")
        logging.info(f"{len(self.all_jobs)} jobs to scrape")
        changes_counter = 0

        for unit in self.all_jobs:
            dict_data = self.parse_unit(unit)
            logging.info(f"Parsing {unit}")
            if dict_data is None:
                continue
            self.json_data[unit] = dict_data
            changes_counter += 1
            sleep(interval)
        
        if len(self.json_data) == 0:
            logging.info(f"No data to save")
            return False

        if changes_counter == 0:
            logging.info(f"No changes to save")
            return False
 
        try:
            with open(hondex_arch.get_file_path(self.model) if path is None else path, "wb") as f:
                f.write(orjson.dumps(self.json_data))       
        except:
            raise
    
        return True

    @staticmethod
    def run_all_scraps():
        changes :bool = False
        import importlib
        # get parent dir
        parent_dir = os.path.dirname(os.path.abspath(__file__))
        # get all files in parent dir
        files = os.listdir(parent_dir)
        # filter out all files that are not scrap classes
        files = [x for x in files if x.endswith(".py") and not x.startswith("_")]
        for file in files:
            # remove .py
            file = file[:-3]
            # import module
            module = importlib.import_module(f"hondex_scrap.{file}")
            if not hasattr(module, "run_scrap"):
                logging.info(f"{file} does not have a run_scrap function")

            changes = module.run_scrap() or changes
    
        return changes