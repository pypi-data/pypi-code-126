# Copyright 2021 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""Module for building neural networks in the MLCVZoo"""
from abc import ABC, abstractmethod

__author__ = "Thilo Bauer"
__license__ = "Open Logistics License 1.0"
__email__ = "thilo.bauer@dbschenker.com"

from typing import Optional


class NetConfiguration:
    """
    A net configuration.
    """

    def __init__(self) -> None:
        pass


class Net(ABC):
    """
    The net is held and used by any of the sub-classes of interface NetBased.
    This class provides methods to initialize, store or restore the net.
    """

    def __init__(self) -> None:
        self.initialize()

    @abstractmethod
    def initialize(self) -> str:
        """
        Initializes the network, must be implemented by subclasses
        """
        raise NotImplementedError("Must be implemented by sub-class: initialize(...)")

    @abstractmethod
    def store(
        self,
        configuration: Optional[NetConfiguration] = None,
        net_path: Optional[str] = None,
    ) -> None:
        """
        The method stores the weights of the net either by the given configuration or a given
        file path via net_path
        """
        raise NotImplementedError("Must be implemented by sub-class: store(...)")

    @abstractmethod
    def restore(
        self,
        configuration: Optional[NetConfiguration] = None,
        net_path: Optional[str] = None,
    ) -> None:
        """
        The method restores the weights of the net either by the given configuration or a given
        file path via net_path
        """
        raise NotImplementedError("Must be implemented by sub-class: restore(...)")
