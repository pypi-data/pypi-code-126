import imp
from typing import Iterable
from itertools import groupby
import pandas as pd

import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    from neleval.evaluate import Evaluate, StrictMetricWarning
    from neleval.configs import get_measure
    from neleval.annotation import Annotation, Candidate
    from neleval.document import Document
    from neleval.prepare import SelectAlternatives

# constants for interacting with different neleval measures
_PARTIAL_EVAL_MEASURE_FMT_STRING = 'overlap-maxmax:None:span+kbid'
_PARTIAL_EVAL_MEASURE = get_measure(_PARTIAL_EVAL_MEASURE_FMT_STRING)

# equivalent to strong_all_match
_STRICT_EVAL_MEASURE_FMT_STRING = 'sets:None:span+kbid'
_STRICT_EVAL_MEASURE = get_measure(_STRICT_EVAL_MEASURE_FMT_STRING)

_NER_STRICT_EVAL_MEASURE_FMT_STRING = 'sets:None:span'
_NER_STRICT_EVAL_MEASURE = get_measure(_NER_STRICT_EVAL_MEASURE_FMT_STRING)

# constants for interacting with different neleval measures
_NER_PARTIAL_EVAL_MEASURE_FMT_STRING = 'overlap-maxmax:None:span'
_NER_PARTIAL_EVAL_MEASURE = get_measure(_NER_PARTIAL_EVAL_MEASURE_FMT_STRING)

# Any match within the unit / sentence counts
_LOOSE_EVAL_MEASURE_FMT_STRING = 'sets:None:docid+kbid'
_LOOSE_EVAL_MEASURE = get_measure(_LOOSE_EVAL_MEASURE_FMT_STRING)

#def weighting_function_candidates_kbids(c1, c2):
#    if c1 == c2 or len(set(c1.split("/")).intersection(c2.split("/"))) > 0:
#        return 1
#    return 0

def entity_linking_error_analysis(ground_truth : Iterable, prediction : Iterable, allow_multiple_gold_candidates = False) -> pd.DataFrame:
    """
    Assuming entities are aligned
    """
    res = []
    for gt, pred in zip(ground_truth, prediction):
        error_df = _get_error_df(gt["entities"], pred["entities"], allow_multiple_gold_candidates)
        error_df['corpus_id'] = gt['corpus_id']
        error_df['document_id'] = gt['document_id']
        res.append(error_df)
    return pd.concat(res)

def _get_error_df(gt_ents : list, pred_ents: list, allow_multiple_gold_candidates = False) -> pd.DataFrame: 
    def get_items(entities):
        return  [(e['offsets'][0][0], e['offsets'][-1][1], e['normalized'], e['text']) for e in entities]
    gt_items = get_items(gt_ents)
    pred_items = get_items(pred_ents)

    ent_res = []

    def record_match(pred_s, pred_e, pred_c, pred_text, gt_s, gt_e, gt_c, gt_text, e_match_type):
        if not gt_c:
            return
        if not pred_c and gt_c:
            ent_res.append(
                {
                    'pred_start' : pred_s,
                    'pred_end' : pred_e,
                    'pred_text' : pred_text,
                    'gt_start' : gt_s,
                    'gt_end' : gt_e,
                    'gt_text' : gt_text,
                    'entity_match_type' : e_match_type,
                    'gold_concept' : gt_concept,
                    #'gold_type' : '',
                    'pred_index' : -1,
                    'pred_index_score' : None,
                    'pred_top': None,
                    'pred_top_score' : None,
                }
            )

        if allow_multiple_gold_candidates:
            raise Exception("Not yet implemented")
        else:
            for gt_concept in gt_c:
                pred_ids = [c['db_id'] for c in pred_c]
                idx = pred_ids.index(gt_concept['db_id']) if gt_concept['db_id'] in pred_ids else -1
                ent_res.append(
                    {
                        'pred_start' : pred_s,
                        'pred_end' : pred_e,
                        'pred_text' : pred_text,
                        'gt_start' : gt_s,
                        'gt_end' : gt_e,
                        'gt_text' : gt_text,
                        'entity_match_type' : e_match_type,
                        'gold_concept' : gt_concept,
                        #'gold_type' : gt_type,
                        'pred_index' : idx,
                        'pred_index_score' : pred_c[idx].get("score", None) if idx >= 0 else None,
                        'pred_top' : pred_c[0]["db_id"] if len(pred_c) > 0 else None,
                        'pred_top_score' : pred_c[0].get("score", None) if len(pred_c) > 0 else None,
                    }
                )

    while gt_items or pred_items:
        if not gt_items:
            e_match_type = 'fp'
            pred_s, pred_e, pred_c, pred_text = pred_items.pop()
            record_match(pred_s, pred_e, pred_c, pred_text, gt_s, gt_e, gt_c, gt_text, e_match_type)
        elif not pred_items:
            e_match_type = 'fn'
            gt_s, gt_e, gt_c, gt_text = gt_items.pop()
            record_match(pred_s, pred_e, pred_c, pred_text, gt_s, gt_e, gt_c, gt_text, e_match_type)
        else: 
            pred_s, pred_e, pred_c, pred_text = pred_items[0]
            gt_s, gt_e, gt_c, gt_text = gt_items[0]

            if pred_s == gt_s and pred_e == gt_e:
                e_match_type = 'tp'
                record_match(pred_s, pred_e, pred_c, pred_text, gt_s, gt_e, gt_c, gt_text, e_match_type)
                gt_items.pop(0)
                pred_items.pop(0)
            elif pred_s >= gt_e:
                e_match_type = 'fn'
                record_match(pred_s, pred_e, pred_c, pred_text, gt_s, gt_e, gt_c, gt_text, e_match_type)
                gt_items.pop(0)
            elif pred_e <= gt_s:
                e_match_type = 'fp'
                record_match(pred_s, pred_e, pred_c, pred_text, gt_s, gt_e, gt_c, gt_text, e_match_type)
                pred_items.pop(0)
            else:
                e_match_type = 'be'
                pred_s, pred_e, pred_c, pred_text = pred_items.pop(0)
                gt_s, gt_e, gt_c, gt_text = gt_items.pop(0)
                while True:
                    record_match(pred_s, pred_e, pred_c, pred_text, gt_s, gt_e, gt_c, gt_text, e_match_type)
                    if pred_e < gt_e:
                        if pred_items and pred_items[0][0] <= gt_e:
                            pred_s, pred_e, pred_c, pred_text = pred_items.pop(0)
                        else:
                            if gt_items:
                                gt_items.pop(0)
                            break
                    elif gt_e < pred_e:
                        if gt_items and gt_items[0][0] <= pred_e:
                            gt_s, gt_e, gt_c, gt_text = gt_items.pop(0)
                        else:
                            if pred_items:
                                pred_items.pop(0)
                            break
                    else:                    
                        break

    return pd.DataFrame(ent_res)
    
def evaluate(ground_truth : Iterable, prediction : Iterable, allow_multiple_gold_candidates = False, top_k_predictions=None, threshold=None, ner_only=False) -> dict:
    with warnings.catch_warnings():
        # Ignore division by zero problems raised by neleval
        warnings.filterwarnings("ignore", category=StrictMetricWarning)
        if ner_only:
            allow_multiple_gold_candidates = False
        system_docs = list(_to_nel_eval(prediction, allow_multiple_candidates=False, top_k=top_k_predictions, threshold=threshold, ner_only=ner_only))
        gold_docs = list(_to_nel_eval(ground_truth, allow_multiple_candidates=allow_multiple_gold_candidates, top_k=None, threshold=None, ner_only=ner_only))
        
        num_annos_system = sum([len(a.candidates) for d in system_docs for a in d.annotations])
        num_annos_gold = sum([len(a.candidates) for d in gold_docs for a in d.annotations])

        if allow_multiple_gold_candidates:
            SelectAlternatives(system_docs, gold_docs)()        
        
        eval = Evaluate(
            system = system_docs, 
            gold = gold_docs, 
            measures = { _STRICT_EVAL_MEASURE, _LOOSE_EVAL_MEASURE, _PARTIAL_EVAL_MEASURE, _NER_STRICT_EVAL_MEASURE, _NER_PARTIAL_EVAL_MEASURE }
        )
        res = eval()
        for v in res.values():
            v['n_docs_system'] = len(system_docs)
            v['n_annos_system'] = num_annos_system
            v['n_docs_gold'] = len(gold_docs)
            v['n_annos_gold'] = num_annos_gold
        metrics = {
            'strict' : res[_STRICT_EVAL_MEASURE_FMT_STRING], 
            'partial' : res[_PARTIAL_EVAL_MEASURE_FMT_STRING],
            'loose' : res[_LOOSE_EVAL_MEASURE_FMT_STRING],
            'ner_strict' : res[_NER_STRICT_EVAL_MEASURE_FMT_STRING],
            'ner_partial' : res[_NER_PARTIAL_EVAL_MEASURE_FMT_STRING],
        }
        return metrics

def _to_nel_eval(units : Iterable, allow_multiple_candidates : bool = False, top_k : int = None, threshold : float = None, ner_only = False) -> Iterable:
    for u in units:
        entities = u['entities']
        unit_id = u['corpus_id'] + u['document_id']
        annotations = []
        for e in entities:
            if 'normalized' in e:
                for c in e['normalized']:
                    if not 'type' in c:
                        c['type'] = None
                    if not 'score' in c:
                        c['score'] = None
            else:
                e['normalized'] = []
            start, end = e['offsets'][0][0], e['offsets'][-1][1]
            if ner_only:                    
                anno = Annotation(unit_id, start, end, [])
                annotations.append(anno)
            else:                   
                candidates = []
                for c in e['normalized']:
                    if not threshold or not c['score'] or c['score'] >= threshold:
                        candidates.append(Candidate(c['db_id'], c['score'], c['type']))    
                candidates.sort(key=lambda c: -c.score if c.score else 0)
                if top_k:
                    candidates = candidates[:top_k]
                if allow_multiple_candidates:
                    anno = Annotation(unit_id, start, end, candidates)
                    annotations.append(anno)
                else:
                    for cand in candidates:
                        anno = Annotation(unit_id, start, end, [cand])
                        annotations.append(anno)
        yield Document(unit_id, annotations)