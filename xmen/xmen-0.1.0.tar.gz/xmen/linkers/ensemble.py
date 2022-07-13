
from typing import Dict
from xmen.linkers import EntityLinker
from datasets import Dataset
from datasets import utils
import numpy as np

class EnsembleLinker(EntityLinker):

    def __init__(self):
        self.linkers_fn = {}
        self.linkers_k = {}
        self.linker_thresholds = {}
        self.linker_weigths = {}

    def add_linker(self, name, linker, k=1, threshold=0.0, weight=1.0):
        self.add_linker_fn(name, lambda: linker, k, threshold, weight)

    def add_linker_fn(self, name, linker_fn, k=1, threshold=0.0, weight=1.0):
        self.linkers_fn[name] = linker_fn
        self.linkers_k[name] = k
        self.linker_thresholds[name] = threshold
        self.linker_weigths[name] = weight

    @staticmethod
    def filter_and_apply_threshold(input_pred, k : int, threshold : float):
        assert k >= 0
        def apply(entry):
            entities = entry['entities']
            for e in entities:
                filtered = [n for n in e['normalized'] if 'score' in n and n['score'] >= threshold] 
                e['normalized'] = sorted(filtered, key=lambda n: n['score'])[-1::-1][:k]
            return { 'entities' : entities }
        return input_pred.map(apply, load_from_cache_file=False)

    def predict_batch(self, dataset, batch_size, top_k=None, reuse_preds=None):
        def merge_linkers(batch, index):
            progress = utils.logging.is_progress_bar_enabled()
            try:
                mapped = {}
                if progress:
                    utils.logging.disable_progress_bar()

                for linker_name, linker_fn in self.linkers_fn.items():
                    if reuse_preds:
                        linked = reuse_preds[linker_name].select(index)
                    else:
                        linker = linker_fn()
                        print('Running', linker_name)
                        linked = linker.predict_batch(Dataset.from_dict(batch), batch_size)    
                    mapped[linker_name] = self.filter_and_apply_threshold(
                        linked, self.linkers_k[linker_name], self.linker_thresholds[linker_name])['entities']
    
                entities = []

                for i, doc in enumerate(batch['entities']):
                    for j, e in enumerate(doc):
                        e['normalized'] = []
                        for linker_name in mapped.keys():
                            linker_scores = []
                            for n in mapped[linker_name][i][j]['normalized']:
                                n['predicted_by'] = linker_name
                                if 'score' in n:
                                    n['score'] *= self.linker_weigths[linker_name]
                                linker_scores.append(n)
                            e['normalized'] += linker_scores
                        e['normalized'] = sorted(e['normalized'], key=lambda n: n['score'])[-1::-1]
                        if top_k:
                            e['normalized'] = e['normalized'][:top_k]
                                
                    entities.append(doc)
            finally:
                if progress:
                    utils.logging.enable_progress_bar()
            return {'entities' : entities }

        return dataset.map(merge_linkers, with_indices=True, batched=True, batch_size=batch_size, load_from_cache_file=False)
        
        # def merge_concepts(concepts_i : list) -> list:
        #     assert len(concepts_i) > 0
        #     res = []
        #     for ent_concepts in zip(*concepts_i):
        #         def merge_values(k):
        #             return np.array([s for c in ent_concepts for s in c[k]])
        #         scores = merge_values('score')
        #         linker_weights = [self.linker_weights[l] for l in merge_values('predicted_by')]
        #         if len(scores) > 0:
        #             scores += np.linspace(0.0001, 0.00, len(scores))
        #         scores *= linker_weights
        #         order = np.argsort(scores, kind='stable')[-1::-1]
        #         if top_k:
        #             order = order[:top_k]
        #         merged = {}
        #         for k in ent_concepts[0].keys():
        #             if k == 'score':
        #                 merged[k] = scores[order]
        #             else:
        #                 merged[k] = list(merge_values(k)[order])
        #         res.append(merged)
        #     return res
        
        # def get_entities(item, i):
        #     ents = item["entities"].copy()
        #     concepts_i = [v[i].copy() for v in concepts.values()]
        #     ents["concepts"] = merge_concepts(concepts_i)
        #     return ents
        
        # return dataset.map(lambda item, i: {'entities' : get_entities(item, i)}, with_indices=True, load_from_cache_file=False)        

    def predict(self, unit : str, entities : dict) -> dict:
        raise NotImplementedError() 
