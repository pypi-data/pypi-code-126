import pickle
import hydra
from omegaconf import DictConfig, ListConfig, OmegaConf
from langcodes import Language
from scispacy import umls_utils
from pathlib import Path
import json
import logging
import pandas as pd

from xmen.linkers import SapBERTLinker
from xmen.util import create_flat_term_dict
from xmen.knowledge_base import CompositeKnowledgebase

from scispacy.candidate_generation import create_tfidf_ann_index

log = logging.getLogger(__name__)

_TASKS = [
    "all",
    "assemble",
    "build_sapbert_index",
    "build_ngram_index"
]

@hydra.main(config_path="../conf", config_name="config")
def prepare_kbs(cfg : DictConfig) -> None:
    tasks = cfg.task

    if type(tasks) != list:
        tasks = [tasks]
    if tasks == ["all"]:
        tasks = [t for t in _TASKS if t != "all"]
        log.info("Running all tasks")
    
    for t in tasks:
        if not t in _TASKS:
            raise Exception(f"Unknown task {t}")
    
    log.info(f"Running tasks: {tasks}")

    if "assemble" in tasks:
        assemble(cfg)
    if "build_sapbert_index" in tasks:
        build_sapbert_index(cfg)
    if "build_ngram_index" in tasks:
        build_ngram_index(cfg)

def assemble(cfg : DictConfig):
    build_kbs = cfg.build_kbs if type(cfg.build_kbs) == ListConfig else [cfg.build_kbs]
    for assemble_config in build_kbs:
        split = assemble_config.split('-')
        if len(split) == 1:
            kb = assemble_config
            lang = None
        elif len(split) == 2:
            kb = split[0]
            lang = split[1]
        else:
            raise Exception(f'Invalid KB {assemble_config}')
        kb_config = cfg.kb.get(kb)
        if lang != None and lang != 'all' and lang in kb_config and not lang in kb_config.lang:
            raise Exception(f'Invalid language {lang} for {kb}')
        
        log.info(f"Building JSON for {assemble_config}")

        concept_details = get_concept_details(cfg, kb_config, kb, lang)

        n_concepts = len(concept_details)
        if n_concepts == 0:
            print('WARNING, list of concepts is empty')
        log.info(f'> Number of concepts: {n_concepts}')

        log.info(f'> Number of aliases: {get_alias_count(concept_details)}')

        output_path = get_kb_path(cfg, assemble_config) 
        output_path.parent.mkdir(exist_ok=True, parents=True)

        with open(output_path, 'w') as fout:
            for value in concept_details.values():
                fout.write(json.dumps(value) + "\n")     

def build_sapbert_index(cfg : DictConfig):
    if cfg.build_dicts == 'all':
        build_dicts = cfg.dict
    else:
        build_dicts = cfg.build_dicts
    
    for dict_name in build_dicts:
        dict_config = cfg.dict.get(dict_name)
        paths = [get_kb_path(cfg, kb) for kb in dict_config.kbs]
        log.info(f"> Building SapBERT index for {dict_name} with KBs: {dict_config.kbs}")

        index_folder = ensure_index_folder(cfg, dict_name)
        term_dict = create_flat_term_dict(paths)

        SapBERTLinker.write_dict_embeddings(
             out_dict_file=index_folder / cfg.sapbert.dict_file,
             out_embed_file=index_folder / cfg.sapbert.embed_file,
             jsonl_files=term_dict,
             cuda=(cfg.cuda is not None)
         )
            
def build_ngram_index(cfg : DictConfig):
    if cfg.build_dicts == 'all':
        build_dicts = cfg.dict
    else:
        build_dicts = cfg.build_dicts

    for dict_name in build_dicts:
        dict_config = cfg.dict.get(dict_name)
        paths = [get_kb_path(cfg, kb) for kb in dict_config.kbs]
        log.info(f"> Building n-gram index index for {dict_name} with KBs: {dict_config.kbs}")

        index_folder = ensure_index_folder(cfg, dict_name)
        kb = CompositeKnowledgebase(paths)

        pickle.dump(kb, open(index_folder / 'kb.pickle', 'wb'))

        create_tfidf_ann_index(index_folder, kb)

    print("I'm a building gnram")
    pass

def get_kb_path(cfg, kb_name):
    return Path(cfg.data_path) / f'{kb_name}.jsonl'

def ensure_index_folder(cfg, dict_name):
    p =  Path(cfg.data_path) / dict_name
    p.mkdir(exist_ok=True, parents=True)
    return p 

def get_concept_details(cfg, kb_config, kb, lang):
    if kb == 'umls' or kb_config.get('parent', None) == 'umls':
        return get_umls_concepts(cfg.kb.umls.meta_path, lang, 
            sabs = kb_config.get('sabs', []), 
            sources = kb_config.get('sources', []),  
            semantic_groups= kb_config.get('semantic_groups', None),  
            non_suppressed_only=kb_config.get('non_suppressed_only', False)
        )
    if kb == 'distemist':
        return get_dismetist_concepts(kb_config.distemist_path)    
    if kb == 'mugit':
        return get_mugit_concepts(cfg.kb.umls.meta_path, kb_config.mugit_path, kb_config.mugit_file)
    if kb == 'medlexsp':
        return get_medlexsp_concepts(kb_config.path)
    if kb == 'ops':
        return get_ops_concepts(kb_config.path)
    if kb == 'atc':
        return get_atc_concepts(kb_config.path)
    if kb == 'icd10':
        return get_icd10_concepts(kb_config.path)
    raise Exception(f'Unknown KB: {kb}')

def get_alias_count(concept_details):
    return sum([len(c['aliases']) + 1 for c in concept_details.values()])

def read_umls_sabs(meta_path):
    res = []
    sab_filename = "MRSAB.RRF"
    headers = umls_utils.read_umls_file_headers(meta_path, sab_filename)
    with open(f"{meta_path}/{sab_filename}") as fin:
        for line in fin:
            splits = line.strip().split("|")
            assert len(headers) == len(splits)
            sabs = dict(zip(headers, splits))
            res.append(sabs)
    return pd.DataFrame(res)

def filter_semantic_groups(sem_group_path, semantic_groups, concept_details):
    sem_groups = pd.read_csv(sem_group_path / 'SemGroups.txt', sep='|')
    sem_groups.columns = ['GRP', 'GRP_NAME', 'TUI', 'TUI_NAME']
    valid_tuis = sem_groups[sem_groups.GRP.isin(semantic_groups)].TUI.unique()
    print(valid_tuis)
    return {k:v for k, v in concept_details.items() if any([t in valid_tuis for t in v["types"]])}

#
# Adapted from: https://github.com/allenai/scispacy/blob/main/scripts/export_umls_json.py
#
def get_umls_concepts(meta_path : str, lang : str, sabs: list, sources : list, semantic_groups : list, non_suppressed_only=False) -> dict:
    if lang == 'all':
        lang = None
    else:
        lang_obj = Language.get(lang)
        assert lang_obj.is_valid()
        lang = lang_obj.to_alpha3(variant='B').upper()

    if not sabs:
        sabs = []

    if sources:
        sab_df = read_umls_sabs(meta_path)
        sabs += list(sab_df[sab_df.SF.isin(sources)].RSAB.unique())
    
    log.info(f'Using sources: {sabs}')

    concept_details = {}
    if not sabs:
        sabs = [ None ]
    for source in sabs:
        log.info(f'>> Reading concepts from {"all sources" if not source else source} and language {lang}')
        umls_utils.read_umls_concepts(meta_path, concept_details, source=source, lang=lang, non_suppressed=non_suppressed_only)

    log.info('>> Reading types ... ')
    umls_utils.read_umls_types(meta_path, concept_details)

    if semantic_groups:
        log.info(f'> Number of concepts before type-filtering: {len(concept_details)}')
        concept_details = filter_semantic_groups(Path(meta_path) / '..', semantic_groups, concept_details)

    log.info('>> Reading definitions ... ')
    umls_utils.read_umls_definitions(meta_path, concept_details)

    log.info(f'> Number of concepts before de-duplication: {len(concept_details)}')
    log.info(f'> Number of aliases before de-duplication: {get_alias_count(concept_details)}')

    for concept in concept_details.values():
        # Some concepts have many duplicate aliases. Here we remove them.
        concept["aliases"] = list(set(concept["aliases"]))

        # if a concept doesn't have a canonical name, use the first alias instead
        if 'canonical_name' not in concept:
            aliases = concept['aliases']
            concept['canonical_name'] = aliases[0]
            del aliases[0]

        # deleting `is_from_preferred_source`
        if 'is_from_preferred_source' in concept:
            del concept['is_from_preferred_source']

    return concept_details

def get_mugit_concepts(umls_meta_path : str, mugit_path : str, mugit_file : str) -> dict:
    concept_details = {}

    log.info('>> Reading concepts ...')

    mugit_interface = pd.read_csv(Path(mugit_path) / mugit_file, sep='\t', header=None)
    mugit_interface.columns = ['SNOMED_ID', 'TERM_ID', 'English', 'German']
    mugit_interface.set_index('SNOMED_ID', inplace=True)
    mugit_interface.sort_index(inplace=True)
    mugit_interface.dropna(inplace=True)

    concepts_filename = "MRCONSO.RRF"
    headers = umls_utils.read_umls_file_headers(umls_meta_path, concepts_filename)

    snomed_ids = set()

    with open(f"{umls_meta_path}/{concepts_filename}") as fin:
        for line in fin:
            splits = line.strip().split("|")
            assert len(headers) == len(splits), (headers, splits)
            concept = dict(zip(headers, splits))
            if concept['SAB'] == 'SNOMEDCT_US':
                snomed_id = int(concept['CODE'])
                if snomed_id in snomed_ids:
                    continue
                snomed_ids.add(snomed_id)
                if snomed_id in mugit_interface.index:
                    interface_terms = mugit_interface.loc[[snomed_id]]
                    concept_id = concept["CUI"]
                    if not concept_id in concept_details:
                        concept_details[concept_id] = {
                            "concept_id": concept_id,
                            "canonical_name" : None,
                            "types": [],
                            "aliases" : interface_terms.German.tolist()
                        }
                    else:
                        concept_details[concept_id]['aliases'] += interface_terms.German.tolist()

    # Remove duplicates
    for v in concept_details.values():
        v['aliases'] = list(set(v['aliases']))  

    log.info('>> Reading types ... ')
    umls_utils.read_umls_types(umls_meta_path, concept_details)

    log.info('>> Reading definitions ... ')
    umls_utils.read_umls_definitions(umls_meta_path, concept_details)

    for concept in concept_details.values():
        # deleting `is_from_preferred_source`
        if 'is_from_preferred_source' in concept:
            del concept['is_from_preferred_source']

    return concept_details

def get_dismetist_concepts(path : str) -> dict:
    distemist_dict = pd.read_csv(path, sep='\t')
    distemist_dict.sort_values('code', inplace=True)

    concept_details = {}

    for _, entry in distemist_dict.iterrows():
        sid = entry.code
        if not sid in concept_details:
            concept_details[sid] = {
                "concept_id": sid,
                "canonical_name" : None,
                "types": [],
                "aliases" : []
            }
        if entry.mainterm:
            assert not concept_details[sid]["canonical_name"]
            concept_details[sid]["canonical_name"] = entry.term
        else:
            concept_details[sid]["aliases"].append(entry.term)
        if not entry.semantic_tag in concept_details[sid]["types"]:
            concept_details[sid]["types"].append(entry.semantic_tag)

    for v in concept_details.values():
        if not v["canonical_name"]:
            v["canonical_name"] = v["aliases"].pop()
 
    return concept_details

def get_medlexsp_concepts(path : str) -> dict:
    #http://www.lllf.uam.es/ESP/nlpmedterm_en.html
    ...

def get_ops_concepts(path : str) -> dict:
    ...

def get_atc_concepts(path : str) -> dict:
    ...

def get_icd10_concepts(path : str) -> dict:
    ...

if __name__ == "__main__":
    prepare_kbs()