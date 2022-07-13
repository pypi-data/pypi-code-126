from collections import defaultdict
import json
from typing import List, Union
from collections.abc import Mapping
from pathlib import Path
import pandas as pd

def clean_concepts_from_dataset(dataset):
    return dataset.map(lambda i: {'entities' : { k:v for k, v in i['entities'].items() if k in ["id", "spans_start", "spans_end", "text"]}})

def create_flat_term_dict(concept_names_jsonl : List[Union[str, Path]], mappers : List[Mapping] = None):
    term_dict = []
    if not mappers:
        mappers = [lambda x: x] * len(concept_names_jsonl)
    assert len(mappers) == len(concept_names_jsonl)
    for jsonl_file, mapper in zip(concept_names_jsonl, mappers):
        with open(jsonl_file) as f:
            for entry in f:
                entry = json.loads(entry)
                if mapper != None:
                    entry = mapper(entry)
                    if not entry:
                        continue
                if type(entry) != list:
                    entry = [entry]
                for e in entry:
                    assert e['canonical_name']
                    cui = e['concept_id']
                    tuis = e['types']
                    term_dict.append({
                        'cui' : str(cui), 
                        'term' : e['canonical_name'],
                        'canonical' : e['canonical_name'],
                        'tuis' : tuis
                        }
                    )
                    for alias in e['aliases']:
                        term_dict.append({
                            'cui' : str(cui), 
                            'term' : alias,
                            'canonical' : e['canonical_name'],
                            'tuis' : tuis
                            }
                        )
    term_dict = pd.DataFrame(term_dict)
    return term_dict.drop_duplicates(subset=['cui', 'term'])

class Concept():

    def __init__(self, db_id : str = None, score : float = None, db_name : str = None, type : str = None):
        self._dict = {
            "db_id": db_id,
            "target_kb": db_name,
            "type": type,
            "score": score,
        }

class Entity():

    def __init__(self, offsets, text : Union[str, List[str]], id : str = "1", entity_type : str = None, concepts : List[Concept] = None):
        self._dict = {
            "id": id,
            "text": [text] if type(text) == str else text,
            "offsets": offsets,
            "type" : entity_type,
            "normalized": [c._dict for c in concepts] if concepts else []
        }


def make_document(entities : List[Entity], document_id : str ="1", corpus_id : str = "x") -> dict:
    return { "corpus_id" : corpus_id, "document_id" : document_id, "entities" : [e._dict for e in entities]}