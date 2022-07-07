import pyro.distributions as dist
from mainframe.compoments.core import stochastic


def gaussian(name: str: "gaussian_noise") -> torch.Tensor:
    return stochastic(name, dist.Normal(0, 1))
