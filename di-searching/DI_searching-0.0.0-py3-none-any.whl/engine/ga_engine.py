import numpy as np
import copy
from typing import Any, Dict, Sequence, Tuple

from .base_search_engine import BaseSearchEngine, ENGINE_REGISTRY
from disearch.problem import ProblemHandler


@ENGINE_REGISTRY.register('ga')
class GeneticAlgorithmEngine(BaseSearchEngine):

    config = dict(
        cross_rate=0.1,
        mutate_rate=0.1,
        max_generation=100,
        population_size=100,
        verbose=False,
    )

    def __init__(self, cfg: Dict, search_space: "BaseSpace", random_state: Any = None) -> None:  # noqa
        super().__init__(cfg, search_space, random_state)
        self._cross_rate = self._cfg.cross_rate
        self._mutate_rate = self._cfg.mutate_rate

        self._handler = ProblemHandler(search_space)
        self._first_generation = True
        self._verbose = self._cfg.verbose

    def reset(self) -> None:
        self._handler.clear()
        self._first_generation = True

    def search(self, target_func) -> Tuple[np.ndarray, float]:
        for i in range(self._cfg.max_generation):
            pop = self.propose(self._cfg.population_size)
            score = self._handler.get_score(pop, target_func)
            self.update_score(pop, score)
            best_seq, best_score = self.provide_best()
            if not self._verbose:
                print(" Generation {} best score: {:.3f} .".format(i + 1, best_score))
        return best_seq, best_score

    def propose(self, candidate_num: int) -> np.ndarray:
        if self._first_generation:
            candidates = np.vstack([self._search_space.sample() for _ in range(candidate_num)])
            self._first_generation = False
        else:
            samples, scores = self._handler.get_all_data()
            parents_idx = self._random_state.choice(
                np.arange(len(self._handler)), candidate_num, True, p=scores / np.sum(scores)
            )
            parents = samples[parents_idx]
            children = self._crossover(parents, parents.copy())
            children = self._mutation(children)
            candidates = np.vstack(children)
        return candidates

    def _crossover(self, seqs: np.ndarray, pops: np.ndarray) -> np.ndarray:
        for i in range(len(seqs)):
            if self._random_state.rand() < self._cross_rate:
                j = self._random_state.randint(0, len(seqs), size=1)
                cross_points = self._random_state.randint(0, 2, len(self._search_space)).astype(bool)
                seqs[i, cross_points] = pops[j, cross_points]
        return seqs

    def _mutation(self, seqs: np.ndarray) -> np.ndarray:
        for seq in seqs:
            for point in range(len(self._search_space)):
                if self._random_state.rand() < self._mutate_rate:
                    seq[point] = self._random_state.randint(self._search_space.nshape[point])
        return seqs

    def update_score(self, sequences: np.ndarray, scores: np.ndarray) -> None:
        self._handler.update_data(sequences, scores)

    def provide_best(self) -> Tuple[np.ndarray, float]:
        if self._first_generation:
            return
        return self._handler.provide_best()
