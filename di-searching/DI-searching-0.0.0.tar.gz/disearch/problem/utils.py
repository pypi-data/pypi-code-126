from typing import Tuple
import numpy as np

from .space import HybridSpace


def make_hashable(x):
    if isinstance(x, np.ndarray):
        if x.dtype == object:
            x_ = x.copy()
            x = []
            for xi in x_:
                x += xi.flatten().tolist()
        else:
            x = x.flatten()
    return tuple(map(float, x))


class DataPool():

    def __init__(self, search_space: "BaseSpace") -> None:  # noqa
        if isinstance(search_space, HybridSpace):
            self._samples = np.empty(shape=(0, len(search_space)))
        else:
            self._samples = np.empty(shape=(0, *search_space.shape))
        self._scores = np.empty(shape=(0, ))
        self._best_idx = None
        self._sample_dict = {}

    def update(self, samples: np.ndarray, scores: np.ndarray) -> None:
        new_idx = []
        for i in range(samples.shape[0]):
            sample, score = samples[i], scores[i]
            if make_hashable(sample) not in self._sample_dict:
                self._sample_dict[make_hashable(sample)] = score
                new_idx.append(i)
        self._samples = np.concatenate([self._samples, samples[new_idx]], axis=0)
        self._scores = np.concatenate([self._scores, scores[new_idx]], axis=0)
        self._best_idx = np.argmax(self._scores)

    def get_score(self, samples: np.ndarray) -> np.ndarray:
        scores = []
        for sample in samples:
            try:
                score = self._sample_dict[make_hashable(sample)]
            except KeyError:
                print(f"sample {sample} not found in cache!")
                score = None
            scores.append(score)
        return scores

    def __len__(self) -> int:
        return len(self._sample_dict)

    def clear(self) -> None:
        self._searched_samples = np.empty(shape=(0, *self._samples.shape[1:]))
        self._searched_scores = np.empty(shape=0)
        self._sample_dict = {}
        self._best_idx = None

    @property
    def data(self) -> Tuple[np.ndarray, np.ndarray]:
        return self._samples, self._scores

    @property
    def best(self) -> Tuple[np.ndarray, float]:
        if self._best_idx is None:
            raise ValueError("sample pool is empty!")
        return self._samples[self._best_idx], self._scores[self._best_idx]
