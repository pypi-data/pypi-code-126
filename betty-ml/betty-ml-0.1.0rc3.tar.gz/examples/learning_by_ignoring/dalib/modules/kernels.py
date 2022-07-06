from typing import Optional, List
import torch
import torch.nn as nn
from numpy import array, dot
import numpy as np
from qpsolvers import solve_qp


__all__ = ["GaussianKernel"]


class GaussianKernel(nn.Module):
    r"""Gaussian Kernel Matrix

    Gaussian Kernel k is defined by

    .. math::
        k(x_1, x_2) = \exp \left( - \dfrac{\| x_1 - x_2 \|^2}{2\sigma^2} \right)

    where :math:`x_1, x_2 \in R^d` are 1-d tensors.

    Gaussian Kernel Matrix K is defined on input group :math:`X=(x_1, x_2, ..., x_m),`

    .. math::
        K(X)_{i,j} = k(x_i, x_j)

    Also by default, during training this layer keeps running estimates of the
    mean of L2 distances, which are then used to set hyperparameter  :math:`\sigma`.
    Mathematically, the estimation is :math:`\sigma^2 = \dfrac{\alpha}{n^2}\sum_{i,j} \| x_i - x_j \|^2`.
    If :attr:`track_running_stats` is set to ``False``, this layer then does not
    keep running estimates, and use a fixed :math:`\sigma` instead.

    Parameters:
        - sigma (float, optional): bandwidth :math:`\sigma`. Default: None
        - track_running_stats (bool, optional): If ``True``, this module tracks the running mean of :math:`\sigma^2`.
          Otherwise, it won't track such statistics and always uses fix :math:`\sigma^2`. Default: ``True``
        - alpha (float, optional): :math:`\alpha` which decides the magnitude of :math:`\sigma^2` when track_running_stats is set to ``True``

    Inputs:
        - X (tensor): input group :math:`X`

    Shape:
        - Inputs: :math:`(minibatch, F)` where F means the dimension of input features.
        - Outputs: :math:`(minibatch, minibatch)`
    """

    def __init__(
        self,
        sigma: Optional[float] = None,
        track_running_stats: Optional[bool] = True,
        alpha: Optional[float] = 1.0,
    ):
        super(GaussianKernel, self).__init__()
        assert track_running_stats or sigma is not None
        self.sigma_square = torch.tensor(sigma * sigma) if sigma is not None else None
        self.track_running_stats = track_running_stats
        self.alpha = alpha

    def forward(self, X: torch.Tensor) -> torch.Tensor:
        l2_distance_square = ((X.unsqueeze(0) - X.unsqueeze(1)) ** 2).sum(2)

        if self.track_running_stats:
            self.sigma_square = self.alpha * torch.mean(l2_distance_square.detach())

        return torch.exp(-l2_distance_square / (2 * self.sigma_square))


def optimal_kernel_combinations(kernel_values: List[torch.Tensor]) -> torch.Tensor:
    # use quadratic program to get optimal kernel
    num_kernel = len(kernel_values)
    kernel_values_numpy = array(
        [float(k.detach().cpu().data.item()) for k in kernel_values]
    )
    if np.all(kernel_values_numpy <= 0):
        beta = solve_qp(
            P=-np.eye(num_kernel),
            q=np.zeros(num_kernel),
            A=kernel_values_numpy,
            b=np.array([-1.0]),
            G=-np.eye(num_kernel),
            h=np.zeros(num_kernel),
        )
    else:
        beta = solve_qp(
            P=np.eye(num_kernel),
            q=np.zeros(num_kernel),
            A=kernel_values_numpy,
            b=np.array([1.0]),
            G=-np.eye(num_kernel),
            h=np.zeros(num_kernel),
        )
    beta = beta / beta.sum(axis=0) * num_kernel  # normalize
    return sum([k * b for (k, b) in zip(kernel_values, beta)])
