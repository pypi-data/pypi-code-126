import numpy as np
from typing import Any, Dict, Callable

from .base_search_engine import BaseSearchEngine, ENGINE_REGISTRY
from disearch.problem import ProblemHandler


@ENGINE_REGISTRY.register('random')
class RandomEngine(BaseSearchEngine):

    config = dict(num_sample=100, )

    def __init__(self, cfg: Dict, search_space: "BaseSpace", random_state: Any = None) -> None:  # noqa
        super().__init__(cfg, search_space, random_state)
        self._handler = ProblemHandler(search_space)

    def reset(self):
        self._handler.clear()

    def search(self, target_func: Callable):
        samples = self.propose(self._cfg.num_sample)
        self._handler.get_score(samples, target_func)
        return self.provide_best()

    def propose(self, sample_num: int) -> np.ndarray:
        samples = []
        for _ in range(sample_num):
            samples.append(self._search_space.sample())
        return np.array(samples)

    def update_score(self, samples: np.ndarray, scores: np.ndarray) -> None:
        self._handler.update_data(samples, scores)

    def provide_best(self):
        return self._handler.provide_best()
