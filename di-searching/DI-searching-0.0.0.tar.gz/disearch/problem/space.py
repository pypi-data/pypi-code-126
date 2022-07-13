from abc import ABC, abstractclassmethod, abstractproperty
from math import ceil
from typing import Any, List, Type, Union

import numpy as np


class BaseSpace(ABC):
    r"""
    Abstract class of `space`.

    :param List shape: the shape of space, defaults to None
    :param Type dtype: the type of space, defaults to None
    :param Any random_state: the random method for space to generate sample, defaults to None
    """

    def __init__(self, shape: List = None, dtype: Type = None, random_state: Any = None) -> None:
        self._shape = None if shape is None else np.array(shape)
        self._dtype = None if dtype is None else np.dtype(dtype)
        if random_state is None:
            self._random_state = np.random.RandomState()
        elif isinstance(random_state, int):
            self._random_state = np.random.RandomState(random_state)
        elif isinstance(random_state, np.random.RandomState):
            self._random_state = random_state
        else:
            raise TypeError(f'Unknown random state type - {repr(random_state)}.')

    @abstractclassmethod
    def sample(self) -> np.ndarray:
        """
        Get a random sample from the space.

        :return np.ndarray: The random sample.
        """
        raise NotImplementedError

    @property
    def shape(self) -> np.ndarray:
        """
        Shape array of the space. It should be equal to the `shape` of a sample in space.

        :return np.ndarray: shape array.
        """
        return self._shape

    @property
    def dtype(self) -> Type:
        """
        Data type of the samples in searching space.

        :return Type: dtype.
        """
        return self._dtype


class DiscreteSpace(BaseSpace):
    """
    Discrete search space. It is configured by a input value or a list.
    The element of input at each position determinates the discrete
    space for each dim.

    :param List shape: list of space shape, defaults to None
    :param Type dtype: data type of samples, defaults to np.int64
    :param Any random_state: random state of sampler, defaults to None

    :Examples:

    >>> space = DiscreteSpace((2, 3, 4))
    >>> space.shape
    array([3, ])
    >>> x = space.sample()
    >>> x
    array([1, 1, 0])
    """

    def __init__(self, shape: List = None, dtype: Type = np.int64, random_state: Any = None) -> None:
        assert (np.array(shape) > 0).all(), "shape must be positive"
        if np.isscalar(shape):
            shape = [shape]
        self._nshape = np.asarray(shape, dtype=dtype)
        shape = self._nshape.shape

        super().__init__(shape, dtype, random_state)

    def sample(self) -> np.ndarray:
        sample = self._random_state.random_sample(self._nshape.shape) * self._nshape
        return sample.astype(self._dtype)

    def sample_single(self, position: int) -> int:
        """
        Get a random value at the position of the discrete space.

        :param int position: the position in the space to sample
        :return int: the random value at position
        """
        assert position < len(self._nshape)
        return self._random_state.randint(self._nshape[position])

    def __len__(self) -> int:
        return self._nshape.size

    @property
    def nshape(self) -> np.ndarray:
        """
        List of the space shape.

        :return np.ndarray: nshape
        """
        return self._nshape


class SeparateSpace(BaseSpace):
    """
    Separate search space. It is defined by a range of `start`, `end` and step to determine a list
    of values, and its dimension.

    :param int start: start value
    :param int end: end value, will NOT included in the space
    :param int step: step length, defaults to 1
    :param Union[int, List] dim: dimension or repeat times of the space, defaults to 1
    :param Type dtype: data type of space, defaults to np.int64
    :param Any random_state: random state for sampler, defaults to None

    :Examples:

    >>> space = SeparateSpace(start=1, end=6, step=2, dim=1)
    >>> space.shape
    array([1, ])
    >>> space.sample()  # must be in [1, 3, 5]
    1
    """

    def __init__(
            self,
            start: int,
            end: int,
            step: int = 1,
            dim: Union[int, List] = 1,
            dtype: Type = np.int64,
            random_state: Any = None
    ) -> None:
        self._start = start
        self._end = end
        self._step = step
        if np.isscalar(dim):
            dim = [dim]
        self._dim = np.array(dim)
        assert self._start >= 0 and self._end > 0 and self._step > 0 and (self._dim > 0).all(), \
            "all args must be positive!"
        self._count = ceil((self._end - self._start) / self._step)
        super().__init__(dim, dtype, random_state)

    def sample(self) -> np.ndarray:
        sample = self._random_state.randint(self._count, size=self._dim)
        sample = sample * self._step + self._start
        return sample.astype(self._dtype)

    def __len__(self) -> int:
        return self._count

    @property
    def nshape(self) -> np.ndarray:
        return self._shape


class ContinuousSpace(BaseSpace):
    """
    Continuous search space. The space is defined by its shape and lower/higher bounds, with continuous value.
    Users can set the lower and higher boundary of each dimension of the space, otherwise the value will be
    infinite at these dimensions. Each dimension can have different boundary types and values. If so, the shape
    of boundary argument must be the same as space's shape.

    :param List shape: shape of the space
    :param float low: the lower bound of space, defaults to None
    :param float high: the higher bound of space, defaults to None
    :param Type dtype: data type of space, defaults to np.float32
    :param Any random_state: random space of sampler, defaults to None

    :Example:

    >>> space = ContinuousSpace(shape=(2, 3), low=0, high=((5, 5, 5), (8, 8, 8)))
    >>> space.shape
    array([2, 3])
    >>> space.sample()
    array([[2.7791994, 4.216622 , 3.0280395],
       [4.2073464, 7.35141  , 2.5952444]], dtype=float32)
    """

    def __init__(
            self,
            shape: List,
            low: float = None,
            high: float = None,
            dtype: Type = np.float32,
            random_state: Any = None
    ) -> None:
        assert dtype is not None, "dtype must be explicitly provided."
        if np.isscalar(shape):
            shape = [shape]

        super().__init__(shape, dtype, random_state)

        if low is not None:
            assert (np.isscalar(low) or low.shape == self._shape), \
                "low.shape doesn't match provided shape"
            if np.isscalar(low):
                low = np.full(self._shape, low)
        else:
            low = np.full(self._shape, -np.inf)
        if high is not None:
            assert (np.isscalar(high) or high.shape == self._shape), \
                "low.shape doesn't match provided shape"
            if np.isscalar(high):
                high = np.full(self._shape, high)
        else:
            high = np.full(self._shape, np.inf)

        self._low = low.astype(dtype)
        self._high = high.astype(dtype)

        self._bounded_below = -np.inf < self._low
        self._bounded_above = np.inf > self._high

    def sample(self) -> np.ndarray:
        """
        Get a random sample from the space. unbounded dimension will be sampled from a normal distribution,
        dimensions with one bound will be sampled from a exponential distribution. Others will be sampled
        from a exponential distribution.

        :return np.ndarray: The random sample.
        """
        sample = np.empty(self._shape)

        unbounded = ~self._bounded_below & ~self._bounded_above
        upp_bounded = ~self._bounded_below & self._bounded_above
        low_bounded = self._bounded_below & ~self._bounded_above
        bounded = self._bounded_below & self._bounded_above

        sample[unbounded] = np.random.normal(size=unbounded[unbounded].shape)
        sample[low_bounded] = (np.random.exponential(size=low_bounded[low_bounded].shape) + self._low[low_bounded])

        sample[upp_bounded] = (-np.random.exponential(size=upp_bounded[upp_bounded].shape) + self._high[upp_bounded])

        sample[bounded] = np.random.uniform(
            low=self._low[bounded], high=self._high[bounded], size=bounded[bounded].shape
        )

        return sample.astype(self._dtype)

    def __len__(self) -> int:
        return np.prod(self._shape)

    @property
    def nshape(self) -> np.ndarray:
        return self._shape

    @property
    def bounds(self) -> np.ndarray:
        return np.array(list(zip(self._low, self._high)))


class HybridSpace(BaseSpace):
    """
    Hybrid searching space consists of one or more kinds of space above.

    :param space_kwargs: the provided space list

    :Example:

    >>> s1 = DiscreteSpace(3)
    >>> s2 = ContinuousSpace(2)
    >>> space = HybridSpace(s1, s2)
    >>> space.shape
    [array([1]), array([2])]
    >>> space.sample()
    [array(1), array([-0.35141  , 1.5952444], dtype=float32)]
    """

    def __init__(self, *space_kwargs) -> None:
        self._spaces = []
        for space in space_kwargs:
            self._spaces.append(space)

    def sample(self) -> np.ndarray:
        """
        Get a list of random samples from each space.

        :return np.ndarray: sample list
        """
        samples = np.zeros(shape=(len(self, )), dtype=object)
        for i in range(len(self)):
            space = self._spaces[i]
            samples[i] = space.sample()
        return np.array(samples, dtype=object)

    def __len__(self) -> int:
        """
        Get the num of spaces.

        :return int: space num
        """
        return len(self._spaces)

    @property
    def shape(self) -> List:
        """
        Get a shape list of each space.

        :return List: space list
        """
        shape = []
        for space in self._spaces:
            shape.append(space.shape)
        return shape

    @property
    def nshape(self) -> np.ndarray:
        """
        get a nshape list of each space.

        :return np.ndarray: nshape list
        """
        nshape = []
        for space in self._spaces:
            nshape.append(space.nshape)
        return np.array(nshape)
