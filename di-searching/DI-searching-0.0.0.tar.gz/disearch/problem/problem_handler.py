import numpy as np
from typing import Any, Callable, Dict, List, Tuple

from .utils import DataPool


class ProblemHandler():
    """
    This class is used to provide a uniformed interface for the searching engine to
    interact with. It can store the searching space class, provide an entry to get a
    batch of scores from provided samples and hold all the searched results.

    :param BaseSpace search_space: Search space of handler.

    :Examples:

    >>> def target_func(x):
    >>>     ...
    >>> space = DiscreteSpace(5)
    >>> handler = ProblemHandler(space)
    >>> x = space.sample()
    >>> y = handler.get_score(np.array([x]), target_func)
    >>> x, y
    array([ 2 ]) array([ -2.25 ])
    >>> handler.get_all_data()
    array([[ 2 ]]) array([ -2.25 ])
    """

    def __init__(
            self,
            search_space: "BaseSpace",  # noqa
    ) -> None:
        self._search_space = search_space
        self._data_pool = DataPool(search_space)

    def get_score(self, new_samples: np.ndarray, target_function: Callable) -> np.ndarray:
        """
        Get scores of a batch of samples from target function. All samples and scores will be stored.

        :param np.ndarray new_samples: Samples to get scores.
        :param Callable target_function: Target function. The input and output should be one sample.
        :return np.ndarray: Scores of all provided samples.
        """
        scores = []
        for sample in new_samples:
            score = target_function(sample)
            scores.append(score)
        scores = np.array(scores)
        self._data_pool.update(new_samples, scores)
        return scores

    def get_cached_score(self, samples: np.ndarray) -> List:
        """
        Get scores of a batch of sample from stored scores. All the samples must be searched or updated
        before. Otherwise the score will be `None`.

        :param np.ndarray samples: Samples to get scores.
        :return List: Scores of all provided samples stored as `List` for there will be `None` elements.
        """
        return self._data_pool.get_score(samples)

    def get_all_data(self) -> Tuple[np.ndarray, np.ndarray]:
        """
        Get all stores sample and scores.

        :return Tuple[np.ndarray, np.ndarray]: Stores samples and scores.
        """
        return self._data_pool.data

    def update_data(self, samples: np.ndarray, scores: np.ndarray) -> None:
        """
        Update a batch of samples and scores. If not stored already, they will be added into data pool.

        :param np.ndarray samples: Samples to be updated
        :param np.ndarray scores: Scores to be updated
        """
        assert samples.shape[0] == scores.shape[0], "sample and score must have the same num"
        self._data_pool.update(samples, scores)

    def provide_best(self) -> Tuple[np.ndarray, float]:
        """
        Get the currently best sample and its score in the data pool.

        :return Tuple[np.ndarray, float]: best sample and its score
        """
        if len(self) == 0:
            return
        return self._data_pool.best

    def __len__(self) -> int:
        return len(self._data_pool)

    @property
    def space(self) -> "BaseSpace":  # noqa
        return self._search_space

    @property
    def best_score(self) -> float:
        """
        Get the currently best score only.

        :return float: best score
        """
        if len(self._data_pool) == 0:
            return -np.inf
        return self._data_pool.best[1]

    def reset(self) -> None:
        """
        Reset the handler. Clear data pool.
        """
        self._data_pool.clear()
