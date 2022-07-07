"""core functions for mainframe"""

from abc import abstractmethod
from pydantic.dataclasses import dataclass
from pyro.infer import Predictive


@dataclass
class Simulator:
    num_samples: int = 1000

    @abstractmethod
    def model(self):
        raise NotImplementedError("model() must be implemented")

    @property
    def samples(self):
        return Predictive(self.model, {}, num_samples=self.num_samples)()
