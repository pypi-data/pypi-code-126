from typing import Union
import datasets
from pathlib import Path
from itertools import groupby
import numpy as np

from bigbio.dataloader import BigBioConfigHelpers

conhelps = BigBioConfigHelpers()

data_dir = Path(__file__).parent

def _load_dataset(config_name : str, dataset_name : str, lang_mapper, splits):
    assert config_name and not dataset_name or dataset_name and not config_name
    if dataset_name:
        configs = conhelps.for_dataset(dataset_name).filtered(lambda conf: conf.is_bigbio_schema)
    else:
        configs = [conhelps.for_config_name(config_name)]
    ds_map = {c.config.name : c.load_dataset() for c in configs}
    ds = []
    for conf, ds_dict in ds_map.items():
        for k in ds_dict.keys():
            ds_dict[k] = ds_dict[k].add_column('corpus_id', [conf] * len(ds_dict[k]))
            ds_dict[k] = ds_dict[k].add_column('lang', [lang_mapper(conf)] * len(ds_dict[k]))
        ds.append(ds_dict)
    output = datasets.dataset_dict.DatasetDict()
    for s in splits:
        output[s] = datasets.concatenate_datasets([d[s] for d in ds])
    return output#.map(attribute_mapper)

def _merge_concepts_same_entity(ds):
    def _merge_entities(d):
        ents = d['entities']
        merged = []
        for k, grp in groupby(sorted(ents, key=lambda e: e['offsets'][0][0]), lambda e: (e['text'], e['offsets'])):
            grp = list(grp)
            normalized = []
            for e in grp:
                for n in e['normalized']:
                    if not n in normalized:
                        normalized.append(n)
            merged.append({
                'id' : '+'.join([e['id'] for e in grp]),
                'normalized' : normalized,
                'type' : [e['type'] for e in grp],
                'text' : k[0],
                'offsets' : k[1]
            })
        return { "entities" : merged }      
    return ds.map(_merge_entities)

def load_mantra_gsc(merge_concepts=True):
    ds = _load_dataset(
        None, 
        "mantra_gsc",
        lambda conf_name: conf_name.split("_")[2],
        splits = [ "train" ]
    )
    if merge_concepts:
        return _merge_concepts_same_entity(ds)
    else:
        return ds

def _load_medmentions(config_name, merge_concepts):
    def drop_prefix(entities):
        for e in entities:
            for n in e['normalized']:
                n['db_id'] = n['db_id'].replace('UMLS:', '')
        return entities

    ds =_load_dataset(
        config_name,
        None,
        lambda _: "en",
        splits = ["train", "validation", "test"],
    ).map(lambda d: {"entities" : drop_prefix(d['entities'])})
    if merge_concepts:
        return _merge_concepts_same_entity(ds)
    else:
        return ds
    
def load_medmentions_full(merge_concepts=True):
    return _load_medmentions("medmentions_full_bigbio_kb", merge_concepts)

def load_medmentions_st21pv(merge_concepts=True):
    return _load_medmentions("medmentions_st21pv_bigbio_kb", merge_concepts)

def load_quaero():
    return _load_dataset(
        None, 
        "quaero",
        lambda _: "fr",
        splits = [ "train", "validation", "test" ]
    )

def load_distemist_linking():
    return _load_dataset(        
        "distemist_linking_bigbio_kb",
        None,
        lambda _: "es",
        splits = ["train"]
    )

def load_bronco(bronco_150_xml_path : Union[Path, str]):
    pass#return load_dataset(str(data_dir / 'bronco'), bronco_150_xml_path = bronco_150_xml_path)